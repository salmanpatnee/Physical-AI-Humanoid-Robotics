# Data Model for Module 4 - Vision-Language-Action (VLA)

This document outlines the key entities involved in Module 4's content structure, primarily building upon the existing Docusaurus document and content model.

## Entities

### 1. Module
Represents a top-level learning unit, encompassing multiple chapters.

-   **Name**: `Module 4: Vision-Language-Action (VLA)`
-   **ID**: `007-module4-vla` (corresponds to directory naming convention)
-   **Chapters**: Ordered list of Chapter entities.
-   **Metadata**:
    -   `title`: "Vision-Language-Action (VLA)"
    -   `sidebar_position`: `7` (derived from module ID)
    -   `type`: "module" (custom frontmatter for categorization)
    -   `description`: Short summary of the module's content and learning goals.

### 2. Chapter
A self-contained learning unit within a Module, typically corresponding to a single MDX file.

-   **ID**: `NN-chapter-slug` (e.g., `01-focus-the-convergence-of-llms-and-robotics`)
-   **Title**: Display title of the chapter (e.g., "Focus: The convergence of LLMs and robotics")
-   **Content**: MDX formatted text, incorporating standard Markdown and custom MDX components.
-   **Custom MDX Components**:
    -   `<LearningObjectives />`: Lists key learning objectives for the chapter.
    -   `<KeyTakeaways />`: Summarizes main points for review.
    -   `<Prerequisites />`: Lists required prior knowledge or setup.
    -   `<ExerciseBlock />`: Encapsulates structured exercises.
-   **Frontmatter Metadata**:
    -   `id`: Unique identifier (e.g., `focus-the-convergence-of-llms-and-robotics`)
    -   `title`: Display title of the chapter.
    -   `sidebar_position`: Numeric order within the module (e.g., `1`, `2`, `3`, `4`).
    -   `slug`: URL-friendly path.
    -   `description`: Short chapter summary.
    -   `category`: Reference to the parent module's category (e.g., `module4-vla`).
    -   Additional metadata validated against JSON Schema (e.g., `difficulty`, `estimated_time`).

### 3. Exercise
A structured activity embedded within an `<ExerciseBlock />` component in a Chapter.

-   **Type**: e.g., "Code Along", "Conceptual Question", "Simulation Task", "Deployment Challenge"
-   **Description**: Detailed instructions for the student.
-   **Expected Output/Outcome**: What the student should achieve.
-   **Hints/Solutions**: (Optional) Guidance or complete solutions.
-   **Associated Files**: References to example code or configuration files (e.g., in `examples/module4/`).

### 4. Whisper Inference Example
Code or configuration demonstrating speech-to-text inference using OpenAI Whisper.

-   **Name**: Descriptive name (e.g., "Basic Whisper Inference Script")
-   **File Path**: Location within `examples/module4/whisper-inference/`.
-   **Purpose**: Illustrates how to convert audio to text commands.
-   **Associated Chapter**: Reference to the Chapter where it's used.

### 5. LLM Planning Prompt
Examples of natural language prompts designed to guide Large Language Models for cognitive planning and task decomposition.

-   **Name**: Descriptive name (e.g., "LLM Prompt for Object Manipulation")
-   **File Path**: Location within `examples/module4/llm-planning-prompts/`.
-   **Purpose**: Shows how to instruct an LLM to generate robot intentions.
-   **Associated Chapter**: Reference to the Chapter where it's used.

### 6. Vision Graph
A visual representation, configuration file, or code for a computer vision pipeline.

-   **Name**: Descriptive name (e.g., "Object Detection Vision Graph")
-   **File Path**: Location within `examples/module4/vision-graphs/`.
-   **Purpose**: Illustrates how a robot perceives its environment and identifies objects.
-   **Associated Chapter**: Reference to the Chapter where it's used.

### 7. VLA Pipeline
An integrated system that demonstrates the full Vision-Language-Action loop.

-   **Name**: Descriptive name (e.g., "Humanoid Pick-and-Place VLA")
-   **Configuration Files/Code**: ROS 2 launch files, Python scripts, integration components.
-   **Purpose**: The capstone example, showing an autonomous humanoid acting on voice commands.
-   **Associated Chapter**: Reference to the Chapter where it's used (Capstone Chapter).
