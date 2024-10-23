from sentence_transformers import SentenceTransformer
import os
import numpy as np



def load_processed_text(path):
    with open(path, 'r') as file:
        return file.read()
    
def save_embeddings(embeddings, out_path):
    np.save(out_path, embeddings)
    print(f"Embeddings saved to {out_path}")

def vectorize_text(text):
    return model.encode([text])

if __name__ == "__main__":
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    
    processed_file = 'data/processed_text.txt'
    processed_text = load_processed_text(processed_file)

    doc_embedding = vectorize_text(processed_text)
    output_file = 'data/embeddings.npy'
    save_embeddings(doc_embedding, output_file)

    print('doc embedding saved')