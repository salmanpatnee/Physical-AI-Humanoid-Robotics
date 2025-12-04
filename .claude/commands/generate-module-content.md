---
description: Generate complete educational module content from source materials (PDF, docs) with proper MDX formatting and validation
---

## User Input

```text
$ARGUMENTS
```

Expected format: `--feature <feature-id> --source <pdf-path> [--module-number <num>] [--module-name <name>]`

Example: `--feature 005-module2-simulation --source doc/textbook.pdf --module-number 2 --module-name "The Digital Twin"`

## Outline

### 1. Parse Arguments and Validate

Parse the user input to extract:
- `--feature <feature-id>`: Feature directory (e.g., `004-module1-ros2`)
- `--source <pdf-path>`: Path to source material (PDF or documentation)
- `--module-number <num>` (optional): Module number for directory naming
- `--module-name <name>` (optional): Display name for the module

**Validation**:
- Verify feature directory exists: `specs/<feature-id>/`
- Verify source file exists at provided path
- Check for required files: `spec.md`, `tasks.md` in feature directory

If validation fails, report missing items and stop.

### 2. Load Specification and Tasks

Read the following files from `specs/<feature-id>/`:
- **spec.md**: Feature specification with module details
- **tasks.md**: Task breakdown and acceptance criteria
- **plan.md** (if exists): Architecture and technical decisions

Extract from spec.md:
- Module overview and learning objectives
- Chapter list with titles and topics
- Required MDX components
- Frontmatter schema requirements

### 3. Extract Source Material Content

**CRITICAL**: Follow Anti-Hallucination Mandate - only use content from source material.

Read the source PDF/document and:
1. Identify the relevant section for this module
2. Extract:
   - Key concepts and definitions
   - Code examples and technical details
   - Learning objectives and prerequisites
   - Real-world applications and use cases
3. Map extracted content to chapter requirements from spec.md

**Verification**: Confirm that each chapter has sufficient source material. If any chapter lacks content, report it and ask for additional sources or clarification.

### 4. Determine Module Directory Structure

Based on arguments and spec:
- Module directory name: `module<number>-<slug>`
  - Example: `module1-robotic-nervous-system`
- Full path: `docs/module<number>-<slug>/`
- Chapter files: `docs/module<number>-<slug>/0X-<chapter-slug>.mdx`

**Check if directory exists**:
- If exists: Ask user if they want to overwrite or skip
- If not exists: Create directory structure

### 5. Generate Module Configuration

Create `docs/module<number>-<slug>/_category_.json`:

```json
{
  "label": "Module <number>: <Module Name>",
  "position": <number + 1>,
  "link": {
    "type": "generated-index",
    "description": "<Brief module description from spec>"
  }
}
```

**Example**:
```json
{
  "label": "Module 1: The Robotic Nervous System",
  "position": 2,
  "link": {
    "type": "generated-index",
    "description": "Learn about ROS 2, the middleware that acts as the nervous system for modern robots. This module covers nodes, topics, services, URDF modeling, and launch files."
  }
}
```

### 6. Generate Chapter Content

For each chapter in the spec (typically 5 chapters per module):

#### 6.1 Create Frontmatter
Generate valid YAML frontmatter:

```yaml
---
title: "<Chapter Number>. <Chapter Title>"
sidebar_position: <number>
chapter_type: "concept" | "tutorial" | "reference" | "case-study"
learning_goals:
  - "<Specific learning objective 1>"
  - "<Specific learning objective 2>"
  - "<Specific learning objective 3>"
prerequisites:
  - "<Required knowledge>"
  - "<Technology familiarity>"
key_takeaways:
  - "<Core concept learned>"
  - "<Practical application>"
  - "<Connection to broader context>"
---
```

**Determine chapter_type**:
- `concept`: Introduces ideas, theory, architecture
- `tutorial`: Step-by-step hands-on implementation
- `reference`: Technical reference, API documentation
- `case-study`: Real-world applications and examples

#### 6.2 Generate Chapter Body

Structure each chapter as follows:

```markdown
# <Chapter Title>

## Introduction
<Context and motivation - why this topic matters, 2-3 paragraphs>

<LearningGoals>
- <Goal 1>
- <Goal 2>
- <Goal 3>
</LearningGoals>

<Prerequisites>
- <Prerequisite 1>
- <Prerequisite 2>
</Prerequisites>

## <Core Section 1>
<Conceptual explanation with examples>

### Code Example: <Example Title>
```<language>
// Well-commented, runnable code example
// extracted from source material
```

<Explanation of code example>

## <Core Section 2>
<Additional concepts and examples>

## <Core Section 3>
<Advanced topics or applications>

<KeyTakeaways>
- <Key takeaway 1>
- <Key takeaway 2>
- <Key takeaway 3>
</KeyTakeaways>

## Practical Exercise

<ExerciseBlock
  question="<Problem statement that tests understanding>"
  hints={[
    { title: "Hint 1", content: "<First hint - general direction>" },
    { title: "Hint 2", content: "<Second hint - more specific>" },
    { title: "Hint 3", content: "<Third hint - near solution>" }
  ]}
  solution={
    <div>
      <p><strong>Solution:</strong></p>
      <pre>{`
<Complete solution code>
      `}</pre>
      <p><strong>Key Design Choices:</strong></p>
      <ul>
        <li><Explanation of choice 1></li>
        <li><Explanation of choice 2></li>
      </ul>
    </div>
  }
/>

## Next Steps
<Bridge to next chapter or module>
```

**Content Requirements**:
- 2,500-4,000 words per chapter
- 3-5 code examples per chapter
- 1-2 exercises per chapter
- Clear section headers and logical flow
- Technical terms explained on first use

#### 6.3 Validate Chapter Content

For each generated chapter:
- [ ] Frontmatter validates against schema (if schema exists)
- [ ] All MDX components have correct syntax
- [ ] Code examples are complete and syntactically correct
- [ ] Exercises include question, hints, and solution
- [ ] Learning goals match content coverage
- [ ] No placeholder text (TODO, FIXME, etc.)
- [ ] All content sourced from provided materials

### 7. Update Sidebar Configuration

Read `sidebars.ts` and check if module is already included.

**If not included**, add module entry:

```typescript
{
  type: 'autogenerated',
  dirName: 'module<number>-<slug>',
},
```

Insert in the correct position in the `bookSidebar` array (typically after Introduction, before existing modules).

**Example insertion**:
```typescript
const sidebars: SidebarsConfig = {
  bookSidebar: [
    'intro',
    {
      type: 'category',
      label: '1. Introduction',
      // ...
    },
    {
      type: 'autogenerated',
      dirName: 'module1-robotic-nervous-system',
    },
    {
      type: 'category',
      label: '2. Core Modules',
      // ...
    },
    // ...
  ],
};
```

### 8. Validate Build

Run build validation:

```bash
npm run build
```

**Monitor for**:
- Frontmatter validation errors
- MDX syntax errors
- Component rendering errors
- Missing dependencies

**If build fails**:
1. Read error output
2. Identify problematic file/line
3. Fix the issue (frontmatter, MDX syntax, component usage)
4. Re-run build
5. Repeat until build passes

**Build must pass** before marking content generation complete.

### 9. Update Task Tracking

Read `specs/<feature-id>/tasks.md` and mark completed tasks:

For each completed task:
- Change `- [ ]` to `- [X]`
- Verify all tasks in the implementation phases are marked

Example:
```markdown
- [X] T001 Create the directory `docs/module1-robotic-nervous-system/`
- [X] T002 [P] Create the file `docs/module1-robotic-nervous-system/_category_.json`
- [X] T009 [P] [US1] Write content for chapter 01-focus-middleware-for-robot-control.mdx
```

### 10. Generate Summary Report

Create a summary of completed work:

```markdown
## Module Content Generation Complete ✅

**Module**: Module <number> - <Module Name>
**Feature**: <feature-id>
**Source Material**: <source-path>

### Files Created
- `docs/module<number>-<slug>/_category_.json` - Module configuration
- `docs/module<number>-<slug>/01-<chapter1-slug>.mdx` - Chapter 1: <title>
- `docs/module<number>-<slug>/02-<chapter2-slug>.mdx` - Chapter 2: <title>
- `docs/module<number>-<slug>/03-<chapter3-slug>.mdx` - Chapter 3: <title>
- `docs/module<number>-<slug>/04-<chapter4-slug>.mdx` - Chapter 4: <title>
- `docs/module<number>-<slug>/05-<chapter5-slug>.mdx` - Chapter 5: <title>

### Files Modified
- `sidebars.ts` - Added module to bookSidebar
- `specs/<feature-id>/tasks.md` - Marked <count> tasks complete

### Validation Status
- ✅ Frontmatter schema: PASS
- ✅ MDX syntax: PASS
- ✅ Build validation: PASS (exit code 0)
- ✅ Content sourcing: All from provided materials

### Content Statistics
- Total chapters: <count>
- Total words: ~<word-count>
- Code examples: <count>
- Exercises: <count>

### Next Steps
1. Review generated content for accuracy
2. Test interactive components in browser
3. Optionally run content quality review
4. Proceed to next module or finalize feature
```

### 11. Create Prompt History Record (PHR)

**REQUIRED**: Create PHR as per constitutional mandate.

Follow the PHR creation process:
1. Read PHR template: `.specify/templates/phr-template.prompt.md`
2. Allocate next ID in sequence
3. Fill all placeholders:
   - Stage: `green` (implementation)
   - Feature: `<feature-id>`
   - Command: `/generate-module-content`
   - Files: List all created/modified files
   - Prompt: User's command with arguments
   - Response: Summary of generated content
4. Write to: `history/prompts/<feature-id>/<ID>-generate-module<number>-content.green.prompt.md`

## Error Handling

### Source Material Issues
- **Missing file**: Report error and stop
- **Insufficient content**: Report which chapters lack material, ask for additional sources
- **Extraction failure**: Report specific sections that couldn't be processed

### Build Failures
- **Frontmatter errors**: Show validation errors, fix syntax
- **MDX syntax errors**: Identify line/file, correct syntax
- **Component errors**: Check component props and usage
- **Missing dependencies**: Report and suggest fixes

### Task Tracking Issues
- **tasks.md not found**: Warning, but continue
- **Cannot parse tasks**: Warning, manual verification needed

## Quality Gates

Content generation cannot complete until:
1. ✅ All chapter files created with valid frontmatter
2. ✅ All MDX components render correctly
3. ✅ Build passes without errors (exit code 0)
4. ✅ Sidebar configuration updated correctly
5. ✅ All content sourced from provided materials (no hallucinations)
6. ✅ Task tracking updated
7. ✅ PHR created and saved

## Agent Context

This command uses the `educational-content-generator` agent for content generation tasks. The agent ensures:
- Pedagogical quality (learning progression, clarity)
- Technical accuracy (sourced from materials)
- Component compliance (proper MDX usage)
- Build validation (working Docusaurus site)

## Example Usage

### Basic Usage
```
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2
```

### With Custom Module Name
```
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2 --module-name "The Digital Twin"
```

### Multiple Source Files (comma-separated)
```
/generate-module-content --feature 006-module3-perception --source "doc/textbook.pdf,doc/perception-supplement.pdf" --module-number 3
```

## Success Message

Upon completion:

```
✅ Module <number> content generation complete!

Created <count> chapters with <word-count> words of educational content.
All chapters validated and building successfully.

View at: http://localhost:3000/docs/module<number>-<slug>

Next: Review content and proceed to next module or finalize feature.
```
