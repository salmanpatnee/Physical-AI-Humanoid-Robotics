# Quickstart Guide: Module 4 Content Generation

This guide provides a quick overview and instructions for generating and editing content for Module 4, "Vision-Language-Action (VLA)", within the Docusaurus project.

## 1. Directory Structure

All content for Module 4 will reside in the following main directories:

-   **MDX Chapters**: `docs/007-module4-vla/`
-   **Example Files**: `examples/module4/`
-   **Static Assets (images, etc.)**: `static/img/module4/`

Ensure that all files and directories follow the `NN-prefix-semantic-filename` convention (e.g., `01-focus-the-convergence-of-llms-and-robotics.mdx`).

## 2. Creating New Chapters (MDX Files)

1.  Navigate to the `docs/007-module4-vla/` directory.
2.  Create a new MDX file (e.g., `01-new-chapter-title.mdx`).
3.  **Frontmatter**: Every MDX file *must* include a frontmatter block at the top. This metadata is crucial for Docusaurus and for validation.

    ```markdown
    ---
    id: new-chapter-title-slug
    title: New Chapter Title
    sidebar_position: 1 # Increment for each new chapter in the module
    slug: /module4/new-chapter-title-slug
    description: A brief description of the chapter's content.
    category: module4-vla
    keywords: [vla, llm, robotics] # Optional keywords
    # Add other custom metadata as defined in the JSON Schema
    ---
    ```
    *Note*: The `id` should be unique and slug-like. `sidebar_position` dictates the order within the module. `slug` defines the URL path. `category` links it to the module's sidebar.

4.  **Content**: Start writing your chapter content using Markdown and the project's custom MDX components:
    -   `<LearningObjectives />`
    -   `<KeyTakeaways />`
    -   `<Prerequisites />`
    -   `<ExerciseBlock />`

    Example usage:
    ```markdown
    import LearningObjectives from '@site/src/components/LearningGoals';
    import ExerciseBlock from '@site/src/components/ExerciseBlock';

    # My New Chapter

    <LearningObjectives
      objectives={[
        "Understand concept X",
        "Implement technique Y",
      ]}
    />

    This is the main content of your chapter.

    <ExerciseBlock title="Hands-on Exercise" type="code-along">
      Follow these steps to...
      ```python
      # Your VLA code here
      print("Hello VLA!")
      ```
    </ExerciseBlock>
    ```

## 3. Adding Example Files

For code examples, simulation scenes, or configuration blocks, place them in the appropriate subdirectories under `examples/module4/`:

-   `examples/module4/whisper-inference/`
-   `examples/module4/llm-planning-prompts/`
-   `examples/module4/vision-graphs/`
-   `examples/module4/vla-pipelines/`

Reference these files from your MDX chapters using relative paths.

## 4. Adding Images and Static Assets

Place any images, diagrams, or other static assets relevant to Module 4 in `static/img/module4/`.
Reference them in your MDX files using absolute paths from the static directory: `![Alt Text](/img/module4/my-image.png)`.

## 5. Docusaurus Build & Validation

To ensure your content is correctly formatted and valid, run the Docusaurus build process locally:

```bash
npm run build
```

This command will validate the frontmatter against the JSON Schema and check for any structural errors. Address any warnings or errors reported during the build.

## 6. Local Development Server

To preview your changes in real-time, start the Docusaurus development server:

```bash
npm run start
```
Then navigate to `http://localhost:3000/module4/`.
