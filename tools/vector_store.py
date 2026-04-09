from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStoreTool:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.model = SentenceTransformer('all-MiniLM-L6-v2')
            cls.index = None
            cls.chunks = []
        return cls._instance

    def build_index(self, text):
        # Split text into chunks
        self.chunks = [text[i:i+500] for i in range(0, len(text), 500)]
        embeddings = self.model.encode(self.chunks)
        
        # Create FAISS Index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings).astype('float32'))

    def search(self, query, k=3):
        query_vector = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vector).astype('float32'), k)
        return [self.chunks[i] for i in indices[0]]