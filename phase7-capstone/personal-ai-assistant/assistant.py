import chromadb
from chromadb.utils import embedding_functions
from pypdf import PdfReader
from ddgs import DDGS
import ollama

# ---- RAG SETUP (from Phase 3) ----
def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)
client = chromadb.Client()
collection = client.create_collection(name="documents", embedding_function=embedding_fn)

print("Loading document into vector database...")
text = extract_text("document.pdf")
chunks = chunk_text(text)
collection.add(documents=chunks, ids=[f"chunk_{i}" for i in range(len(chunks))])
print(f"Loaded {len(chunks)} chunks.\n")



# ---- WEB SEARCH TOOL (from Phase 4) ----
def search_web(query, max_results=3):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(f"Title: {r['title']}\nSnippet: {r['body']}")
    return "\n\n".join(results)

# ---- ROUTER: decide which capability to use ----
def route_question(question):
    router_prompt = f"""You are a router that decides how to answer a question.
Respond with ONLY ONE WORD - either "DOCUMENT" or "WEB".

Use "DOCUMENT" if the question is about company policies, work hours, leave, 
remote work, expenses, referrals, or anything that sounds like it belongs 
in an employee handbook.

Use "WEB" if the question needs current/real-time information, like news, 
weather, recent events, or anything not related to company policies.

Question: {question}

Answer with only one word: DOCUMENT or WEB"""

    response = ollama.generate(model='llama3.2', prompt=router_prompt)
    decision = response['response'].strip().upper()
    
    if "DOCUMENT" in decision:
        return "DOCUMENT"
    else:
        return "WEB"

# ---- PATH 1: Answer from document (RAG) ----
def answer_from_document(question, top_k=3):
    results = collection.query(query_texts=[question], n_results=top_k)
    context = "\n\n".join(results['documents'][0])
    
    system_prompt = """You are a helpful assistant answering from a company document.
Only use the given context. If the answer isn't in the context, say so."""
    
    response = ollama.generate(
        model='llama3.2',
        system=system_prompt,
        prompt=f"Context:\n{context}\n\nQuestion: {question}"
    )
    return response['response']

# ---- PATH 2: Answer using web search (Agent) ----
def answer_from_web(question):
    search_results = search_web(question)
    
    system_prompt = """You are a helpful research assistant.
Answer the question using only the search results given to you."""
    
    response = ollama.generate(
        model='llama3.2',
        system=system_prompt,
        prompt=f"Search Results:\n{search_results}\n\nQuestion: {question}"
    )
    return response['response']

# ---- MAIN ASSISTANT LOOP ----
print("Personal AI Assistant ready! Ask me anything (type 'exit' to quit)\n")

while True:
    question = input("You: ")
    if question.lower() == "exit":
        break
    
    decision = route_question(question)
    print(f"[Router decided: {decision}]")
    
    if decision == "DOCUMENT":
        answer = answer_from_document(question)
    else:
        answer = answer_from_web(question)
    
    print(f"\nAI: {answer}\n")