from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
import sys

# Add current directory to sys.path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rag_core import RAGSystem

app = FastAPI(title="Humanoid Robotics API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for hackathon/dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global RAG instance
rag: Optional[RAGSystem] = None

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[dict]

@app.on_event("startup")
async def startup_event():
    global rag
    docs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))
    rag = RAGSystem(docs_path)

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not rag:
        raise HTTPException(status_code=500, detail="RAG system not initialized")
    
    results = rag.search(request.query)
    
    # Simple formatting of the answer based on retrieved context
    # In a full system, this context would be passed to an LLM.
    if not results:
        answer = "I couldn't find any information about that in the book."
    else:
        answer = f"Based on the book, here is what I found about '{request.query}':\n\n"
        for i, res in enumerate(results):
            answer += f"- {res['text']} (Source: {res['source']})\n\n"
            
    return ChatResponse(answer=answer, sources=results)

@app.get("/health")
async def health():
    return {"status": "ok"}