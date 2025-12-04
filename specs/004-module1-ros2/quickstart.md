# Quickstart: Authoring a New Chapter in Module 1

This guide explains how to create a new chapter within Module 1: "The Robotic Nervous System (ROS 2)".

## 1. Create the Chapter File

All chapters for Module 1 belong in the `/docs/module1-robotic-nervous-system/` directory. Create a new `.mdx` file here, ensuring the filename is prefixed with a two-digit number for correct sidebar ordering.

For example, to create the first chapter, you would create the file:

```
/docs/module1-robotic-nervous-system/01-focus-middleware-for-robot-control.mdx
```

## 2. Add the Frontmatter

Each chapter file must begin with a frontmatter block that provides the necessary metadata. This metadata is validated automatically against the project's `ChapterMetadata.schema.json`.

Copy the template below and fill in the values for your specific chapter.

```yaml
---
title: "1. Focus: Middleware for Robot Control"
sidebar_position: 1
chapter_type: "concept"
learning_goals:
  - "Understand the role of middleware in robotics."
  - "Recognize why ROS 2 is a foundational tool for humanoid robotics."
prerequisites:
  - "Basic understanding of programming concepts."
key_takeaways:
  - "Middleware connects different software components in a complex system."
  - "ROS 2 provides a standardized communication layer for robots."
---
```

## 3. Add Content Using MDX Components

You can now write your chapter content. Use the globally available MDX components to structure your educational material.

```mdx
import { ExerciseBlock } from '@site/src/components/ExerciseBlock';

# Focus: Middleware for Robot Control

<LearningObjectives />

This chapter introduces the concept of middleware...

<KeyTakeaways />

### Exercises

<ExerciseBlock
  question="In your own words, what is middleware?"
  hints={[
    { title: "Hint 1", content: "Think about it as a 'software bus'." },
    { title: "Hint 2", content: "It helps different programs talk to each other without knowing the details of the other programs." }
  ]}
  solution={
    <div>
      Middleware is a software layer that provides services to software applications beyond those available from the operating system. It acts as a bridge, making it easier for developers to create communication and input/output for distributed applications.
    </div>
  }
/>
```

## 4. Update the Sidebar Category

Ensure the file `/docs/module1-robotic-nervous-system/_category_.json` exists and is configured correctly to give the module a label in the sidebar.

```json
{
  "label": "Module 1: The Robotic Nervous System",
  "position": 2,
  "link": {
    "type": "generated-index"
  }
}
```

By following this process, your new chapter will be correctly integrated into the textbook.
