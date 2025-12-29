# Tasks: Humanoid Robotics Platform

## Content
- [x] **Task 1**: Refactor `docs/` structure.
  - Create `docs/01-introduction.md`
  - Create `docs/02-history.md`
  - Create `docs/03-components.md`
  - Create `docs/04-ai-ml.md`
  - Create `docs/05-sota.md`
  - Create `docs/06-applications.md`
  - Create `docs/07-ethics.md`
  - Move content from `docs/physical-ai-and-humanoids.md` to these files.
  - Delete `docs/physical-ai-and-humanoids.md`.

## Backend (Python)
- [x] **Task 2**: Setup Python Environment.
  - Create `backend/requirements.txt` with: `fastapi`, `uvicorn`, `python-multipart`.
  - Create `backend/__init__.py`.
- [x] **Task 3**: Implement RAG Core (`backend/rag_core.py`).
  - Class `RAGSystem` that loads MD files, chunks them, and performs search.
- [x] **Task 4**: Implement API (`backend/main.py`).
  - `POST /chat` endpoint calling `RAGSystem`.

## Frontend (Docusaurus)
- [x] **Task 5**: Create Chat Widget.
  - `src/components/ChatWidget/index.js` (React component).
  - `src/components/ChatWidget/styles.module.css`.
- [x] **Task 6**: Register Component.
  - Update `src/pages/index.js` or `docusaurus.config.js` to include the chat capability (or just add it to the Homepage).

## Verification
- [x] **Task 7**: Run verification.
  - `python backend/rag_core.py` (Verified).