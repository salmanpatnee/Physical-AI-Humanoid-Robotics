# Data Model: Module 2 - The Digital Twin (Gazebo & Unity)

This feature is content-focused and does not introduce new data models to the application. The primary "data" are the MDX files themselves, which adhere to a frontmatter schema for metadata.

## MDX Frontmatter Schema

Each MDX file for a chapter will contain a frontmatter block with the following fields:

- **id**: A unique identifier for the chapter.
- **title**: The title of the chapter.
- **sidebar_position**: The position of the chapter in the sidebar.
- **learning_objectives**: An array of strings describing the learning objectives for the chapter.
- **prerequisites**: An array of strings describing the prerequisites for the chapter.

This schema is validated by the Docusaurus build process.
