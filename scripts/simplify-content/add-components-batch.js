#!/usr/bin/env node

/**
 * Batch Add Components Script
 * Adds WhatYouWillLearn, DoubtfulQA, and GrownUpWords to all chapter files
 */

const fs = require('fs');
const path = require('path');
const { extractTerms, knownTerms } = require('./extract-technical-terms.js');

const chapters = [
  'docs/module1-robotic-nervous-system/02-ros2-nodes-topics-services.mdx',
  'docs/module1-robotic-nervous-system/03-bridging-python-agents-with-rclpy.mdx',
  'docs/module1-robotic-nervous-system/04-understanding-urdf.mdx',
  'docs/module1-robotic-nervous-system/05-managing-complex-systems-with-launch-files.mdx',
  'docs/module2-the-digital-twin/01-focus-physics-simulation-and-world-building.mdx',
  'docs/module2-the-digital-twin/02-simulating-collisions-gravity-and-sensors-in-gazebo.mdx',
  'docs/module2-the-digital-twin/03-high-fidelity-rendering-and-interaction-scenes-in-unity.mdx',
  'docs/module2-the-digital-twin/04-sensor-simulation-lidar-depth-cameras-and-imus.mdx',
  'docs/module3-ai-robot-brain/01-focus-advanced-perception-and-synthetic-data.mdx',
  'docs/module3-ai-robot-brain/02-isaac-sim-for-photorealistic-simulation-and-training.mdx',
  'docs/module3-ai-robot-brain/03-isaac-ros-for-gpu-accelerated-vslam-and-navigation.mdx',
  'docs/module3-ai-robot-brain/04-nav2-for-humanoid-path-planning-and-locomotion.mdx',
  'docs/module4-vision-language-action/01-focus-the-convergence-of-llms-and-robotics.mdx',
  'docs/module4-vision-language-action/02-voice-to-action-using-whisper.mdx',
  'docs/module4-vision-language-action/03-cognitive-planning-using-llms-for-ros2-task-decomposition.mdx',
  'docs/module4-vision-language-action/04-capstone-the-autonomous-humanoid.mdx'
];

function addWhatYouWillLearn(content, learning_goals) {
  // Check if WhatYouWillLearn already exists
  if (content.includes('<WhatYouWillLearn')) {
    return content;
  }

  // Find the first heading after frontmatter
  const lines = content.split('\n');
  let insertIndex = -1;
  let inFrontmatter = false;

  for (let i = 0; i < lines.length; i++) {
    if (lines[i].trim() === '---') {
      if (!inFrontmatter) {
        inFrontmatter = true;
      } else {
        inFrontmatter = false;
        // Find next heading
        for (let j = i + 1; j < lines.length; j++) {
          if (lines[j].startsWith('# ')) {
            insertIndex = j + 1;
            break;
          }
        }
        break;
      }
    }
  }

  if (insertIndex === -1) return content;

  const goals = learning_goals.slice(0, 4).map((goal, idx) => {
    const icons = ['Target', 'Lightbulb', 'Rocket', 'CheckCircle2'];
    return `    {
      text: "${goal.replace(/"/g, '\\"')}",
      icon: "${icons[idx]}",
      why_it_matters: "This is important for building real robots!"
    }`;
  }).join(',\n');

  const component = `
<WhatYouWillLearn
  goals={[
${goals}
  ]}
  displayStyle="cards"
/>
`;

  lines.splice(insertIndex, 0, component);
  return lines.join('\n');
}

function addGrownUpWords(content, terms) {
  // Check if GrownUpWords already exists
  if (content.includes('<GrownUpWords')) {
    return content;
  }

  // Add before "Next Steps" or at the end
  const termsList = Array.from(terms.entries())
    .slice(0, 8)
    .map(([term, info]) => {
      return `    {
      simple_term: "${info.simple}",
      technical_term: "${term}",
      context_example: "This chapter discusses ${term} in detail."
    }`;
    }).join(',\n');

  const component = `
## Technical Terms Glossary

<GrownUpWords
  terms={[
${termsList}
  ]}
  displayStyle="table"
/>
`;

  // Find "Next Steps" or "## Next" or add before last heading
  let insertPos = content.lastIndexOf('## Next');
  if (insertPos === -1) {
    insertPos = content.lastIndexOf('\n## ');
  }
  if (insertPos === -1) {
    // Add at end
    return content + '\n' + component;
  }

  return content.substring(0, insertPos) + component + '\n' + content.substring(insertPos);
}

function processChapter(filePath) {
  try {
    // Resolve from project root
    const projectRoot = path.resolve(__dirname, '../..');
    const fullPath = path.resolve(projectRoot, filePath);
    const content = fs.readFileSync(fullPath, 'utf-8');

    // Extract frontmatter (handle both \n and \r\n line endings)
    const frontmatterMatch = content.match(/^---[\r\n]+([\s\S]*?)[\r\n]+---/);
    if (!frontmatterMatch) {
      console.log(`❌ ${path.basename(filePath)}: No frontmatter found`);
      return;
    }

    const frontmatter = frontmatterMatch[1];
    const learning_goals_match = frontmatter.match(/learning_goals:\s*\n([\s\S]*?)(?=\n\w+:|$)/);

    let learning_goals = [];
    if (learning_goals_match) {
      learning_goals = learning_goals_match[1]
        .split('\n')
        .map(line => line.trim().replace(/^-\s*["']?|["']?$/g, ''))
        .filter(line => line.length > 0);
    }

    // Extract technical terms
    const terms = extractTerms(content);

    // Add components
    let updatedContent = content;
    updatedContent = addWhatYouWillLearn(updatedContent, learning_goals);
    updatedContent = addGrownUpWords(updatedContent, terms);

    // Write back
    fs.writeFileSync(fullPath, updatedContent, 'utf-8');
    console.log(`✅ ${path.basename(filePath)}: Added components`);

  } catch (error) {
    console.log(`❌ ${path.basename(filePath)}: ${error.message}`);
  }
}

// Process all chapters
console.log('🚀 Adding components to all chapters...\n');
chapters.forEach(processChapter);
console.log('\n✨ Done!');
