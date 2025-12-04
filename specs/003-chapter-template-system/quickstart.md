# Quickstart: Authoring with the New Chapter Template

This guide explains how to create a new chapter using the reusable template system for the Physical AI & Humanoid Robotics Textbook.

## 1. Create a New Chapter File

First, create a new folder and file for your chapter inside the `/docs` directory. The folder and file name should be prefixed with a two-digit number to ensure correct sidebar ordering.

For example, to create a new chapter titled "Advanced Locomotion", you might create:

```
/docs/05-advanced-locomotion/index.mdx
```

## 2. Add the Frontmatter

Every chapter file must begin with a frontmatter block that provides metadata about the chapter. This metadata is validated automatically when the site is built.

Copy and paste the following template into your `index.mdx` file and fill in the values.

```yaml
---
title: "Your Chapter Title"
sidebar_position: 5
chapter_type: "concept" # can be: tutorial, concept, lab, or reference
learning_goals:
  - "First learning goal."
  - "Second learning goal."
prerequisites:
  - "Concept from a previous chapter."
  - "A specific technology (e.g., Python)."
key_takeaways:
  - "First key takeaway."
  - "Second key takeaway."
---
```

## 3. Using the Custom Components

You can now start writing your chapter content using standard Markdown and the custom components provided.

### Importing Components

While many components are globally available, it's good practice to import them if needed. For the `ExerciseBlock`, you will need to import it.

```javascript
import { ExerciseBlock } from '@site/src/components/ExerciseBlock';
```

### Learning Goals, Prerequisites, and Key Takeaways

These components are designed to wrap lists of items.

```mdx
<LearningGoals>
- Goal 1
- Goal 2
</LearningGoals>

<Prerequisites>
- Prereq 1
- Prereq 2
</Prerequisites>

<KeyTakeaways>
- Takeaway 1
- Takeaway 2
</KeyTakeaways>
```

### Interactive Exercises

The `ExerciseBlock` component allows you to create interactive problems with hints and a solution.

```mdx
<ExerciseBlock
  question="What is the primary function of a robot's actuator?"
  hints={[
    { title: "Hint 1", content: "Think about what makes a robot move." },
    { title: "Hint 2", content: "It's the component that converts energy into physical motion." }
  ]}
  solution={
    <div>
      An actuator is a component of a machine that is responsible for moving and controlling a mechanism or system.
    </div>
  }
/>
```

## 4. Writing Content

You can write the rest of your content using standard Docusaurus MDX features, including headers, lists, images, and code blocks.

```mdx
## Section 1: Introduction

This is the first section of the chapter...
```

By following this structure, your chapter will be consistent with all others in the book and will be automatically validated and integrated into the site's navigation.
