const fs = require('fs');
const path = require('path');

const files = [
  'docs/module3-ai-robot-brain/01-focus-advanced-perception-and-synthetic-data.mdx',
  'docs/test-simplified-components.mdx',
  'docs/module4-vision-language-action/04-capstone-the-autonomous-humanoid.mdx',
  'docs/module4-vision-language-action/03-cognitive-planning-using-llms-for-ros2-task-decomposition.mdx',
  'docs/module4-vision-language-action/02-voice-to-action-using-whisper.mdx',
  'docs/module4-vision-language-action/01-focus-the-convergence-of-llms-and-robotics.mdx',
  'docs/module3-ai-robot-brain/04-nav2-for-humanoid-path-planning-and-locomotion.mdx',
  'docs/module3-ai-robot-brain/03-isaac-ros-for-gpu-accelerated-vslam-and-navigation.mdx',
  'docs/module3-ai-robot-brain/02-isaac-sim-for-photorealistic-simulation-and-training.mdx',
  'docs/module1-robotic-nervous-system/01-focus-middleware-for-robot-control.mdx',
  'docs/module1-robotic-nervous-system/04-understanding-urdf.mdx',
  'docs/module1-robotic-nervous-system/05-managing-complex-systems-with-launch-files.mdx',
  'docs/module2-the-digital-twin/01-focus-physics-simulation-and-world-building.mdx',
  'docs/module2-the-digital-twin/02-simulating-collisions-gravity-and-sensors-in-gazebo.mdx',
  'docs/module2-the-digital-twin/03-high-fidelity-rendering-and-interaction-scenes-in-unity.mdx',
  'docs/module2-the-digital-twin/04-sensor-simulation-lidar-depth-cameras-and-imus.mdx',
  'docs/99-chapter-template-example/index.mdx'
];

function removeComponent(content, componentName) {
  // Remove self-closing component tags
  const selfClosingRegex = new RegExp(`<${componentName}[^>]*/>`, 'gs');
  content = content.replace(selfClosingRegex, '');

  // Remove component with content (opening and closing tags)
  const withContentRegex = new RegExp(`<${componentName}[^>]*>.*?<\/${componentName}>`, 'gs');
  content = content.replace(withContentRegex, '');

  return content;
}

function cleanFile(filePath) {
  const fullPath = path.join(process.cwd(), filePath);

  if (!fs.existsSync(fullPath)) {
    console.log(`❌ File not found: ${filePath}`);
    return;
  }

  let content = fs.readFileSync(fullPath, 'utf8');
  const originalContent = content;

  // Remove broken components
  content = removeComponent(content, 'WhatYouWillLearn');
  content = removeComponent(content, 'DoubtfulQA');
  content = removeComponent(content, 'GrownUpWords');

  // Clean up multiple consecutive blank lines
  content = content.replace(/\n{3,}/g, '\n\n');

  if (content !== originalContent) {
    fs.writeFileSync(fullPath, content, 'utf8');
    console.log(`✅ Cleaned: ${filePath}`);
  } else {
    console.log(`⏭️  No changes: ${filePath}`);
  }
}

console.log('🧹 Removing broken components from MDX files...\n');

files.forEach(cleanFile);

console.log('\n✨ Done!');
