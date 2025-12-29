# Tasks: AI Robotics Structure

**Input**: Design documents from `/specs/003-ai-robotics-structure/`
**Prerequisites**: plan.md, spec.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

## Phase 1: Setup

- [ ] T001 Create directory `docs/ai-robotics/`

## Phase 2: Foundational (Content Migration & Creation)

- [ ] T002 [P] [US1] Create `docs/ai-robotics/intro.md` with overview and case studies from `docs/04-ai-ml.md`
- [ ] T003 [P] [US1] Create `docs/ai-robotics/ml-basics.md` with ML basics and migrated RL/Sim2Real content
- [ ] T004 [P] [US1] Create `docs/ai-robotics/vision.md` with CNNs and migrated VLM content
- [ ] T005 [P] [US1] Create `docs/ai-robotics/navigation.md` with SLAM and Path Planning content

## Phase 3: Integration & Cleanup

- [ ] T006 Update `sidebars.js` to include the new `ai-robotics` category and its files
- [ ] T007 Remove `docs/04-ai-ml.md` after verifying all content is migrated
- [ ] T008 Verify site build with `npm run build`

## Dependencies & Execution Order

- **Phase 1**: Must complete before Phase 2.
- **Phase 2**: Files can be created in parallel.
- **Phase 3**: Depends on Phase 2 completion.
