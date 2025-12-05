# Data Model for Module 3 - The AI-Robot Brain (NVIDIA Isaac)

This document outlines the key entities involved in Module 3's content structure, primarily building upon the existing Docusaurus document and content model.

## Entities

### 1. Module
Represents a top-level learning unit, encompassing multiple chapters.

-   **Name**: `Module 3: The AI-Robot Brain (NVIDIA Isaac)`
-   **ID**: `006-module3-ai-robot-brain` (corresponds to directory naming convention)
-   **Chapters**: Ordered list of Chapter entities.
-   **Metadata**:
    -   `title`: "The AI-Robot Brain (NVIDIA Isaac)"
    -   `sidebar_position`: `6` (derived from module ID)
    -   `type`: "module" (custom frontmatter for categorization)
    -   `description`: Short summary of the module's content and learning goals.

### 2. Chapter
A self-contained learning unit within a Module, typically corresponding to a single MDX file.

-   **ID**: `NN-chapter-slug` (e.g., `01-focus-advanced-perception-and-synthetic-data`)
-   **Title**: Display title of the chapter (e.g., "Focus: Advanced perception and synthetic data")
-   **Content**: MDX formatted text, incorporating standard Markdown and custom MDX components.
-   **Custom MDX Components**:
    -   `<LearningObjectives />`: Lists key learning objectives for the chapter.
    -   `<KeyTakeaways />`: Summarizes main points for review.
    -   `<Prerequisites />`: Lists required prior knowledge or setup.
    -   `<ExerciseBlock />`: Encapsulates structured exercises.
-   **Frontmatter Metadata**:
    -   `id`: Unique identifier (e.g., `focus-advanced-perception-and-synthetic-data`)
    -   `title`: Display title of the chapter.
    -   `sidebar_position`: Numeric order within the module (e.g., `1`, `2`, `3`, `4`).
    -   `slug`: URL-friendly path.
    -   `description`: Short chapter summary.
    -   `category`: Reference to the parent module's category (e.g., `module3-ai-robot-brain`).
    -   Additional metadata validated against JSON Schema (e.g., `difficulty`, `estimated_time`).

### 3. Exercise
A structured activity embedded within an `<ExerciseBlock />` component in a Chapter.

-   **Type**: e.g., "Code Along", "Conceptual Question", "Simulation Task", "Deployment Challenge"
-   **Description**: Detailed instructions for the student.
-   **Expected Output/Outcome**: What the student should achieve.
-   **Hints/Solutions**: (Optional) Guidance or complete solutions.
-   **Associated Files**: References to example code or configuration files (e.g., in `examples/module3/`).

### 4. Example Scene
A pre-built simulation environment or project for NVIDIA Isaac Sim.

-   **Name**: Descriptive name (e.g., "Basic Humanoid Navigation Scene")
-   **File Path**: Location within `examples/module3/isaac-sim-scenes/`.
-   **Purpose**: Illustrates a concept, serves as a starting point for an exercise.
-   **Associated Chapter**: Reference to the Chapter where it's used.

### 5. Pipeline
A defined series of processing steps, particularly for Isaac ROS (e.g., VSLAM pipeline, perception graph).

-   **Name**: Descriptive name (e.g., "Stereo VSLAM Pipeline")
-   **Configuration Files/Code**: Relevant ROS/Isaac ROS launch files, YAML configurations, or Python scripts.
-   **Purpose**: Demonstrates a functional robotic capability.
-   **Associated Chapter**: Reference to the Chapter where it's used.

### 6. Configuration Block
A snippet of code or configuration data (e.g., for Nav2, a URDF fragment).

-   **Type**: e.g., "YAML", "XML", "Python", "C++"
-   **Content**: The actual configuration text.
-   **Purpose**: Illustrates how to set up or configure a system component.
-   **Associated Chapter**: Reference to the Chapter where it's used.
