import os
import glob
import re
from typing import List, Dict
import math
from collections import Counter

class RAGSystem:
    def __init__(self, docs_dir: str):
        self.docs_dir = docs_dir
        self.documents = []  # List of {text, source, tokens}
        self._ingest_docs()

    def _tokenize(self, text: str) -> List[str]:
        # Simple regex tokenizer: lowercase and keep only alphanumeric
        return re.findall(r'\b\w+\b', text.lower())

    def _ingest_docs(self):
        print(f"Ingesting docs from {self.docs_dir}...")
        md_files = glob.glob(os.path.join(self.docs_dir, "*.md"))
        
        all_chunks = []
        for file_path in md_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Chunk by double newline (paragraphs)
                    raw_chunks = [c.strip() for c in content.split("\n\n") if c.strip()]
                    
                    filename = os.path.basename(file_path)
                    for chunk in raw_chunks:
                        if len(chunk) < 20: # Skip very short chunks
                            continue
                        all_chunks.append({
                            "text": chunk,
                            "source": filename,
                            "tokens": set(self._tokenize(chunk))
                        })
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
        
        self.documents = all_chunks
        print(f"Ingestion complete. {len(self.documents)} chunks indexed.")

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        if not self.documents:
            return []

        query_tokens = set(self._tokenize(query))
        if not query_tokens:
            return []

        scored_docs = []
        for doc in self.documents:
            # Jaccard similarity-ish (Intersection count)
            # We prioritize chunks that contain more of the query words
            intersection = query_tokens.intersection(doc["tokens"])
            score = len(intersection)
            
            if score > 0:
                scored_docs.append({
                    "text": doc["text"],
                    "source": doc["source"],
                    "score": score
                })
        
        # Sort by score desc
        scored_docs.sort(key=lambda x: x["score"], reverse=True)
        
        return scored_docs[:top_k]

if __name__ == "__main__":
    # Simple test
    # Resolve path relative to this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    docs_path = os.path.join(base_dir, "..", "docs")
    
    rag = RAGSystem(docs_path)
    print("Searching for 'ASIMO'...")
    results = rag.search("Who created ASIMO?")
    for r in results:
        print(f"--- {r['source']} ({r['score']}) ---\n{r['text'][:100]}...")