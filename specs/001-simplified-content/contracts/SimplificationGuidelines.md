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
- "build" instead of "construct"
- "test" instead of "validate"
- "run" instead of "execute"

### Technical Terms That MUST Be Used
(These appear in "Grown-Up Words" glossary)
- ROS2 (always explain as "Robot Operating System")
- Node (after first introduction with analogy)
- Topic (after first introduction with analogy)
- Sensor (common word, keep it)
- Simulation (explain with comparison to video games)
- URDF (introduce as "robot blueprint language")
- Gazebo (introduce as "robot practice world")
- Isaac Sim (introduce as "NVIDIA's robot training world")

### Forbidden Jargon
Replace with simpler alternatives:
- "Architecture" → use "design" or "structure"
- "Infrastructure" → use "foundation" or "system"
- "Paradigm" → use "approach" or "way of doing things"
- "Middleware" → use "connection system" then introduce technical term
- "Synchronous/Asynchronous" → use "waits for answer" vs "doesn't wait"
- "Implement" → use "build" or "create"
- "Instantiate" → use "create"
- "Invoke" → use "call" or "use"
- "Leverage" → use "use"
- "Paradigm shift" → use "big change"

## Analogy Quality Standards
Every analogy must:
1. Use experiences familiar to 8-12 year olds
2. Map accurately to the technical concept
3. Include a "but it's different because..." clause if major differences exist
4. Be tested for potential misconceptions

## Real-World Example Domains (Preferred)
- **School/classroom activities**: group projects, announcements, class schedules
- **Sports and games**: team sports, video games, board games, playground activities
- **Family/home activities**: cooking, cleaning, organizing, home projects
- **Nature/animals**: animal communication, ecosystems, bird migration
- **Popular media**: age-appropriate movie/book references, common apps/tech

## Core Analogy Bank

### ROS2 Concepts

| Technical Term | Simple Analogy | Explanation |
|----------------|----------------|-------------|
| ROS2 Topics | Walkie-talkie channels | Just like walkie-talkies have different channels (channel 1, 2, 3), ROS2 topics are different channels where robot parts can talk to each other |
| ROS2 Node | Worker in a factory | Each node is like a worker with a specific job - one might watch the camera, another moves the arm |
| Middleware | School bus system | Instead of every student needing a car to get to school, the bus system connects everyone. ROS2 connects all robot parts the same way |
| Publisher | Classroom speaker | Like when the teacher makes an announcement over the speaker - everyone listening can hear it |
| Subscriber | Student listening | Like students listening to classroom announcements - they hear what's being said |
| Service | Asking teacher a question | You ask a question and wait for an answer before moving on |

### Simulation Concepts

| Technical Term | Simple Analogy | Explanation |
|----------------|----------------|-------------|
| Gazebo Simulation | Flight simulator game | Pilots practice in flight simulators before flying real planes. Robots practice in Gazebo before doing real tasks |
| Physics Engine | Video game rules | Just like how video games have rules for gravity and collisions, Gazebo has rules for how robots move |
| Sensor Simulation | Practice sensors | Like using a toy thermometer to practice reading temperatures before using a real one |

### AI/Perception Concepts

| Technical Term | Simple Analogy | Explanation |
|----------------|----------------|-------------|
| VSLAM (Visual Mapping) | Drawing a map while exploring | Like when you walk through a new place and draw a map as you go, the robot does the same with its camera |
| GPU Acceleration | 100 helpers instead of 1 | Instead of one person doing all the work, 100 people work together to finish faster |
| Computer Vision | Robot's eyes | The camera and computer work together like your eyes and brain to see and understand things |
| Path Planning | Google Maps for robots | Like how Google Maps finds the best route from home to school, path planning finds the best route for the robot |

## Code Annotation Strategy

### For Python Code
- Use "What This Code Does" summaries before code blocks
- Explain each section (not line-by-line unless critical)
- Use comments that explain WHY, not WHAT
- Relate code concepts to real-world actions

Example:
```python
# What This Code Does:
# This code creates a simple robot program that says "Hello!" when it starts.
# Think of it like writing a script for a play - you're telling the robot what to do!

import rclpy  # Import the tools to talk to ROS2 (like getting your art supplies)
from rclpy.node import Node  # Import the Node class (like getting a template to follow)

class HelloRobot(Node):  # Create our robot program (like naming your character)
    def __init__(self):
        super().__init__('hello_node')  # Give it a name: 'hello_node'
        self.get_logger().info('Hello, Robot World!')  # Make it say hello!
```

### For XML/URDF Files
- Explain what URDF is (blueprint for robot structure)
- Use visual metaphors (LEGO instructions, building blocks)
- Focus on what each part represents physically

### For Command-Line Instructions
- Explain what each command does in plain English
- Use "This command..." format
- Provide expected outcomes

Example:
```bash
# This command starts the robot simulation
ros2 launch my_robot simulation.launch.py

# What happens: A virtual robot appears on your screen, ready to practice!
```

## Paragraph Structure

### Opening Paragraphs
- Start with a question or relatable scenario
- Hook the reader's interest immediately
- Connect to prior knowledge

Good example:
> "Have you ever wondered how robots know where they are? Imagine you're playing hide-and-seek in a huge building. You'd need to remember where you've been and create a mental map, right? Robots do the same thing using something called VSLAM!"

### Body Paragraphs
- Maximum 3-4 sentences per paragraph
- One main idea per paragraph
- Include an example or analogy
- Use transition words (first, next, then, finally)

### Conclusion Sentences
- Summarize the key point
- Connect to the next topic or real-world application

## Common Misconceptions to Address

### Misconception 1: "Simulation is just for fun, like a game"
**Reality**: Simulation is practice for real robots. It's like how pilots use flight simulators - it's serious training, not just a game.

### Misconception 2: "ROS2 is an operating system like Windows"
**Reality**: ROS2 is more like a toolbox that runs ON TOP of an operating system. It helps robot parts talk to each other.

### Misconception 3: "Robots think like humans"
**Reality**: Robots follow instructions (code) very precisely. They don't "think" on their own - they do exactly what we program them to do.

### Misconception 4: "If it works in simulation, it will work perfectly on a real robot"
**Reality**: Simulation is practice, but real robots face challenges simulation can't fully copy (like battery life, real-world friction, and unexpected obstacles).

## Writing Style Guidelines

### Voice and Tone
- Conversational and friendly (use "you" and "we")
- Encouraging and positive
- Curious and exploratory
- Respectful of reader's intelligence (avoid being condescending)

### Things to AVOID
- Excessive exclamation marks (max 1 per paragraph)
- Overly childish language ("super duper", "yay!")
- Talking down to readers
- Assuming no prior knowledge (build on what they know)
- Long, complex sentences
- Abstract concepts without concrete examples

### Things to INCLUDE
- Questions that engage the reader
- "Think about it" moments
- Real-world connections
- Step-by-step explanations
- Visual descriptions
- Encouraging language ("You can do this!")

## Validation Checklist

Before finalizing simplified content, check:
- [ ] Flesch-Kincaid grade level between 3-6
- [ ] At least 80% active voice
- [ ] No sentences longer than 20 words
- [ ] All technical terms introduced with analogies
- [ ] At least one real-world example per major concept
- [ ] Short paragraphs (3-4 sentences max)
- [ ] No forbidden jargon without explanation
- [ ] Analogies are age-appropriate
- [ ] Technical accuracy preserved (no misconceptions introduced)
- [ ] Engaging and respectful tone throughout
