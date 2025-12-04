# Custom Agents and Skills

This directory contains custom Claude Code agents and skills for the Physical AI & Humanoid Robotics project.

## Available Agents

### 📚 Educational Content Generator (`educational-content-generator.agent.md`)

**Purpose**: Specialized agent for creating educational content from source materials (PDFs, papers, documentation) and generating structured learning modules.

**Capabilities**:
- Extract content from source materials while maintaining fidelity (Anti-Hallucination Mandate)
- Generate chapter content with proper pedagogical structure
- Create interactive learning components (exercises, code examples, assessments)
- Ensure MDX/Docusaurus compliance and build validation
- Follow frontmatter schema requirements

**When to Use**:
- Creating new educational modules or tutorials
- Transforming technical documentation into course content
- Generating structured learning materials from research papers
- Building interactive coding tutorials with exercises

**Quality Standards**:
- All content must be sourced from provided materials
- Includes learning goals, prerequisites, and key takeaways
- Code examples must be complete and runnable
- Exercises include progressive hints and complete solutions
- Build validation required before completion

## Available Skills (Slash Commands)

### 🎓 Generate Module Content (`/generate-module-content`)

**Purpose**: End-to-end workflow for creating a complete educational module from specification to validated content.

**Usage**:
```bash
/generate-module-content --feature <feature-id> --source <pdf-path> [--module-number <num>] [--module-name <name>]
```

**Examples**:
```bash
# Basic usage - generate Module 2
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2

# With custom module name
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2 --module-name "The Digital Twin"

# Multiple source files
/generate-module-content --feature 006-module3-perception --source "doc/textbook.pdf,doc/perception-supplement.pdf" --module-number 3
```

**What It Does**:
1. ✅ Validates feature directory and source materials
2. ✅ Loads spec.md, tasks.md, and plan.md
3. ✅ Extracts relevant content from source PDF/docs
4. ✅ Generates module directory structure
5. ✅ Creates _category_.json configuration
6. ✅ Generates all chapter files with:
   - Valid frontmatter (title, learning_goals, prerequisites, key_takeaways)
   - MDX components (LearningGoals, Prerequisites, KeyTakeaways, ExerciseBlock)
   - Code examples with explanations
   - Practical exercises with hints and solutions
7. ✅ Updates sidebars.ts to include new module
8. ✅ Validates build (npm run build)
9. ✅ Updates task tracking (tasks.md)
10. ✅ Creates Prompt History Record (PHR)

**Output**:
- Module directory: `docs/module<N>-<slug>/`
- Configuration: `_category_.json`
- Chapters: `01-<chapter>.mdx` through `05-<chapter>.mdx`
- Updated: `sidebars.ts`, `tasks.md`
- PHR: `history/prompts/<feature>/###-generate-module-content.green.prompt.md`

**Prerequisites**:
- Feature directory exists: `specs/<feature-id>/`
- Required files: `spec.md`, `tasks.md`
- Source material available (PDF or documentation)
- Docusaurus project configured

**Success Criteria**:
- All chapters created with valid frontmatter
- Build passes (exit code 0)
- Sidebar includes new module
- All content sourced from materials (no hallucinations)
- Tasks marked complete

## How to Use

### Using the Agent Directly

The agent is invoked automatically when using the associated skills, but you can also reference it directly:

```
Claude, use the educational-content-generator agent to help me create Chapter 3 for Module 2.
```

### Using the Skill

Simply invoke the slash command with required arguments:

```
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2
```

## Workflow Example

Here's a complete workflow for creating a new module:

### Step 1: Create Feature Specification
```bash
/sp.specify
# Describe Module 2: The Digital Twin - Simulation
```

### Step 2: Create Implementation Plan
```bash
/sp.plan
# Review spec and create plan.md with architecture
```

### Step 3: Generate Tasks
```bash
/sp.tasks
# Create detailed task breakdown in tasks.md
```

### Step 4: Generate Module Content
```bash
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2 --module-name "The Digital Twin"
```

### Step 5: Review and Finalize
- Open http://localhost:3000/docs/module2-digital-twin
- Review generated content
- Make any manual adjustments if needed
- Commit and create PR

## Quality Standards

All generated content follows these standards:

### Frontmatter Requirements
- ✅ `title`: Clear, descriptive chapter title
- ✅ `sidebar_position`: Sequential numbering
- ✅ `chapter_type`: concept | tutorial | reference | case-study
- ✅ `learning_goals`: 3-5 specific, measurable objectives
- ✅ `prerequisites`: Required prior knowledge
- ✅ `key_takeaways`: 3-5 core concepts learned

### Content Requirements
- ✅ 2,500-4,000 words per chapter
- ✅ 3-5 runnable code examples per chapter
- ✅ 1-2 exercises with hints and solutions
- ✅ Clear section structure and logical flow
- ✅ All technical terms explained on first use
- ✅ All content sourced from provided materials

### Technical Requirements
- ✅ Valid MDX syntax
- ✅ Proper MDX component usage
- ✅ Frontmatter schema compliance
- ✅ Build validation passes
- ✅ No placeholder text (TODO, FIXME)

## Troubleshooting

### Build Failures

**Issue**: Frontmatter validation error
```
Error: Invalid frontmatter in file...
```
**Fix**: Check frontmatter YAML syntax, ensure all required fields present

**Issue**: MDX component error
```
Error: Unknown component: LearningGoals
```
**Fix**: Verify component is imported/available, check props syntax

### Content Issues

**Issue**: Insufficient source material
```
Warning: Chapter 3 has insufficient content from source
```
**Fix**: Provide additional source files or clarify chapter scope

**Issue**: Sidebar not updating
```
Module not appearing in sidebar
```
**Fix**: Check `sidebars.ts` syntax, restart dev server (npm start)

### Common Mistakes

❌ **Don't**: Run command without source material
✅ **Do**: Provide PDF or documentation path

❌ **Don't**: Skip build validation
✅ **Do**: Ensure `npm run build` passes before completing

❌ **Don't**: Generate content without spec.md
✅ **Do**: Create spec first with `/sp.specify`

## File Structure

```
.claude/
├── agents/
│   ├── educational-content-generator.agent.md  # Agent definition
│   └── README.md                                # This file
└── commands/
    └── generate-module-content.md               # Skill definition

docs/
└── module<N>-<slug>/                            # Generated by skill
    ├── _category_.json
    ├── 01-<chapter>.mdx
    ├── 02-<chapter>.mdx
    ├── 03-<chapter>.mdx
    ├── 04-<chapter>.mdx
    └── 05-<chapter>.mdx

specs/
└── <feature-id>/
    ├── spec.md                                  # Required input
    ├── plan.md                                  # Optional input
    └── tasks.md                                 # Required input

history/prompts/<feature-id>/
└── ###-generate-module-content.green.prompt.md  # Auto-generated PHR
```

## Contributing

To add new agents or skills:

1. Create agent definition: `.claude/agents/<name>.agent.md`
2. Create skill command: `.claude/commands/<name>.md`
3. Update this README with usage instructions
4. Test thoroughly with sample content
5. Document quality standards and requirements

## Support

For issues or questions:
- Review agent/skill documentation above
- Check troubleshooting section
- Consult `.specify/memory/constitution.md` for project rules
- Review PHRs in `history/prompts/` for examples

---

**Last Updated**: 2025-12-04
**Version**: 1.0.0
**Maintained By**: Physical AI & Humanoid Robotics Team
