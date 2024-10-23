import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def load_embeddings(file_path):
    return np.load(file_path)

def query_embedding(query, model):
    return model.encode(query)

def compute_similarity(query_embedding, document_embeddings):
    return cosine_similarity([query_embedding], document_embeddings)

def main():
    # Load precomputed document embeddings
    embeddings_file = 'data/document_embeddings.npy'
    document_embeddings = load_embeddings(embeddings_file)
    
    # Load SBERT model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    
    while True:
        # Accept user query
        query = input("Enter your query: ")
        if query.lower() == 'exit':
            break
        
        # Encode the query
        query_emb = query_embedding(query, model)
        
        # Compute similarity between the query and document embeddings
        similarity_scores = compute_similarity(query_emb, document_embeddings)
        
        # Retrieve and display the most relevant document(s)
        top_n = 3  # You can adjust this to retrieve more documents
        top_n_indices = np.argsort(similarity_scores[0])[::-1][:top_n]
        
        print(f"Top {top_n} most relevant documents:")
        for idx in top_n_indices:
            print(f"Document {idx+1} with similarity score: {similarity_scores[0][idx]}")
        print("-" * 50)

if __name__ == "__main__":
    main()
