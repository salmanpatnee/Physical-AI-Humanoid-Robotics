#!/usr/bin/env node

/**
 * Technical Term Extractor Script
 * Extracts technical terms from MDX files and suggests simple term mappings
 * Helps build the "Grown-Up Words" glossary
 */

const fs = require('fs');
const path = require('path');

// Common technical terms in robotics/AI domain with suggested simple terms
const knownTerms = {
  'ROS2': { simple: "Robot's language", category: 'core' },
  'ROS 2': { simple: "Robot's language", category: 'core' },
  'Node': { simple: "Robot part or worker", category: 'core' },
  'Topic': { simple: "Announcement channel", category: 'core' },
  'Publisher': { simple: "Announcer", category: 'core' },
  'Subscriber': { simple: "Listener", category: 'core' },
  'Service': { simple: "Question-answer system", category: 'core' },
  'Middleware': { simple: "Connection system", category: 'core' },
  'URDF': { simple: "Robot blueprint", category: 'description' },
  'Gazebo': { simple: "Robot practice world", category: 'simulation' },
  'Isaac Sim': { simple: "NVIDIA robot training world", category: 'simulation' },
  'Simulation': { simple: "Practice environment", category: 'simulation' },
  'Sensor': { simple: "Robot's senses", category: 'hardware' },
  'LiDAR': { simple: "Laser distance measurer", category: 'hardware' },
  'Camera': { simple: "Robot's eyes", category: 'hardware' },
  'IMU': { simple: "Balance sensor", category: 'hardware' },
  'Processor': { simple: "Robot's brain", category: 'hardware' },
  'CPU': { simple: "Computer brain", category: 'hardware' },
  'GPU': { simple: "Graphics brain", category: 'hardware' },
  'VSLAM': { simple: "Map-making with camera", category: 'ai' },
  'Path Planning': { simple: "Route finding", category: 'ai' },
  'Computer Vision': { simple: "Robot seeing and understanding", category: 'ai' },
  'LLM': { simple: "Smart language helper", category: 'ai' },
  'Neural Network': { simple: "Learning pattern matcher", category: 'ai' },
  'Launch File': { simple: "Startup instructions", category: 'core' },
  'Package': { simple: "Toolbox", category: 'core' },
  'Message': { simple: "Information packet", category: 'core' }
};

// Extract text content and identify technical terms
function extractTerms(mdxContent) {
  let text = mdxContent;

  // Remove frontmatter
  text = text.replace(/^---[\s\S]*?---\n/m, '');

  // Remove code blocks (but keep inline code for term detection)
  text = text.replace(/```[\s\S]*?```/g, '');

  const foundTerms = new Map();

  // Search for known technical terms
  Object.keys(knownTerms).forEach(term => {
    const regex = new RegExp(`\\b${term}\\b`, 'gi');
    const matches = text.match(regex);

    if (matches && matches.length > 0) {
      const termInfo = knownTerms[term];
      foundTerms.set(term, {
        count: matches.length,
        simple: termInfo.simple,
        category: termInfo.category,
        technical: term
      });
    }
  });

  // Extract terms from inline code that might be technical
  const inlineCodeRegex = /`([^`]+)`/g;
  let match;
  while ((match = inlineCodeRegex.exec(text)) !== null) {
    const codeTerm = match[1];
    // Check if it's a known term
    if (knownTerms[codeTerm] && !foundTerms.has(codeTerm)) {
      foundTerms.set(codeTerm, {
        count: 1,
        simple: knownTerms[codeTerm].simple,
        category: knownTerms[codeTerm].category,
        technical: codeTerm
      });
    }
  }

  return foundTerms;
}

// Find context examples for terms
function findContextExamples(mdxContent, terms) {
  const examples = new Map();

  terms.forEach((info, term) => {
    const regex = new RegExp(`[^.!?]*\\b${term}\\b[^.!?]*[.!?]`, 'i');
    const match = mdxContent.match(regex);

    if (match) {
      let example = match[0].trim();
      // Clean up example
      example = example.replace(/^[#*\-\s]+/, '');
      example = example.replace(/`/g, '');

      if (example.length > 200) {
        example = example.substring(0, 197) + '...';
      }

      examples.set(term, example);
    }
  });

  return examples;
}

function analyzeFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const terms = extractTerms(content);
    const examples = findContextExamples(content, terms);

    if (terms.size === 0) {
      return {
        warning: 'No technical terms found',
        filePath
      };
    }

    // Convert to array and sort by frequency
    const termsList = Array.from(terms.entries())
      .map(([term, info]) => ({
        technical_term: term,
        simple_term: info.simple,
        category: info.category,
        count: info.count,
        context_example: examples.get(term) || `The chapter discusses ${term}.`
      }))
      .sort((a, b) => b.count - a.count);

    return {
      filePath,
      totalTerms: termsList.length,
      terms: termsList
    };

  } catch (error) {
    return {
      error: `Failed to analyze file: ${error.message}`,
      filePath
    };
  }
}

function formatReport(result) {
  if (result.error) {
    console.log(`\n❌ Error: ${result.error}`);
    console.log(`   File: ${result.filePath}`);
    return;
  }

  if (result.warning) {
    console.log(`\n⚠️  ${result.warning}`);
    console.log(`   File: ${result.filePath}`);
    return;
  }

  console.log(`\n✅ Found ${result.totalTerms} technical terms in ${path.basename(result.filePath)}`);
  console.log('─'.repeat(80));

  // Group by category
  const byCategory = {};
  result.terms.forEach(term => {
    if (!byCategory[term.category]) {
      byCategory[term.category] = [];
    }
    byCategory[term.category].push(term);
  });

  Object.keys(byCategory).sort().forEach(category => {
    console.log(`\n📚 ${category.toUpperCase()} Terms:`);
    byCategory[category].forEach(term => {
      console.log(`   ${term.technical_term} → "${term.simple_term}" (used ${term.count}x)`);
    });
  });

  console.log('\n\n📝 Suggested GrownUpWords Component Data:');
  console.log('─'.repeat(80));
  console.log('<GrownUpWords');
  console.log('  terms={[');

  result.terms.slice(0, 10).forEach((term, index) => {
    console.log('    {');
    console.log(`      simple_term: "${term.simple_term}",`);
    console.log(`      technical_term: "${term.technical_term}",`);
    console.log(`      context_example: "${term.context_example}"`);
    console.log(`    }${index < Math.min(9, result.terms.length - 1) ? ',' : ''}`);
  });

  console.log('  ]}');
  console.log('/>');
}

// Main execution
if (require.main === module) {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log('Usage: node extract-technical-terms.js <mdx-file-path>');
    console.log('Example: node extract-technical-terms.js docs/module1-robotic-nervous-system/01-focus-middleware-for-robot-control.mdx');
    process.exit(1);
  }

  const filePath = path.resolve(args[0]);

  if (!fs.existsSync(filePath)) {
    console.error(`❌ File not found: ${filePath}`);
    process.exit(1);
  }

  console.log('🔍 Extracting technical terms...');
  const result = analyzeFile(filePath);
  formatReport(result);
}

module.exports = { analyzeFile, extractTerms, knownTerms };
