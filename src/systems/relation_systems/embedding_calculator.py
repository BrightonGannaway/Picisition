#TODO: uninstall sentance-transformers after testing 

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from gensim.models import KeyedVectors
from scipy.spatial.distance import cosine

class EmbeddingCalculator:
    def __init__(self, model_path="bin/glove_100d.kv"):
        self.model = KeyedVectors.load(model_path, mmap='r')
        print("Embedding model loaded successfully.")

    def calculate_similarity(self, word1, word2):
        for word in word1.split() + word2.split():
            if word not in self.model:
                raise ValueError(f"Word '{word}' not found in the embedding model.")
        
        vec1 = self.calculate_vector_average(word1.split())
        vec2 = self.calculate_vector_average(word2.split())

        similarity = 1 - cosine(vec1, vec2)
        return similarity

    def calculate_vector_average(self, words):
        vectors = [self.model[word] for word in words if word in self.model]
        average_vector = sum(vectors) / len(vectors)
        return average_vector

    @staticmethod
    def similarity_to_percentage(similarity):
        if not (-1 <= similarity <= 1):
            raise ValueError("Cosine similarity must be between -1 and 1.")
        return similarity * 100





