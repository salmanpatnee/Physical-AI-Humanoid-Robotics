# Quick Start Guide: Educational Content Generation

This guide shows you how to quickly generate a new educational module using the custom agent and skill.

## Prerequisites

Before you start, ensure you have:
- ✅ Source material (PDF, documentation, or research papers)
- ✅ Feature specification created (`/sp.specify`)
- ✅ Implementation plan created (`/sp.plan`)
- ✅ Task breakdown created (`/sp.tasks`)

## Quick Start: Generate Your First Module

### Step 1: Prepare Your Feature

If you haven't already created the feature, run:

```bash
/sp.specify
```

Describe your module (e.g., "Module 2: The Digital Twin - Simulation with Gazebo and Isaac Sim")

Then create the plan and tasks:

```bash
/sp.plan
/sp.tasks
```

### Step 2: Locate Your Source Material

Make sure your source material (PDF, documentation) is accessible:

```bash
# Example structure:
doc/
├── Hackathon I_ Physical AI & Humanoid Robotics Textbook.pdf
└── supplementary-materials/
    └── simulation-guide.pdf
```

### Step 3: Generate Module Content

Run the slash command with your feature details:

```bash
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2
```

**With custom module name:**
```bash
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2 --module-name "The Digital Twin"
```

### Step 4: Wait for Generation

The agent will:
1. ✅ Validate your feature and source material
2. ✅ Extract content from PDF
3. ✅ Generate 5 chapters with proper frontmatter
4. ✅ Create code examples and exercises
5. ✅ Update sidebar configuration
6. ✅ Validate build
7. ✅ Create PHR

This typically takes 5-10 minutes depending on content complexity.

### Step 5: Review Generated Content

Open your browser and navigate to:
```
http://localhost:3000/docs/module2-digital-twin
```

(If dev server isn't running, start it: `npm start`)

Review:
- [ ] All 5 chapters are visible in sidebar
- [ ] Content is accurate and sourced from materials
- [ ] Code examples are complete and well-explained
- [ ] Exercises have hints and solutions
- [ ] Learning goals and prerequisites are clear

### Step 6: Make Adjustments (Optional)

If you need to edit any content:

```bash
# Edit specific chapter
code docs/module2-digital-twin/01-introduction.mdx

# Or use Claude to make edits
Claude, please update Chapter 2 to include more examples of Gazebo simulation.
```

### Step 7: Finalize

Once you're satisfied:

```bash
# Commit your work
git add docs/module2-digital-twin sidebars.ts specs/
git commit -m "Add Module 2: The Digital Twin content"

# Optional: Create PR
/sp.git.commit_pr
```

## Example: Complete Workflow

Here's a real example creating Module 2:

```bash
# 1. Create feature specification
/sp.specify
# User describes: "Module 2: The Digital Twin - Learn about simulation environments
# for humanoid robots including Gazebo and Isaac Sim"

# 2. Create implementation plan
/sp.plan
# System generates plan.md with architecture decisions

# 3. Generate task breakdown
/sp.tasks
# System creates tasks.md with detailed implementation steps

# 4. Generate module content
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2 --module-name "The Digital Twin"

# Wait 5-10 minutes...

# 5. Review in browser
# Open: http://localhost:3000/docs/module2-digital-twin

# 6. Commit and finalize
git add .
git commit -m "Add Module 2: The Digital Twin content"
```

## Common Arguments

### Required Arguments

- `--feature <feature-id>`: Feature directory name (e.g., `005-module2-simulation`)
- `--source <pdf-path>`: Path to source PDF or documentation

### Optional Arguments

- `--module-number <num>`: Module number for directory naming (default: auto-detect)
- `--module-name <name>`: Display name for the module (default: from spec.md)

## Common Use Cases

### Use Case 1: Standard Module Generation

**Scenario**: Create a new module from your course textbook

```bash
/generate-module-content --feature 005-module2-simulation --source doc/textbook.pdf --module-number 2
```

### Use Case 2: Module with Multiple Sources

**Scenario**: Combine content from textbook and supplementary materials

```bash
/generate-module-content --feature 006-module3-perception --source "doc/textbook.pdf,doc/perception-supplement.pdf" --module-number 3
```

### Use Case 3: Custom Module Name

**Scenario**: Override module name from spec

```bash
/generate-module-content --feature 007-module4-manipulation --source doc/textbook.pdf --module-number 4 --module-name "Grasping and Manipulation"
```

### Use Case 4: Regenerate Existing Module

**Scenario**: Regenerate a module with updated content

```bash
# System will ask if you want to overwrite
/generate-module-content --feature 005-module2-simulation --source doc/textbook-v2.pdf --module-number 2
```

## Troubleshooting Quick Fixes

### Issue: "Feature directory not found"

**Fix**: Create feature first
```bash
/sp.specify
# Then try again
```

### Issue: "Source file not found"

**Fix**: Check file path
```bash
# List files in doc directory
ls doc/

# Use correct path
/generate-module-content --feature 005-module2-simulation --source "doc/Hackathon I_ Physical AI & Humanoid Robotics Textbook.pdf" --module-number 2
```

### Issue: "Build failed"

**Fix**: Check error details
```bash
# Manually run build to see errors
npm run build

# Common fixes:
# 1. Check frontmatter YAML syntax
# 2. Verify MDX component syntax
# 3. Ensure all imports are correct
```

### Issue: "Module not showing in sidebar"

**Fix**: Restart dev server
```bash
# Stop server (Ctrl+C)
# Clear cache
npm run clear

# Restart
npm start
```

## Tips for Best Results

### 1. Provide Quality Source Material

✅ **Good**: Comprehensive textbook chapter with examples
❌ **Bad**: Brief outline or abstract

### 2. Have Clear Specifications

✅ **Good**: Detailed spec.md with chapter titles and learning objectives
❌ **Bad**: Vague "create some content about robots"

### 3. Review Generated Content

✅ **Good**: Read through chapters, test code examples
❌ **Bad**: Assume everything is perfect without review

### 4. Iterate if Needed

✅ **Good**: Ask Claude to refine specific sections
❌ **Bad**: Accept first draft if quality is insufficient

### 5. Validate Build Always

✅ **Good**: Ensure `npm run build` passes
❌ **Bad**: Skip build validation

## Next Steps

After generating your first module:

1. **Generate More Modules**: Use the same workflow for Modules 3, 4, 5, etc.
2. **Create Complementary Content**: Add case studies, projects, or assessments
3. **Review and Refine**: Iterate on content quality based on feedback
4. **Share and Deploy**: Build static site and deploy to hosting

## Getting Help

If you run into issues:

1. Check the main [README.md](README.md) for detailed documentation
2. Review the agent definition: `educational-content-generator.agent.md`
3. Check the skill definition: `../commands/generate-module-content.md`
4. Look at PHRs in `history/prompts/` for successful examples
5. Consult the constitution: `.specify/memory/constitution.md`

## Success Checklist

Your module generation is successful when:

- ✅ All 5 chapters created with valid frontmatter
- ✅ MDX components render correctly (LearningGoals, Prerequisites, etc.)
- ✅ Code examples are complete and runnable
- ✅ Exercises include hints and solutions
- ✅ Build passes: `npm run build` exit code 0
- ✅ Module appears in sidebar at correct position
- ✅ Content is accurate and sourced from materials
- ✅ Tasks marked complete in tasks.md
- ✅ PHR created in history/prompts/

---

**Ready to generate your first module?**

```bash
/generate-module-content --feature <your-feature> --source <your-pdf> --module-number <number>
```

Good luck! 🚀
