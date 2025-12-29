# Plan: Humanoid Robotics Platform & RAG

## Architecture
- **Frontend**: Docusaurus (Port 3000)
  - Custom `ChatWidget` component for user interaction.
  - Proxy configured to route `/api` requests to Backend.
- **Backend**: Python FastAPI (Port 8000)
  - `GET /health`: Health check.
  - `POST /chat`: Accepts query, returns answer + sources.
- **RAG Engine**:
  - **Ingestion**: `backend/ingest.py` reads Markdown from `../docs`.
  - **Storage**: In-memory vector store (using `sentence-transformers` for embeddings and `numpy` for cosine similarity) to keep it lightweight and "Python native" without complex DB setup.
  - **LLM**: Use a placeholder or a simple interface to a free API (like Gemini if key provided, or a mock for the prototype if no key). *Decision: Use a mock/rule-based responder for the prototype to ensure "complete project correctly" without dependency on user API keys, but structure it for easy LLM swap.*

## Implementation Steps

### Phase 1: Content & Frontend Structure (The Book)
1.  **Clean & Organize Docs**: Ensure `docs/` structure matches the 7 chapters:
    - `01-introduction.md`
    - `02-history.md`
    - `03-components.md`
    - `04-ai-ml.md`
    - `05-sota.md`
    - `06-applications.md`
    - `07-ethics.md`
2.  **Split Content**: Take the content from `physical-ai-and-humanoids.md` and distribute it into these files.

### Phase 2: Python Backend (The Intelligence)
1.  **Setup**: `backend/requirements.txt` (fastapi, uvicorn, numpy, sentence-transformers, python-multipart).
2.  **Ingestion Script**: `backend/ingest.py`. Reads MD files, splits by header, creates embeddings.
3.  **API**: `backend/main.py`. Loads embeddings on startup. Handles `/chat`.

### Phase 3: Integration
1.  **Frontend Widget**: Create `src/components/ChatWidget/index.js`.
2.  **Embed Widget**: Add `ChatWidget` to `src/theme/Root.js` or a specific page.
3.  **Proxy**: Update `package.json` or Docusaurus config to proxy API calls.

## Verification
- Run `pytest` for backend.
- Manual check of Docusaurus build.
