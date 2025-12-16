# Teaching Physical AI & Humanoid Robotics Course

[![Docusaurus](https://img.shields.io/badge/Built%20with-Docusaurus-3ECC5F.svg)](https://docusaurus.io/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-222222.svg)](https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/)

> A comprehensive, AI-native educational platform for teaching Physical AI and Humanoid Robotics using modern spec-driven development methodologies.

## 🎯 Project Overview

This project is an interactive, Docusaurus-based coursebook that teaches students how to build intelligent, autonomous humanoid robots using cutting-edge Physical AI technologies. The course covers everything from foundational robot control systems (ROS 2) to advanced Vision-Language-Action (VLA) systems powered by Large Language Models.

**Live Course**: [https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/](https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/)

### What Makes This Project Unique

This isn't just a course - it's a **living demonstration of AI-assisted educational content creation** using:

- **Spec-Driven Development (SDD)**: Every feature is formally specified, planned, and tracked
- **Reusable AI Intelligence**: Custom agents, skills, and automation built specifically for this project
- **Constitutional AI Governance**: AI behavior governed by a formal constitution ensuring deterministic, reproducible outputs
- **Child-Friendly Learning**: Advanced content simplified for 8-12 year olds using AI-powered readability analysis

## 📚 Course Structure

### Module 1: The Robotic Nervous System (ROS 2)
Learn the foundational middleware for robot communication - nodes, topics, services, URDF modeling, and Python integration via rclpy.

### Module 2: The Digital Twin (Gazebo & Unity)
Master physics simulation and photorealistic rendering for safe robot development and synthetic data generation.

### Module 3: The AI-Robot Brain (NVIDIA Isaac)
Discover GPU-accelerated perception, Visual SLAM, and autonomous navigation using NVIDIA Isaac Sim and Isaac ROS.

### Module 4: Vision-Language-Action (VLA)
Build robots that understand natural language commands and execute multi-step tasks using LLMs (GPT-4, Claude).

## 🤖 Reusable Intelligence Components

This project demonstrates advanced AI-assisted development through purpose-built agents and automation:

### Custom Slash Commands (AI Agents)

Located in `.claude/commands/`, these specialized agents automate complex workflows:

#### 1. `/generate-module-content`
**The Educational Content Generator**
- **Purpose**: Automatically generates complete module content from PDF source materials
- **Intelligence**:
  - Parses PDF textbooks and extracts relevant educational content
  - Generates 5 chapters per module with proper MDX formatting
  - Creates interactive exercises with progressive hints
  - Validates frontmatter schemas and builds
  - Ensures pedagogical quality and technical accuracy
- **Reusability**: Can be adapted for any educational content generation workflow
- **Files**: `.claude/commands/generate-module-content.md`

#### 2. Spec-Driven Development Commands
Complete workflow automation for feature development:

- **/sp.specify** - Create feature specifications from natural language
- **/sp.plan** - Generate architectural plans and technical designs
- **/sp.tasks** - Break down features into dependency-ordered tasks
- **/sp.implement** - Execute implementation from task lists
- **/sp.clarify** - Identify underspecified areas and ask targeted questions
- **/sp.analyze** - Cross-artifact consistency analysis
- **/sp.adr** - Generate Architectural Decision Records
- **/sp.phr** - Create Prompt History Records for AI traceability
- **/sp.git.commit_pr** - Autonomous git workflows and PR creation
- **/sp.constitution** - Manage project constitution and principles

**Reusability**: These commands form a complete **SpecKit Plus** workflow system that can be ported to any software project requiring rigorous specification, planning, and tracking.

### Content Simplification Scripts

Located in `scripts/simplify-content/`, these tools enable child-friendly content creation:

#### 1. `analyze-readability.js`
- **Purpose**: Analyzes MDX files for readability metrics (Flesch-Kincaid Grade Level, Reading Ease)
- **Target**: Grade 3-6 content, Reading Ease 70-80
- **Intelligence**:
  - Strips MDX components and code blocks for pure text analysis
  - Calculates multiple readability metrics
  - Identifies content that's too complex
- **Reusability**: Adaptable for any content requiring readability validation

#### 2. `extract-technical-terms.js`
- **Purpose**: Identifies technical jargon and creates "Grown-Up Words" glossaries
- **Intelligence**: Maps simplified language to technical terminology for learning transitions

#### 3. `add-components-batch.js` & `validate-components.js`
- **Purpose**: Batch processing of MDX components and validation
- **Intelligence**: Ensures consistent use of custom learning components across all chapters

### SpecKit Constitution System

The project operates under a formal **Constitution** (`.specify/memory/constitution.md`) that governs:

- **Deterministic AI Behavior**: Identical inputs produce identical outputs
- **Anti-Hallucination Mandate**: AI cannot invent content; all outputs traced to source materials
- **Human-in-the-Loop**: Explicit approval required for critical decisions
- **Reproducibility**: Entire development process is reproducible
- **Composability**: All components are modular and reusable

### Prompt History Record (PHR) System

Every AI interaction is documented in `history/prompts/` with:
- Full user prompt (verbatim)
- AI response
- Feature context
- Files modified
- Timestamp and metadata

**Reusability**: This creates a complete audit trail and knowledge base for future AI training and project archaeology.

### Architectural Decision Records (ADR)

Significant technical decisions are documented in `history/adr/` following a structured format:
- Context and problem statement
- Decision drivers
- Options considered
- Decision outcome
- Consequences (positive/negative)

**Reusability**: Standard ADR format used by software industry for technical documentation.

## 🚀 Getting Started

### Prerequisites

- **Node.js** 20.0 or higher
- **npm** or **yarn**
- **Git**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/salmanpatnee/Physical-AI-Humanoid-Robotics.git
   cd Physical-AI-Humanoid-Robotics
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

### Development

Start the local development server:

```bash
npm start
# or
yarn start
```

This opens `http://localhost:3000` with hot reloading.

### Build

Generate static content for production:

```bash
npm run build
# or
yarn build
```

Output is in the `build/` directory.

### Testing

Run accessibility contrast tests:

```bash
npm run test:contrast
```

## 📁 Project Structure

```
Physical-AI-Humanoid-Robotics/
├── .claude/
│   └── commands/           # Custom AI agent commands
│       ├── generate-module-content.md
│       ├── sp.specify.md
│       ├── sp.plan.md
│       └── ... (12 total commands)
├── .specify/
│   ├── memory/
│   │   └── constitution.md # Project governance rules
│   ├── templates/          # Spec, plan, task templates
│   └── scripts/            # Automation scripts
├── docs/                   # Course content (MDX files)
│   ├── module1-robotic-nervous-system/
│   ├── module2-the-digital-twin/
│   ├── module3-ai-robot-brain/
│   └── module4-vision-language-action/
├── specs/                  # Feature specifications
│   ├── 001-simplified-content/
│   ├── 004-module1-ros2/
│   └── ... (14 feature specs)
├── scripts/
│   └── simplify-content/   # Readability & content analysis
│       ├── analyze-readability.js
│       ├── extract-technical-terms.js
│       └── validate-components.js
├── history/
│   ├── prompts/            # Prompt History Records (PHR)
│   └── adr/                # Architectural Decision Records
├── src/
│   └── components/         # Custom React/MDX components
├── docusaurus.config.ts    # Site configuration
├── sidebars.ts             # Documentation sidebar
└── package.json
```

## 🛠️ Technology Stack

### Core Technologies
- **Docusaurus 3.9.2** - Modern static site generator
- **React 19** - UI components and interactivity
- **TypeScript** - Type-safe development
- **MDX** - Markdown with JSX components

### Educational Tools
- **Custom MDX Components**:
  - `<LearningGoals />` - Chapter objectives
  - `<KeyTakeaways />` - Summary of concepts
  - `<Prerequisites />` - Required knowledge
  - `<ExerciseBlock />` - Interactive exercises with hints and solutions
  - `<WhatYouWillLearn />` - Child-friendly summaries
  - `<DoubtfulQA />` - Common confusion points addressed

### Development Tools
- **Playwright** - Accessibility testing
- **text-readability** - Flesch-Kincaid readability analysis
- **Lucide React** - Icon library
- **GitHub Actions** - CI/CD pipeline

### AI & Automation
- **Claude Code** - AI-assisted development with custom commands
- **SpecKit Plus** - Spec-driven development methodology
- **Constitutional AI** - Governed AI behavior

## 📖 Using the Reusable Intelligence

### For Educational Content Creation

To generate a new module from a PDF textbook:

```bash
/generate-module-content --feature 007-module4-vla --source doc/textbook.pdf --module-number 4 --module-name "Vision-Language-Action"
```

This will:
1. Extract content from the PDF
2. Generate 5 chapters with proper MDX formatting
3. Create exercises and interactive components
4. Validate frontmatter and build
5. Update sidebar configuration
6. Create a Prompt History Record

### For Spec-Driven Development

1. **Create a feature specification**:
   ```bash
   /sp.specify Add interactive quizzes with scoring system
   ```

2. **Generate an architectural plan**:
   ```bash
   /sp.plan
   ```

3. **Create implementation tasks**:
   ```bash
   /sp.tasks
   ```

4. **Execute implementation**:
   ```bash
   /sp.implement
   ```

5. **Commit and create PR**:
   ```bash
   /sp.git.commit_pr
   ```

### For Content Readability Analysis

```bash
node scripts/simplify-content/analyze-readability.js docs/module1-robotic-nervous-system/01-focus-middleware-for-robot-control.mdx
```

## 🎓 Learning from This Project

### For Educators
- **Reuse the module structure** for any technical course
- **Adapt the MDX components** for interactive learning
- **Apply the simplification methodology** for younger audiences

### For Developers
- **Port the SpecKit Plus system** to your projects for rigorous specification
- **Use the PHR system** for AI interaction documentation
- **Adopt the Constitution pattern** for governed AI behavior

### For AI Researchers
- **Study the anti-hallucination techniques** in educational content generation
- **Analyze the Constitutional AI approach** to constrained agent behavior
- **Examine the Human-as-Tool strategy** for collaborative AI workflows

## 🤝 Contributing

We welcome contributions! This project demonstrates advanced AI-assisted development patterns that can benefit the broader community.

### Areas for Contribution
1. **Additional Module Content** - Expand the course with new topics
2. **Interactive Components** - Build new MDX components for learning
3. **Reusable Skills** - Create new automation scripts
4. **Accessibility** - Improve A11y compliance
5. **Translations** - Make the course multilingual

### Contribution Workflow
1. Fork the repository
2. Create a feature branch using the SpecKit workflow (`/sp.specify`)
3. Follow the constitution guidelines
4. Submit a Pull Request with ADRs for significant decisions

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- **ROS 2 Community** - For the incredible robotics middleware
- **NVIDIA Isaac Team** - For GPU-accelerated robotics tools
- **Docusaurus Team** - For the amazing documentation framework
- **Anthropic** - For Claude and Constitutional AI principles

## 📞 Contact & Support

- **Live Course**: [https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/](https://salmanpatnee.github.io/Physical-AI-Humanoid-Robotics/)
- **Issues**: [GitHub Issues](https://github.com/salmanpatnee/Physical-AI-Humanoid-Robotics/issues)
- **Discussions**: [GitHub Discussions](https://github.com/salmanpatnee/Physical-AI-Humanoid-Robotics/discussions)

---

**Built with AI-Native Development Methodologies** | **Governed by Constitutional AI** | **Powered by SpecKit Plus**
