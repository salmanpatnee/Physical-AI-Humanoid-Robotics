# Implementation Plan: Child-Friendly Content Simplification

**Branch**: `001-simplified-content` | **Date**: 2025-12-06 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-simplified-content/spec.md`

**Note**: This plan follows the `/sp.plan` workflow and includes research, design, and architectural decisions for simplifying all coursebook content for children aged 8-12.

## Summary

Transform the Physical AI & Humanoid Robotics coursebook content from technical/academic language into child-friendly explanations that 8-12 year olds can understand. Add structured learning aids including "What You Will Learn" summaries, "Doubtful Questions and Answers" sections, "Grown-Up Words" glossaries, and plain-language code annotations. Maintain 100% technical accuracy while using relatable real-life analogies and everyday examples throughout all 4 modules.

**Primary Approach**: Content rewriting and enhancement workflow using AI-assisted simplification with human review gates, implemented through custom Docusaurus MDX components and content transformation scripts.

## Technical Context

**Language/Version**: JavaScript/TypeScript (Node 22.x), React 19.0.0, MDX
**Primary Dependencies**: Docusaurus 3.9.2, React 19, Lucide React (icons), existing custom components
**Storage**: File-based (MDX files in `/docs/` directory structure)
**Testing**: Content validation (readability metrics, technical accuracy checks), A11y contrast testing (Playwright + Axe-Core)
**Target Platform**: Static website (GitHub Pages), browser-based rendering
**Project Type**: Web (static documentation site with interactive components)
**Performance Goals**:
- Page load time <2 seconds
- Reading level: Flesch-Kincaid Grade 3-6
- Comprehension rate: 90%+ for target age group
**Constraints**:
- Preserve existing Docusaurus structure and navigation
- Maintain existing chapter frontmatter schema (validated by chapter-validation plugin)
- No breaking changes to deployed site during rollout
- All content must pass technical accuracy review
**Scale/Scope**:
- 19 existing chapters across 4 modules
- ~50-70 MDX files including supporting pages
- Estimated 200-300 new "Doubtful Questions" across all content
- ~100-150 code examples requiring plain-language annotations

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Article I: Core Principles Compliance

✅ **Deterministic Generation**:
- Content simplification follows defined templates and style guides
- AI-generated simplified content is version-controlled and reproducible
- Same source content produces consistent simplified output when following same rules

✅ **Reproducibility**:
- Simplification process documented in research.md with clear guidelines
- Templates for "What You Will Learn", Q&A, and glossaries enable consistent output
- Content transformation can be re-run to regenerate simplified versions

✅ **Composability**:
- New MDX components (WhatYouWillLearn, DoubtfulQA, GrownUpWords) are modular and reusable
- Components can be used across all chapters without modification
- Simplification approach is module-agnostic

✅ **Human Override & Oversight**:
- All simplified content requires human review for technical accuracy (FR-004, SC-006)
- Quality gates include educator review and child comprehension testing
- Human editors can override AI suggestions at any stage

✅ **Anti-Hallucination Mandate**:
- All simplified content must preserve technical accuracy from original chapters
- No new concepts introduced; only translation of existing concepts to simpler language
- Analogies and examples must accurately represent underlying technical principles
- Technical accuracy validation required before deployment (SC-006)

### Article III: Spec-Driven Life Cycle Compliance

✅ **Specification**: Complete specification exists (spec.md) with functional requirements, success criteria, and user stories

✅ **Quality Gates Defined**:
- Readability metrics (Flesch-Kincaid Grade 3-6)
- Technical accuracy validation (100% requirement)
- Comprehension testing with target age group
- A11y compliance maintained

### Article IV: Quality Standards

✅ **Markdown Correctness**: All simplified content will be MDX (superset of GFM)

✅ **Docusaurus Structure**: Preserves existing `/docs/` structure and navigation

✅ **Front-Matter Format**: Maintains existing frontmatter schema validated by chapter-validation plugin

✅ **Deterministic Output**: Simplification follows documented guidelines and templates

✅ **Consistent Folder Naming**: No changes to existing folder structure

### Article VI: AI Behavior Governance

✅ **AI MUST**:
- Strictly adhere to this specification and constitution
- Generate content only by simplifying existing source material (no invention)
- Maintain deterministic and reproducible outputs through templates
- Flag ambiguities for human clarification
- Ensure outputs conform to quality standards
- Create PHR for this planning work

✅ **AI MUST NOT**:
- Modify chapter structure or navigation without approval
- Fabricate technical content not present in original material
- Make architecturally significant decisions without human approval
- Write tests unless explicitly requested

✅ **AI MUST Always Ask Human Approval For**:
- Final simplified content before publication
- Deployment to production
- Any modifications to existing technical content that change meaning
- Architecturally significant component design decisions

### Gate Status: ✅ **PASSED**

All constitutional principles are satisfied. Proceeding to Phase 0 research.

## Project Structure

### Documentation (this feature)

```text
specs/001-simplified-content/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output: Simplification guidelines, analogies, Q&A patterns
├── data-model.md        # Phase 1 output: Content structure, component schemas
├── quickstart.md        # Phase 1 output: Guide for content writers/reviewers
├── contracts/           # Phase 1 output: Component APIs, content templates
│   ├── WhatYouWillLearn.schema.json
│   ├── DoubtfulQA.schema.json
│   ├── GrownUpWords.schema.json
│   └── SimplificationGuidelines.md
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Existing Structure (Preserved)
docs/
├── module1-robotic-nervous-system/
│   ├── 01-focus-middleware-for-robot-control.mdx
│   ├── 02-ros2-nodes-topics-services.mdx
│   ├── 03-bridging-python-agents-with-rclpy.mdx
│   ├── 04-understanding-urdf.mdx
│   └── 05-managing-complex-systems-with-launch-files.mdx
├── module2-the-digital-twin/
│   ├── 01-focus-physics-simulation-and-world-building.mdx
│   ├── 02-simulating-collisions-gravity-and-sensors-in-gazebo.mdx
│   ├── 03-high-fidelity-rendering-and-interaction-scenes-in-unity.mdx
│   └── 04-sensor-simulation-lidar-depth-cameras-and-imus.mdx
├── module3-ai-robot-brain/
│   ├── 01-focus-advanced-perception-and-synthetic-data.mdx
│   ├── 02-isaac-sim-for-photorealistic-simulation-and-training.mdx
│   ├── 03-isaac-ros-for-gpu-accelerated-vslam-and-navigation.mdx
│   └── 04-nav2-for-humanoid-path-planning-and-locomotion.mdx
├── module4-vision-language-action/
│   ├── 01-focus-the-convergence-of-llms-and-robotics.mdx
│   ├── 02-voice-to-action-using-whisper.mdx
│   ├── 03-cognitive-planning-using-llms-for-ros2-task-decomposition.mdx
│   └── 04-capstone-the-autonomous-humanoid.mdx
├── assessments.mdx
└── weekly-schedule.mdx

# New Components (To Be Created)
src/components/
├── WhatYouWillLearn/      # NEW: Learning objectives summary component
│   ├── index.tsx
│   └── styles.module.css
├── DoubtfulQA/            # NEW: Questions and answers component
│   ├── index.tsx
│   └── styles.module.css
├── GrownUpWords/          # NEW: Technical glossary component
│   ├── index.tsx
│   └── styles.module.css
└── SimplifiedContent/     # NEW: Wrapper for simplified sections
    ├── index.tsx
    └── styles.module.css

# Content Enhancement Scripts (To Be Created)
scripts/
├── simplify-content/
│   ├── analyze-readability.js      # Flesch-Kincaid and other metrics
│   ├── validate-accuracy.js        # Technical accuracy checker
│   ├── generate-qa-suggestions.js  # AI-assisted Q&A generation
│   └── extract-technical-terms.js  # Build "Grown-Up Words" mappings

# Testing (To Be Created)
tests/
└── content/
    ├── readability.test.js         # Automated readability checks
    ├── component-rendering.test.js # Component unit tests
    └── technical-accuracy.test.js  # Accuracy validation tests
```

**Structure Decision**:
Preserving existing Docusaurus structure to avoid disruption. Adding new React components in `/src/components/` following existing component patterns (ExerciseBlock, LearningGoals, etc.). Content scripts placed in `/scripts/` for content analysis and validation. All simplified content remains in MDX files with new components embedded.

## Complexity Tracking

> No constitution violations detected. This section intentionally left empty.

---

## Phase 0: Research & Guidelines

### Research Objectives

This phase resolves all "NEEDS CLARIFICATION" items and establishes concrete simplification guidelines with real-life analogies and question patterns.

#### Research Task 1: Simplification Style Guide
**Objective**: Define concrete rules for translating technical robotics concepts to child-friendly language (ages 8-12)

**Questions to Answer**:
1. What reading level metrics should we target? (Flesch-Kincaid Grade Level, Flesch Reading Ease)
2. What sentence length and structure rules apply?
3. How do we handle mathematical concepts (quaternions, matrix transformations)?
4. What analogies work best for core robotics concepts?

**Deliverable**: `Simplification-Guidelines.md` with:
- Reading level targets (specific grade levels)
- Sentence structure rules (max words, active voice %, etc.)
- Analogy library for common concepts
- Forbidden words list (jargon to avoid)
- Approved vocabulary list (technical terms that must be used)

#### Research Task 2: Real-Life Analogy Bank
**Objective**: Create a comprehensive library of tested analogies for robotics concepts, as requested in user input

**Core Concepts Requiring Analogies**:

| Technical Concept | Target Analogy Domain | Example Question to Research |
|-------------------|----------------------|------------------------------|
| ROS2 Topics (pub-sub) | Communication systems | "Is it like a walkie-talkie channel?" or "Is it like a classroom announcements speaker?" |
| ROS2 Nodes | Collaborative teams | "Is a node like a worker in a factory?" or "Is it like a student in a group project?" |
| Middleware | Transportation/delivery | "Is middleware like a postal service?" or "Is it like a school bus route?" |
| URDF (robot structure) | Building/anatomy | "Is URDF like a blueprint?" or "Is it like a skeleton with labeled bones?" |
| Sensors (LiDAR, cameras) | Human senses | "Is LiDAR like a bat's echolocation?" or "Is it like measuring with a ruler?" |
| Gazebo simulation | Virtual worlds | "Is it like Minecraft for robots?" or "Is it like a flight simulator?" |
| GPU acceleration | Parallel work | "Is it like having 100 helpers instead of 1?" or "Is it like using a photocopier instead of hand-copying?" |
| VSLAM (mapping) | Navigation/memory | "Is VSLAM like drawing a map as you explore?" or "Is it like remembering landmarks on your way home?" |
| Path planning | Route finding | "Is it like Google Maps for robots?" or "Is it like finding the quickest way through a maze?" |
| LLM task decomposition | Problem solving | "Is it like breaking homework into smaller steps?" or "Is it like following a recipe?" |

**Deliverable**: `Analogy-Bank.md` with:
- 50+ tested analogies mapped to technical concepts
- Age-appropriateness ratings (8-10 vs 10-12)
- Visual diagram suggestions for each analogy
- Potential misconceptions each analogy might create (with mitigation strategies)

#### Research Task 3: Doubtful Question Patterns
**Objective**: Identify common confusion points and create question templates, as requested in user input

**Question Categories**:

1. **Confusion Type: Terminology Mixups**
   - Example: "Is a ROS2 node the same as a Python function?"
   - Pattern: "Is [new term] the same as [familiar but different concept]?"

2. **Confusion Type: Why vs How**
   - Example: "Why do we need middleware instead of just connecting everything directly?"
   - Pattern: "Why do we need [X] instead of [simpler-sounding alternative]?"

3. **Confusion Type: Scope/Scale Misunderstanding**
   - Example: "Does every robot have 20+ motors like humanoids?"
   - Pattern: "Does every [general thing] have [specific attribute] like [specific example]?"

4. **Confusion Type: Simulation vs Reality**
   - Example: "If I build it in Gazebo, will it work on a real robot?"
   - Pattern: "If I do [X] in simulation, will it work in [real world]?"

5. **Confusion Type: Abstract Concepts**
   - Example: "How can a robot 'think' if it doesn't have a brain?"
   - Pattern: "How can [machine] do [human activity] if it doesn't have [human organ/ability]?"

**Deliverable**: `Question-Templates.md` with:
- 10+ question patterns per category
- 5-8 actual questions per chapter (total 95-152 questions across all 19 chapters)
- Answer frameworks that address misconceptions
- Follow-up question suggestions

#### Research Task 4: Code Annotation Strategy
**Objective**: Define approach for plain-language code explanations

**Code Types in Coursebook**:
1. Python ROS2 code (rclpy)
2. Launch files (XML/Python)
3. URDF/SDF files (XML robot descriptions)
4. Command-line instructions
5. Configuration files (YAML)

**Research Questions**:
- Should we use line-by-line comments or block summaries?
- How do we explain syntax without teaching programming?
- What visual aids help (flowcharts, before/after diagrams)?

**Deliverable**: `Code-Annotation-Guide.md` with:
- Annotation format for each code type
- Example annotated code blocks
- "What This Code Does" summary templates
- Visual diagram standards

#### Research Task 5: Grown-Up Words Glossary Structure
**Objective**: Define format and scope of technical term mappings

**Example Mapping**:
```
| Simple Word/Phrase | Technical Term | When You'll Hear It |
|--------------------|----------------|---------------------|
| Robot's brain | Processor/CPU | "The Jetson processor runs the AI" |
| Robot's language | ROS2 | "We use ROS2 to make parts talk" |
| Robot's map | Occupancy grid | "The occupancy grid shows obstacles" |
```

**Deliverable**: `Glossary-Structure.md` with:
- Table format specification
- Placement guidelines (per chapter or per module?)
- Scope decision (all technical terms or only key terms?)
- Progressive disclosure strategy (introduce gradually vs all at once)

### Research Outputs

All research findings will be consolidated in `research.md` using this format:

```markdown
# Research: Child-Friendly Content Simplification

## Decision Summary

### Simplification Guidelines
- **Decision**: [Chosen approach]
- **Rationale**: [Why this works for 8-12 year olds]
- **Alternatives Considered**: [What else was evaluated]
- **Validation Method**: [How we'll test effectiveness]

### Analogy Library
- **Decision**: [Core analogy approach with examples]
- **Rationale**: [Why these analogies are effective]
- **Alternatives Considered**: [Other analogy domains tested]
- **Misconception Mitigation**: [How we prevent confusion]

[Continue for each research task...]
```

---

## Phase 1: Design & Component Contracts

**Prerequisites:** `research.md` complete with all simplification guidelines, analogies, and question patterns defined.

### Design Task 1: Data Model - Content Structure

**File**: `data-model.md`

#### Entity 1: Simplified Chapter Content

```typescript
interface SimplifiedChapter {
  // Existing Frontmatter (Preserved)
  title: string;
  sidebar_position: number;
  chapter_type: 'concept' | 'hands-on' | 'theory' | 'capstone';
  learning_goals: string[];
  prerequisites: string[];
  key_takeaways: string[];

  // New Frontmatter (Added)
  reading_level?: {
    flesch_kincaid_grade: number;  // Target: 3-6
    flesch_reading_ease: number;    // Target: 70-80
  };
  simplification_status?: 'draft' | 'review' | 'approved';
  technical_accuracy_verified?: boolean;

  // Content Sections
  sections: ContentSection[];
}

interface ContentSection {
  heading: string;
  simplified_text: string;        // Rewritten content
  original_text_reference?: string; // Link to original for comparison
  analogies_used: Analogy[];
  technical_terms: TechnicalTerm[];
  doubtful_qa?: DoubtfulQA;       // If this section has confusing points
}
```

#### Entity 2: "What You Will Learn" Component

```typescript
interface WhatYouWillLearnProps {
  goals: LearningGoal[];
  displayStyle?: 'bullets' | 'cards' | 'numbered';
  colorTheme?: 'primary' | 'success' | 'info';
}

interface LearningGoal {
  text: string;                    // Simple, friendly statement
  icon?: string;                   // Lucide icon name (optional)
  why_it_matters?: string;         // Optional expansion
}

// Usage Example:
<WhatYouWillLearn
  goals={[
    {
      text: "Understand how robots talk to each other",
      icon: "MessageCircle",
      why_it_matters: "Just like you need to talk to friends to play a game together, robot parts need to share information to work as a team!"
    },
    {
      text: "Learn what ROS2 does (it's like a robot's nervous system)",
      icon: "Brain"
    },
    {
      text: "See how real robots use these ideas",
      icon: "Bot"
    }
  ]}
  displayStyle="cards"
  colorTheme="primary"
/>
```

#### Entity 3: "Doubtful Questions and Answers" Component

```typescript
interface DoubtfulQAProps {
  questions: ConfusionPoint[];
  allowExpand?: boolean;          // Collapsible accordion style?
  showCategory?: boolean;         // Show confusion type label?
}

interface ConfusionPoint {
  id: string;
  question: string;               // Phrased as student would ask
  answer: string;                 // Clear, simple explanation
  category: 'terminology' | 'why-vs-how' | 'scope' | 'sim-vs-real' | 'abstract';
  misconception_addressed: string; // What wrong idea does this fix?
  follow_up_questions?: string[]; // Optional deeper dive
  visual_aid?: string;            // Link to diagram/image
}

// Usage Example:
<DoubtfulQA
  questions={[
    {
      id: "middleware-vs-direct",
      question: "Why can't robot parts just talk directly to each other instead of using middleware?",
      answer: "Great question! Imagine if every student in your school had to remember the phone number of every other student to share homework. That would be really hard! Middleware is like having a class announcement system - you just say your message once, and everyone who wants to hear it can listen. It's much easier than calling everyone separately!",
      category: "why-vs-how",
      misconception_addressed: "Middleware is unnecessary overhead",
      visual_aid: "/img/middleware-analogy-school-announcements.svg"
    },
    {
      id: "ros-vs-operating-system",
      question: "Is ROS2 an operating system like Windows?",
      answer: "Nope! Even though it's called 'Robot Operating System,' ROS2 is actually more like a set of tools that runs ON TOP of an operating system (like Windows or Linux). Think of it this way: If Linux is like the foundation and walls of a house, ROS2 is like the furniture and appliances inside that make the house useful. You need both!",
      category: "terminology",
      misconception_addressed: "ROS2 is an OS replacement"
    }
  ]}
  allowExpand={true}
  showCategory={false}
/>
```

#### Entity 4: "Grown-Up Words" Glossary Component

```typescript
interface GrownUpWordsProps {
  terms: TechnicalTermMapping[];
  displayStyle?: 'table' | 'cards' | 'inline';
  expandable?: boolean;
}

interface TechnicalTermMapping {
  simple_term: string;            // Child-friendly phrase
  technical_term: string;         // Actual technical term
  context_example: string;        // Sentence showing technical term in use
  why_technical_term_exists?: string; // Optional explanation
}

// Usage Example:
<GrownUpWords
  terms={[
    {
      simple_term: "Robot's language",
      technical_term: "ROS2",
      context_example: "The engineer said: 'We use ROS2 to coordinate the robot's movements.'",
      why_technical_term_exists: "ROS2 stands for Robot Operating System 2 - it's a shorter way to say 'the system that helps robot parts communicate.'"
    },
    {
      simple_term: "Robot's brain",
      technical_term: "Processor (CPU)",
      context_example: "The humanoid robot has a powerful Jetson processor to run AI models.",
    },
    {
      simple_term: "Announcement channel",
      technical_term: "Topic",
      context_example: "The camera publishes images to the /camera/image topic."
    }
  ]}
  displayStyle="table"
  expandable={false}
/>
```

#### Entity 5: Plain-Language Code Annotation

```typescript
interface CodeBlockWithExplanation {
  code: string;                   // The actual code
  language: string;               // Syntax highlighting
  explanation: {
    what_it_does: string;         // High-level summary (1-2 sentences)
    step_by_step?: CodeStep[];    // Optional detailed breakdown
    why_we_need_this?: string;    // Context/motivation
    real_world_analogy?: string;  // Relatable comparison
  };
}

interface CodeStep {
  line_numbers: number[];         // Which lines this explains
  simple_description: string;     // What this part does
  grows_up_to?: string;          // Technical term for this concept
}

// Usage Example:
<CodeBlockWithExplanation
  code={`
import rclpy
from rclpy.node import Node

class HelloRobot(Node):
    def __init__(self):
        super().__init__('hello_node')
        self.get_logger().info('Hello, Robot World!')

def main():
    rclpy.init()
    node = HelloRobot()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
  `}
  language="python"
  explanation={{
    what_it_does: "This code creates a simple robot program that says 'Hello, Robot World!' when it starts running. It's like teaching your robot to introduce itself!",
    step_by_step: [
      {
        line_numbers: [1, 2],
        simple_description: "Import the tools we need to talk to ROS2",
        technical_term: "Import statements"
      },
      {
        line_numbers: [4, 5, 6],
        simple_description: "Create our robot program and give it a name ('hello_node'). Then tell it to print a greeting message.",
        technical_term: "Node class definition"
      },
      {
        line_numbers: [8, 9, 10, 11, 12],
        simple_description: "Start up ROS2, run our greeting program, and then shut everything down nicely when we're done.",
        technical_term: "Main execution loop"
      }
    ],
    real_world_analogy: "This is like writing a script for a play: first you set the stage (import tools), then you define what the actor does (HelloRobot class), and finally you perform the play (main function)."
  }}
/>
```

### Design Task 2: Component API Contracts

**Directory**: `contracts/`

#### Contract 1: WhatYouWillLearn Component API

**File**: `contracts/WhatYouWillLearn.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "WhatYouWillLearn Component Props",
  "type": "object",
  "required": ["goals"],
  "properties": {
    "goals": {
      "type": "array",
      "minItems": 3,
      "maxItems": 5,
      "items": {
        "type": "object",
        "required": ["text"],
        "properties": {
          "text": {
            "type": "string",
            "maxLength": 100,
            "description": "Learning goal in simple, friendly language"
          },
          "icon": {
            "type": "string",
            "description": "Lucide icon name (optional)"
          },
          "why_it_matters": {
            "type": "string",
            "maxLength": 200,
            "description": "Optional explanation of relevance"
          }
        }
      }
    },
    "displayStyle": {
      "type": "string",
      "enum": ["bullets", "cards", "numbered"],
      "default": "bullets"
    },
    "colorTheme": {
      "type": "string",
      "enum": ["primary", "success", "info"],
      "default": "primary"
    }
  }
}
```

#### Contract 2: DoubtfulQA Component API

**File**: `contracts/DoubtfulQA.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "DoubtfulQA Component Props",
  "type": "object",
  "required": ["questions"],
  "properties": {
    "questions": {
      "type": "array",
      "minItems": 5,
      "maxItems": 8,
      "description": "5-8 confusion points per lesson section",
      "items": {
        "type": "object",
        "required": ["id", "question", "answer", "category", "misconception_addressed"],
        "properties": {
          "id": {
            "type": "string",
            "pattern": "^[a-z0-9-]+$"
          },
          "question": {
            "type": "string",
            "maxLength": 200,
            "description": "Question as student would phrase it"
          },
          "answer": {
            "type": "string",
            "maxLength": 500,
            "description": "Clear, simple answer with analogy if helpful"
          },
          "category": {
            "type": "string",
            "enum": ["terminology", "why-vs-how", "scope", "sim-vs-real", "abstract"]
          },
          "misconception_addressed": {
            "type": "string",
            "maxLength": 150,
            "description": "What wrong belief does this question reveal?"
          },
          "follow_up_questions": {
            "type": "array",
            "items": { "type": "string" }
          },
          "visual_aid": {
            "type": "string",
            "format": "uri-reference"
          }
        }
      }
    },
    "allowExpand": {
      "type": "boolean",
      "default": true
    },
    "showCategory": {
      "type": "boolean",
      "default": false
    }
  }
}
```

#### Contract 3: GrownUpWords Component API

**File**: `contracts/GrownUpWords.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "GrownUpWords Component Props",
  "type": "object",
  "required": ["terms"],
  "properties": {
    "terms": {
      "type": "array",
      "minItems": 5,
      "items": {
        "type": "object",
        "required": ["simple_term", "technical_term", "context_example"],
        "properties": {
          "simple_term": {
            "type": "string",
            "maxLength": 50
          },
          "technical_term": {
            "type": "string",
            "maxLength": 50
          },
          "context_example": {
            "type": "string",
            "maxLength": 200,
            "description": "Sentence showing technical term in real use"
          },
          "why_technical_term_exists": {
            "type": "string",
            "maxLength": 150
          }
        }
      }
    },
    "displayStyle": {
      "type": "string",
      "enum": ["table", "cards", "inline"],
      "default": "table"
    },
    "expandable": {
      "type": "boolean",
      "default": false
    }
  }
}
```

#### Contract 4: Simplification Guidelines (Prose)

**File**: `contracts/SimplificationGuidelines.md`

```markdown
# Content Simplification Guidelines

## Reading Level Targets
- **Flesch-Kincaid Grade Level**: 3.0 - 6.0
- **Flesch Reading Ease**: 70 - 80 (Fairly Easy to Easy)
- **Average Sentence Length**: 12-15 words
- **Average Word Length**: 1.5-2.0 syllables

## Sentence Structure Rules
1. Use active voice (80%+ of sentences)
2. One idea per sentence
3. Maximum sentence length: 20 words
4. Avoid subordinate clauses when possible
5. Start sentences with subjects, not prepositional phrases

## Vocabulary Guidelines
### Approved Simple Replacements
- "use" instead of "utilize"
- "show" instead of "demonstrate"
- "help" instead of "facilitate"
- "make" instead of "generate"
- "part" instead of "component" (when appropriate)

### Technical Terms That MUST Be Used
(These appear in "Grown-Up Words" glossary)
- ROS2 (always explain as "Robot Operating System")
- Node (after first introduction with analogy)
- Topic (after first introduction with analogy)
- Sensor (common word, keep it)
- Simulation (explain with comparison to video games)

### Forbidden Jargon
- Architecture (use "design" or "structure")
- Infrastructure (use "foundation" or "system")
- Paradigm (use "approach" or "way of doing things")
- Middleware (use "connection system" then introduce technical term)
- Synchronous/Asynchronous (use "waits for answer" vs "doesn't wait")

## Analogy Quality Standards
Every analogy must:
1. Use experiences familiar to 8-12 year olds
2. Map accurately to the technical concept
3. Include a "but it's different because..." clause if major differences exist
4. Be tested for potential misconceptions

## Real-World Example Domains (Preferred)
- School/classroom activities
- Sports and games
- Family/home activities
- Nature/animals
- Popular media (appropriate references)
```

### Design Task 3: Quickstart Guide

**File**: `quickstart.md`

```markdown
# Quickstart Guide: Simplifying Chapter Content

## For Content Writers

### Step 1: Read Original Chapter
Understand the technical concepts thoroughly before simplifying.

### Step 2: Add "What You Will Learn"
At the top of the chapter (after frontmatter), add:

\`\`\`mdx
<WhatYouWillLearn
  goals={[
    { text: "[Simple statement of goal 1]", icon: "[IconName]" },
    { text: "[Simple statement of goal 2]", icon: "[IconName]" },
    { text: "[Simple statement of goal 3]", icon: "[IconName]" }
  ]}
  displayStyle="cards"
/>
\`\`\`

**Rules**:
- 3-5 goals maximum
- Each goal max 100 characters
- Use conversational language ("Understand how..." not "Understanding of...")

### Step 3: Simplify Each Section
For each section heading:

1. **Rewrite text** following SimplificationGuidelines.md
2. **Add 1-2 analogies** from Analogy-Bank.md
3. **Check readability** with analyze-readability.js script
4. **Identify 5-8 confusion points** likely for that section

### Step 4: Add "Doubtful Questions and Answers"
After each major concept section, add:

\`\`\`mdx
<DoubtfulQA
  questions={[
    {
      id: "[unique-id]",
      question: "[As student would ask]",
      answer: "[Clear explanation with analogy]",
      category: "[terminology|why-vs-how|scope|sim-vs-real|abstract]",
      misconception_addressed: "[What wrong idea this fixes]"
    },
    // ... 4-7 more questions
  ]}
/>
\`\`\`

**Use Question-Templates.md** for inspiration.

### Step 5: Add "Grown-Up Words" Glossary
At the end of the chapter, before exercises:

\`\`\`mdx
<GrownUpWords
  terms={[
    {
      simple_term: "[Child-friendly phrase]",
      technical_term: "[Actual term]",
      context_example: "[Sentence with technical term]"
    },
    // ... 5-10 more terms
  ]}
/>
\`\`\`

### Step 6: Annotate Code Blocks
Replace plain code blocks with:

\`\`\`mdx
<CodeBlockWithExplanation
  code={\`...\`}
  language="python"
  explanation={{
    what_it_does: "[1-2 sentence summary]",
    step_by_step: [
      { line_numbers: [1,2], simple_description: "[What these lines do]" },
      // ...
    ],
    real_world_analogy: "[Relatable comparison]"
  }}
/>
\`\`\`

### Step 7: Validate
Run these checks before submitting:

\`\`\`bash
# Check readability metrics
node scripts/simplify-content/analyze-readability.js docs/module1/.../chapter.mdx

# Validate technical accuracy (requires human review)
node scripts/simplify-content/validate-accuracy.js docs/module1/.../chapter.mdx

# Check component schemas
node scripts/simplify-content/validate-components.js docs/module1/.../chapter.mdx
\`\`\`

## For Reviewers

### Technical Accuracy Checklist
- [ ] All simplified explanations preserve original meaning
- [ ] Analogies accurately represent concepts
- [ ] No new incorrect information introduced
- [ ] Technical terms used correctly
- [ ] Code examples still valid

### Age-Appropriateness Checklist
- [ ] Reading level 3-6 (Flesch-Kincaid)
- [ ] Analogies relatable to 8-12 year olds
- [ ] No overly childish language (avoid "super duper", excessive exclamation marks)
- [ ] Respects intelligence of readers

### Completeness Checklist
- [ ] "What You Will Learn" present at top
- [ ] All sections simplified
- [ ] 5-8 Q&As per major concept
- [ ] "Grown-Up Words" glossary at end
- [ ] All code blocks annotated
- [ ] Existing components (LearningGoals, KeyTakeaways) updated if needed
```

---

## Agent Context Update

*Note: This section will be executed after contract creation by running:*
`.specify/scripts/powershell/update-agent-context.ps1 -AgentType claude`

**Technologies to add to agent context**:
- Flesch-Kincaid readability metrics
- Child-friendly content design patterns (ages 8-12)
- Educational Q&A component design
- Technical glossary best practices
- Code annotation for non-programmers
- MDX component composition in Docusaurus

---

## Architectural Decisions

### ADR Candidates

Based on the planning work, the following architectural decisions may warrant formal ADRs (pending user approval):

1. **Component-Based Content Enhancement vs Full Rewrite**
   - **Decision**: Use React components embedded in MDX rather than completely rewriting markdown files
   - **Rationale**: Preserves existing content, allows gradual rollout, enables A/B testing
   - **Trade-offs**: Slightly more complex authoring vs complete content replacement
   - **Suggest documenting with**: `/sp.adr component-based-simplification`

2. **Inline Q&A vs Separate FAQ Pages**
   - **Decision**: Embed "Doubtful Questions and Answers" inline within chapters rather than separate FAQ section
   - **Rationale**: Contextual help at point of confusion reduces cognitive load
   - **Trade-offs**: Longer pages vs separate navigation
   - **Suggest documenting with**: `/sp.adr inline-qa-placement`

3. **Reading Level Target (Grades 3-6)**
   - **Decision**: Target Flesch-Kincaid Grade 3-6 rather than literal 5-year-old level
   - **Rationale**: User request for "5-year-old understanding" interpreted as very simple language; grades 3-6 balances simplicity with technical concept preservation
   - **Trade-offs**: May still be challenging for younger readers vs risk of being overly simplistic
   - **Suggest documenting with**: `/sp.adr reading-level-target`

### Recommendation
📋 **Architectural decisions detected:**
- Component-based content enhancement strategy
- Inline Q&A placement approach
- Reading level target calibration (grades 3-6)

**Document reasoning and trade-offs?** Run `/sp.adr content-simplification-architecture` to create a consolidated ADR for these decisions.

---

## Next Steps

1. **Phase 0 Complete**: Generate `research.md` with:
   - Simplification guidelines with reading level targets
   - Analogy bank with 50+ tested real-life comparisons
   - Question templates for 5 confusion categories
   - Code annotation strategy
   - Glossary structure

2. **Phase 1 Complete**: Generate:
   - `data-model.md` (component schemas)
   - `contracts/` directory (JSON schemas + guidelines)
   - `quickstart.md` (writer/reviewer guide)
   - Run agent context update script

3. **Ready for `/sp.tasks`**: After Phase 1, run `/sp.tasks` to generate task breakdown for:
   - Component development (WhatYouWillLearn, DoubtfulQA, GrownUpWords)
   - Content scripts (readability, accuracy validation)
   - Chapter-by-chapter simplification (19 chapters)
   - Testing and validation

---

**Plan Status**: ✅ Ready for Phase 0 research execution
**Branch**: 001-simplified-content
**Next Command**: Begin research phase or run `/sp.tasks` after manual research completion
