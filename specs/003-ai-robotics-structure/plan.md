# Implementation Plan - AI Robotics Structure

**Feature**: AI Robotics Chapter Restructure
**Status**: Draft

## Technical Context

**Constraints**:
- Must use Docusaurus Markdown.
- Must preserve existing content.
- Must be a single file or a subdirectory (user implied "Chapter", currently it's a file `04-ai-ml.md`).
- **Decision**: Keep as single file `04-ai-ml.md` for now, but use clear H2/H3 headers. If it gets too long, we can split later.

**Unknowns**:
- None.

## Constitution Check

- **Architecture**: N/A (Documentation)
- **Code Quality**: N/A
- **Security**: N/A
- **Testing**: Verify build.

## Phase 0: Research

**Goal**: N/A - Requirement is structural.

## Phase 1: Design & Contracts

**Goal**: Define the structure of the markdown file.

### Data Model
- **Directory**: `docs/ai-robotics/`
- **Files**:
    - `docs/ai-robotics/intro.md`: Overview and Case Studies.
    - `docs/ai-robotics/ml-basics.md`: ML, RL, Sim2Real.
    - `docs/ai-robotics/vision.md`: CNNs, Detection, VLMs.
    - `docs/ai-robotics/navigation.md`: SLAM, Planning.

## Phase 2: Implementation

**Goal**: Create new files and migrate content.

### Steps
1.  **Create** `docs/ai-robotics/` directory.
2.  **Migrate** content from `docs/04-ai-ml.md` to the new files.
3.  **Add** new foundational content (SLAM, CNNs basics) to the respective files.
4.  **Update** `sidebars.js`.
5.  **Delete** `docs/04-ai-ml.md`.
6.  **Verify** build.