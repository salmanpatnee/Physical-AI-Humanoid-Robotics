# Implementation Tasks: Chatbot-Docusaurus Integration

## Feature Overview
- **Feature**: Chatbot-Docusaurus Integration
- **Branch**: `001-chatbot-docusaurus-integration`
- **Spec**: [spec.md](spec.md)
- **Plan**: [plan.md](plan.md)
- **Input**: Implementation plan and feature specification

## Implementation Strategy
This implementation follows a user story-driven approach to deliver the chatbot integration in priority order. The backend infrastructure already exists, so we'll focus on integrating with it. We'll start with the core frontend functionality (user story 1 - the chat widget) to create an MVP, then add the ability to ask questions with selected text context (user story 2), and finally enable response display with sources (user story 3).

The MVP scope is defined by User Story 1, which will deliver a functional chat widget that appears in the book UI, allowing for early user feedback and validation.

## Dependencies
- User Story 1 (Access Chat Widget) must be completed before User Stories 2 and 3 can be fully tested
- Foundational tasks (models, services, API schemas) must be completed before user story tasks
- Backend API infrastructure exists and is available before frontend implementation is complete

## Parallel Execution Examples
- Model creation tasks (T005-T007) can run in parallel
- UI component and CSS creation (T011-T012) can run in parallel
- API endpoint development and UI response handling (T017, T021-T022) can run in parallel

---

## Phase 1: Setup Tasks

**Goal**: Set up project structure and foundational elements

- [X] T001 Verify existing backend directory structure (backend/src/models, backend/src/services, backend/src/api)
- [X] T002 Create frontend directory structure (frontend/src/components, frontend/src/services)
- [X] T003 Verify existing FastAPI project with proper dependencies in backend directory
- [X] T004 Set up environment configuration for backend API

---

## Phase 2: Foundational Tasks

**Goal**: Create or update core models, services and APIs that will be used by all user stories

- [X] T005 [P] Create or update UserQuery model in backend/src/models/user_query.py based on API contract
- [X] T006 [P] Create or update ChatResponse model in backend/src/models/chat_response.py based on API contract
- [X] T007 [P] Create or update SourceReference model in backend/src/models/source_reference.py based on API contract
- [X] T008 Create or update API endpoint schema in backend/src/api/schemas.py
- [X] T009 [P] Create or update ChatService interface in backend/src/services/chat_service.py
- [X] T010 Create frontend service for API communication in frontend/src/services/chatAPI.js

---

## Phase 3: User Story 1 - Access Chat Widget

**Goal**: Enable users to see a chat widget in the book UI to ask questions about content

**Independent Test Criteria**:
- Chat widget appears consistently on all book pages
- Widget is accessible to users without disrupting the reading experience
- Widget can be toggled open/closed

**User Story**: As an end user reading the book, I want to see a chat widget appear in the book UI so I can ask questions about the content I am reading.

- [X] T011 [P] [US1] Create ChatWidget React component in frontend/src/components/ChatWidget/ChatWidget.jsx
- [X] T012 [P] [US1] Create ChatWidget CSS styles in frontend/src/components/ChatWidget/ChatWidget.css
- [X] T013 [US1] Implement widget toggle functionality in ChatWidget component
- [X] T014 [US1] Add ChatWidget to Docusaurus layout in src/theme/Root.js
- [X] T015 [US1] Test that chat widget appears consistently on all book pages

---

## Phase 4: User Story 2 - Ask Questions with Selected Text Context

**Goal**: Enable users to ask questions and optionally provide selected text for context

**Independent Test Criteria**:
- User can select text on a page
- When asking a question, selected text is passed along with the question to the backend API
- If no text is selected, only the question is sent

**User Story**: As an end user reading the book, I want to ask questions about the content and optionally specify selected text that the answers should be restricted to, so I can get more relevant responses.

- [X] T016 [P] [US2] Implement text selection capture functionality in ChatWidget component
- [X] T017 [US2] Create or update API endpoint for chat queries in backend/src/api/chat_endpoint.py
- [X] T018 [US2] Implement or update query processing service in backend/src/services/query_service.py
- [X] T019 [US2] Update ChatWidget to send selected text with queries
- [X] T020 [US2] Test that selected text is passed along with user questions to backend

---

## Phase 5: User Story 3 - Receive and View Responses

**Goal**: Display chatbot responses with sources clearly to the user

**Independent Test Criteria**:
- Responses are displayed in the chat widget appropriately
- Sources are clearly distinguishable from the answer
- User can understand the basis for the responses

**User Story**: As an end user, I want to receive answers to my questions that are displayed clearly along with their sources, so I can understand the basis for the responses.

- [X] T021 [P] [US3] Update ChatWidget to display responses from backend
- [X] T022 [P] [US3] Implement source reference display in ChatWidget
- [X] T023 [US3] Style response and source elements in ChatWidget.css
- [X] T024 [US3] Test that answers and sources are displayed correctly in the chat widget
- [X] T025 [US3] Implement error handling for API failures in ChatWidget

---

## Phase 6: Polish & Cross-Cutting Concerns

**Goal**: Add finishing touches and handle edge cases

- [X] T026 Add loading indicators during API requests in ChatWidget
- [X] T027 Implement proper error handling for edge cases (no sources, API failures)
- [X] T028 Add analytics tracking for chat interactions (optional)
- [X] T029 Update documentation with usage instructions
- [X] T030 Perform final integration testing of complete flow