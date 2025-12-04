# Data Model for Chapter Template System

**Date**: 2025-12-04

This document defines the data model for the chapter metadata. The model is enforced by a JSON Schema, which will be used by a custom Docusaurus plugin with AJV to validate chapter frontmatter during the build process.

## Chapter Metadata

The core data entity is the **Chapter**. Its metadata is defined in the frontmatter of each `.mdx` file.

### Entity Definition

-   **Entity**: `Chapter`
-   **Description**: Represents a single chapter in the textbook.
-   **Attributes**: Defined in the JSON schema below. These attributes control the chapter's type, learning objectives, and other metadata.

### JSON Schema (`ChapterMetadata.schema.json`)

This schema defines the contract for a chapter's frontmatter.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Chapter Metadata",
  "description": "Schema for the frontmatter of a chapter in the Physical AI & Humanoid Robotics Textbook.",
  "type": "object",
  "properties": {
    "title": {
      "description": "The main title of the chapter, displayed in the sidebar and at the top of the page.",
      "type": "string"
    },
    "sidebar_position": {
      "description": "The numerical position of the chapter in the sidebar.",
      "type": "number"
    },
    "chapter_type": {
      "description": "The pedagogical type of the chapter.",
      "type": "string",
      "enum": ["tutorial", "concept", "lab", "reference"]
    },
    "learning_goals": {
      "description": "A list of key learning goals for the chapter.",
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1
    },
    "prerequisites": {
      "description": "A list of prerequisite chapters or concepts.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "key_takeaways": {
      "description": "A list of key takeaways or summary points for the chapter.",
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1
    }
  },
  "required": [
    "title",
    "sidebar_position",
    "chapter_type",
    "learning_goals",
    "key_takeaways"
  ]
}
```

### State Transitions

-   N/A. The chapter metadata is static for a given file and does not have state transitions. It is validated at build-time.
