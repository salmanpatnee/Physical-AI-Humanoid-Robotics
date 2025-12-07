const fs = require('fs');
const path = require('path');

// Files with Technical Terms Glossary
const files = [
  'docs/module2-the-digital-twin/03-high-fidelity-rendering-and-interaction-scenes-in-unity.mdx',
  'docs/module2-the-digital-twin/04-sensor-simulation-lidar-depth-cameras-and-imus.mdx',
  'docs/module2-the-digital-twin/02-simulating-collisions-gravity-and-sensors-in-gazebo.mdx',
  'docs/module2-the-digital-twin/01-focus-physics-simulation-and-world-building.mdx',
  'docs/module1-robotic-nervous-system/05-managing-complex-systems-with-launch-files.mdx',
  'docs/module1-robotic-nervous-system/01-focus-middleware-for-robot-control.mdx',
  'docs/module1-robotic-nervous-system/04-understanding-urdf.mdx',
  'docs/module3-ai-robot-brain/02-isaac-sim-for-photorealistic-simulation-and-training.mdx',
  'docs/module3-ai-robot-brain/03-isaac-ros-for-gpu-accelerated-vslam-and-navigation.mdx',
  'docs/module3-ai-robot-brain/04-nav2-for-humanoid-path-planning-and-locomotion.mdx',
  'docs/module4-vision-language-action/01-focus-the-convergence-of-llms-and-robotics.mdx',
  'docs/module4-vision-language-action/02-voice-to-action-using-whisper.mdx',
  'docs/module4-vision-language-action/03-cognitive-planning-using-llms-for-ros2-task-decomposition.mdx',
  'docs/module4-vision-language-action/04-capstone-the-autonomous-humanoid.mdx',
  'docs/module3-ai-robot-brain/01-focus-advanced-perception-and-synthetic-data.mdx'
];

function removeEmptyGlossary(filePath) {
  const fullPath = path.join(process.cwd(), filePath);
  let content = fs.readFileSync(fullPath, 'utf8');
  const originalContent = content;

  // Remove empty Technical Terms Glossary sections
  // Pattern: ## Technical Terms Glossary followed by optional whitespace and then another ## or end of file
  content = content.replace(
    /## Technical Terms Glossary\s*\n\s*\n\s*(?=##|$)/g,
    ''
  );

  // Clean up multiple consecutive blank lines
  content = content.replace(/\n{3,}/g, '\n\n');

  if (content !== originalContent) {
    fs.writeFileSync(fullPath, content, 'utf8');
    console.log(`✅ Removed empty glossary from: ${filePath}`);
    return true;
  }
  return false;
}

console.log('🧹 Removing empty Technical Terms Glossary sections...\n');

let count = 0;
files.forEach(file => {
  if (removeEmptyGlossary(file)) {
    count++;
  }
});

console.log(`\n✨ Done! Removed ${count} empty glossary sections.`);
