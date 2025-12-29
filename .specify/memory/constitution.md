# Project Constitution

This document serves as the supreme law of the codebase. All agents and developers must adhere to these principles, standards, and workflows.

## I. Core Philosophy: Spec-Driven Development (SDD)

We believe that **writing code is the easy part; understanding what to build is the hard part.** Therefore, we prioritize clear specifications over immediate implementation.

## II. Workflow Specifications

We adhere to a strict document-driven workflow. Each phase produces a specific artifact with mandatory components.

### 1. Specification Phase (`sp.specify`)
**Goal**: Define the *What* and *Why*.
**Artifact**: `specs/<feature>/spec.md`
**Mandatory Content**:
*   **Metadata**: Feature Branch, Status, Input Prompt.
*   **User Scenarios & Testing**:
    *   **User Stories**: Must be prioritized (P1, P2, P3).
    *   **Independent Test**: How to verify the story in isolation.
    *   **Acceptance Scenarios**: Given/When/Then format.
    *   **Edge Cases**: Error handling, boundaries, and negative tests.
*   **Requirements**:
    *   **Functional Requirements (FR-xxx)**: "System MUST..." statements. Testable.
    *   **Key Entities**: Data objects or core concepts involved.
*   **Success Criteria**:
    *   **Measurable Outcomes (SC-xxx)**: Quantitative (latency, count) or qualitative (user success) metrics.

### 2. Planning Phase (`sp.plan`)
**Goal**: Define the *How*.
**Artifact**: `specs/<feature>/plan.md`
**Mandatory Content**:
*   **Technical Context**:
    *   **Constraints**: Hard limits (tech stack, budget, legacy).
    *   **Unknowns**: Risks or things to research.
*   **Constitution Check**: Validation against project principles.
*   **Phase 0: Research**:
    *   **Decisions**: "We chose X because Y."
    *   **Alternatives**: "We considered Z but rejected it because..."
*   **Phase 1: Design**:
    *   **Data Models**: Schemas, fields, relationships.
    *   **API Contracts**: Endpoints, inputs, outputs.
*   **Phase 2: Implementation Steps**: High-level strategy (MVP first).

### 3. Tasking Phase (`sp.tasks`)
**Goal**: Break down into atomic actions.
**Artifact**: `specs/<feature>/tasks.md`
**Mandatory Content**:
*   **Phases**:
    *   **Phase 1: Setup**: Infrastructure & boilerplate.
    *   **Phase 2: Foundational**: Blocking prerequisites.
    *   **Phase 3+: User Stories**: Organized by Priority (P1, P2...).
*   **Task Format**:
    *   `[ ] Txxx [P] [Story] Description`
    *   **[P]**: Parallelizable.
    *   **[Story]**: US1, US2, etc.
*   **Dependencies**: Explicit execution order and blockers.

## III. Technical Standards

### Tech Stack
- **Documentation/Frontend**: Docusaurus (React, TypeScript/JavaScript).
- **Backend/Scripts**: Python (preferred for data/robotics), Node.js (for web tooling).
- **Styling**: CSS Modules or standard CSS.

### Code Quality
- **Readability**: Code is read more often than written. Optimize for clarity.
- **Comments**: Explain *Why*, not *What*. Use docstrings for functions/classes.
- **Naming**: Verbose and descriptive. `calculateTrajectory()` > `calcTraj()`.
- **DRY (Don't Repeat Yourself)**: Extract common logic, but prefer duplication over wrong abstraction.

## IV. Quality Assurance

- **Testing**:
    *   **Critical Paths**: Must have automated tests (Unit/Integration).
    *   **UI/Docs**: Manual verification scenarios are acceptable.
- **Review**: All code changes must be reviewed against the `tasks.md` checklist.
- **Refactoring**: Leave the campsite cleaner than you found it.

## V. Documentation

- **Single Source of Truth**: The `docs/` folder is the product.
- **Live Specs**: Specifications (`specs/`) are living documents. If requirements change, update the Spec first.
- **ADRs**: Architecturally significant decisions must be recorded in `history/adr/`.