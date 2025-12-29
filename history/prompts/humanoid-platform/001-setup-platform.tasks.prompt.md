---
id: 001
title: Setup Humanoid Platform and RAG
stage: tasks
date: 2025-12-29
surface: agent
model: gemini-2.0-flash-exp
feature: humanoid-platform
branch: main
user: user
command: sp.tasks
labels: ["cleanup", "python", "rag", "docusaurus"]
links: 
  - specs/001-humanoid-platform/spec.md
  - specs/001-humanoid-platform/plan.md
  - specs/001-humanoid-platform/tasks.md
files_yaml:
  - .specify/memory/constitution.md
  - specs/001-humanoid-platform/spec.md
  - specs/001-humanoid-platform/plan.md
  - specs/001-humanoid-platform/tasks.md
  - backend/rag_core.py
  - backend/main.py
  - backend/requirements.txt
  - src/components/ChatWidget/index.js
  - src/components/ChatWidget/styles.module.css
  - src/theme/Root.js
  - docusaurus.config.js
  - src/pages/index.js
tests_yaml:
  - backend/rag_core.py (manual verification)
---

# User Input
delete extra files jou extra bngy hou constition.md update krou mere usm complete detaling mentioned krou is book ki by using the sp. specify , sp.plan, sp.sp.task made compleete project correctly and remove vibe coding completely used [ython only yh sare updates krk project dou

# Response
I have cleaned up the project, removing "vibe coding" artifacts (`.claude`, `temp-site`) and updating the Constitution to enforce Spec-Driven Development and Python-first tooling.

I have executed the `sp.specify` -> `sp.plan` -> `sp.tasks` workflow to define and build the "Humanoid Robotics Platform":
1.  **Refactored Content**: Split the "Physical AI" overview into 7 distinct chapters in `docs/` for the "Book".
2.  **Backend (Python Only)**: Implemented a lightweight, pure-Python RAG system (`backend/rag_core.py`) and FastAPI server (`backend/main.py`). It uses a dependency-free keyword/token overlap search to respect environment constraints.
3.  **Frontend**: Added a React `ChatWidget` to the Docusaurus site (`src/components/ChatWidget`) that connects to the Python backend.
4.  **Verification**: Verified the RAG system indexes the content and retrieves "ASIMO" correctly.

The project is now a complete, functioning documentation platform with an integrated AI assistant.
