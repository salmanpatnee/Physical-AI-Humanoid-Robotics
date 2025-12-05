# Data Model for Weekly Course Schedule Page

This document outlines the data structure for the content that will be displayed on the Weekly Course Schedule page, based on the "Key Entities" section of the feature specification. As this is a static content page, this model describes the conceptual structure of the information, not a database schema.

## Core Entities

### 1. Week

Represents a single week in the 13-week course schedule.

| Attribute | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `weekNumber` | Integer | The number of the week (1-13). | Yes |
| `title` | String | The title for the week (e.g., "ROS 2 Fundamentals"). | Yes |
| `module` | String | The primary module(s) covered. | Yes |
| `prerequisites`| String | A brief note on required knowledge for the week, especially at module transitions. | No |
| `topics` | Array[String] | A list of specific topics or chapters to read. Chapter references must be clickable links. | Yes |
| `activities` | Array[String] | A list of hands-on activities, labs, or projects. | Yes |
| `timeEstimate`| String | The estimated time commitment for the week (e.g., "Approx. 10 hours"). | Yes |

### 2. Visual Timeline Mapping

Represents the high-level relationship between modules and the weekly schedule, to be visualized as a table or Mermaid diagram.

| Attribute | Type | Description | Required |
| :--- | :--- | :--- | :--- |
| `moduleName` | String | The name of the module (e.g., "Module 1: Robotic Nervous System"). | Yes |
| `weekRange` | String | The range of weeks the module covers (e.g., "Weeks 3-5"). | Yes |
| `keyFocus` | String | A brief description of the module's focus. | Yes |

## Example Structure (Conceptual)

This is how the data might be structured within the MDX file for a single week's entry.

```yaml
- weekNumber: 3
  title: "ROS 2 Fundamentals"
  module: "Module 1: The Robotic Nervous System"
  prerequisites: "Completion of Introduction to Physical AI (Weeks 1-2)."
  topics:
    - "[Focus: Middleware for Robot Control](path/to/chapter)"
    - "[ROS 2 Nodes, Topics, & Services](path/to/chapter)"
  activities:
    - "Setup ROS 2 development environment."
    - "Create a simple 'Hello World' publisher and subscriber."
  timeEstimate: "Approx. 10 hours"
```
