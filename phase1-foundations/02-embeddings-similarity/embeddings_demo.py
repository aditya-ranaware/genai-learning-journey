from sentence_transformers import SentenceTransformer
import numpy as np

# Free, local embedding model — downloads once, then runs offline
model = SentenceTransformer('all-MiniLM-L6-v2')

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Words to test
words = ["king", "queen", "man", "woman", "car"]
embeddings = {word: model.encode(word) for word in words}

# Show similarity between pairs
print("\n--- Similarity Scores ---")
pairs = [("king", "queen"), ("king", "car"), ("man", "woman"), ("queen", "car")]
for w1, w2 in pairs:
    sim = cosine_similarity(embeddings[w1], embeddings[w2])
    print(f"{w1} <-> {w2}: {sim:.4f}")

# The famous vector math: king - man + woman ≈ queen
result_vector = embeddings["king"] - embeddings["man"] + embeddings["woman"]
similarity_to_queen = cosine_similarity(result_vector, embeddings["queen"])
print(f"\n(king - man + woman) <-> queen similarity: {similarity_to_queen:.4f}")