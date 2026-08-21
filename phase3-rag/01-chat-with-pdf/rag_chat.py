import chromadb
from chromadb.utils import embedding_functions
from pypdf import PdfReader
import ollama

# ---- Step 1: Extract text from PDF ----
def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# ---- Step 2: Chunk the text ----
def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

# ---- Step 3: Setup Chroma (vector database) ----
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
client = chromadb.Client()
collection = client.create_collection(name="my_pdf", embedding_function=embedding_fn)

# ---- Step 4: Load, chunk, and store the PDF ----
print("Reading and processing PDF...")
text = extract_text("document.pdf")
chunks = chunk_text(text)

collection.add(
    documents=chunks,
    ids=[f"chunk_{i}" for i in range(len(chunks))]
)
print(f"Stored {len(chunks)} chunks in the vector database.\n")

# ---- Step 5: Ask a question, retrieve relevant chunks ----
def ask(question, top_k=3):
    results = collection.query(query_texts=[question], n_results=top_k)
    retrieved_chunks = results['documents'][0]

    context = "\n\n".join(retrieved_chunks)

    system_prompt = """You are a helpful assistant that answers questions based only on the given context.
If the answer is not in the context, say "I don't have that information in the document."
Do not use outside knowledge."""

    response = ollama.generate(
        model='llama3.2',
        system=system_prompt,
        prompt=f"Context:\n{context}\n\nQuestion: {question}"
    )
    return response['response']

# ---- Step 6: Interactive loop ----
print("Ask questions about your PDF (type 'exit' to quit)\n")
while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    answer = ask(question)
    print(f"\nAI: {answer}\n")