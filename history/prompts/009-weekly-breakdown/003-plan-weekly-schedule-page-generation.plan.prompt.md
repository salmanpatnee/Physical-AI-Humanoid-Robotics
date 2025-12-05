---
id: 003
title: Plan Weekly Schedule Page Generation
stage: plan
date: 2025-12-05
surface: agent
model: gemini-cli-agent
feature: 009-weekly-breakdown
branch: 009-weekly-breakdown
user: unknown
command: /sp.plan Create a high-level plan for generating the 13-week course breakdown by mapping each week’s learning goals, activities, and topics to the four modules of the “Teaching Physical AI & Humanoid Robotics Course.” The plan should outline the steps for extracting weekly content from the source PDF, organizing it into a clean Docusaurus MDX structure, assigning each week to the correct module, and presenting the timeline in a consistent format with frontmatter, learning objectives, and key milestones. Keep the plan short and sequential—extract weekly topics → map each to its module → generate MDX files → update sidebar → validate structure—ensuring the final output forms a clear, chronological learning path for students.
labels: ["plan", "docusaurus", "content-generation"]
links:
  spec: specs/009-weekly-breakdown/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/009-weekly-breakdown/plan.md
- specs/009-weekly-breakdown/research.md
- specs/009-weekly-breakdown/data-model.md
- specs/009-weekly-breakdown/quickstart.md
tests: []
---

## Prompt

```text
---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType gemini`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications
```

## Response snapshot

```text
The implementation plan for the "Weekly Course Schedule Page" has been created at `specs/009-weekly-breakdown/plan.md`.

Following the `/sp.plan` workflow, the following actions were taken:
1.  **Context Loaded**: The feature specification and project constitution were read.
2.  **Plan Generated**: The `plan.md` file was populated with a detailed summary, technical context, and a passed constitution check.
3.  **Artifacts Created**:
    *   `specs/009-weekly-breakdown/research.md`: Confirms that no new research is needed.
    *   `specs/009-weekly-breakdown/data-model.md`: Defines the content structure for the new page.
    *   `specs/009-weekly-breakdown/quickstart.md`: Provides steps for viewing the new page.

The plan is now ready for the next phase.
```

## Outcome

- ✅ Impact: A comprehensive implementation plan and supporting design artifacts were created, setting a clear path for the next phase.
- 🧪 Tests: No tests were run or added.
- 📁 Files: 4 files were created/modified.
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: The planning process was smooth due to a well-clarified specification. The agent successfully translated the spec and user request into a formal plan and its associated artifacts.

## Evaluation notes (flywheel)

- Failure modes observed: (none)
- Graders run and results (PASS/FAIL): (none)
- Prompt variant (if applicable): (none)
- Next experiment (smallest change to try): (none)
