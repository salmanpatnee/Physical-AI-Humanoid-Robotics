#!/usr/bin/env node

/**
 * Readability Analysis Script
 * Analyzes MDX files for readability metrics (Flesch-Kincaid Grade Level, Flesch Reading Ease)
 * Target: Grade 3-6, Reading Ease 70-80
 */

const fs = require('fs');
const path = require('path');
const { default: textReadability } = require('text-readability');

// Remove MDX components and code blocks for pure text analysis
function extractTextContent(mdxContent) {
  let text = mdxContent;

  // Remove frontmatter
  text = text.replace(/^---[\s\S]*?---\n/m, '');

  // Remove MDX component tags (opening and closing)
  text = text.replace(/<[A-Z][a-zA-Z0-9]*[^>]*>[\s\S]*?<\/[A-Z][a-zA-Z0-9]*>/g, '');
  text = text.replace(/<[A-Z][a-zA-Z0-9]*[^>]*\/>/g, '');

  // Remove code blocks
  text = text.replace(/```[\s\S]*?```/g, '');
  text = text.replace(/`[^`]+`/g, '');

  // Remove markdown headers but keep the text
  text = text.replace(/^#{1,6}\s+/gm, '');

  // Remove markdown formatting
  text = text.replace(/\*\*([^*]+)\*\*/g, '$1'); // bold
  text = text.replace(/\*([^*]+)\*/g, '$1'); // italic
  text = text.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1'); // links

  // Remove extra whitespace
  text = text.replace(/\n{3,}/g, '\n\n');
  text = text.trim();

  return text;
}

function analyzeFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const text = extractTextContent(content);

    if (!text || text.length < 100) {
      return {
        error: 'Insufficient text content for analysis (less than 100 characters)',
        filePath
      };
    }

    // Calculate readability metrics
    const fleschKincaidGrade = textReadability.fleschKincaidGrade(text);
    const fleschReadingEase = textReadability.fleschReadingEase(text);
    const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
    const words = text.split(/\s+/).filter(w => w.length > 0);
    const avgSentenceLength = words.length / sentences.length;

    // Determine if metrics meet targets
    const gradeInRange = fleschKincaidGrade >= 3.0 && fleschKincaidGrade <= 6.0;
    const easeInRange = fleschReadingEase >= 70 && fleschReadingEase <= 80;
    const sentenceLengthGood = avgSentenceLength >= 12 && avgSentenceLength <= 15;

    const status = gradeInRange && easeInRange ? '✅ PASS' : '⚠️ NEEDS IMPROVEMENT';

    return {
      filePath,
      status,
      metrics: {
        fleschKincaidGrade: fleschKincaidGrade.toFixed(1),
        fleschReadingEase: fleschReadingEase.toFixed(1),
        avgSentenceLength: avgSentenceLength.toFixed(1),
        totalWords: words.length,
        totalSentences: sentences.length
      },
      targets: {
        gradeLevel: '3.0 - 6.0',
        readingEase: '70 - 80',
        avgSentenceLength: '12 - 15 words'
      },
      evaluation: {
        gradeLevel: gradeInRange ? '✅' : '❌',
        readingEase: easeInRange ? '✅' : '❌',
        sentenceLength: sentenceLengthGood ? '✅' : '⚠️'
      }
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

  console.log(`\n${result.status} ${path.basename(result.filePath)}`);
  console.log('─'.repeat(60));
  console.log(`📊 Readability Metrics:`);
  console.log(`   Flesch-Kincaid Grade: ${result.metrics.fleschKincaidGrade} ${result.evaluation.gradeLevel} (target: ${result.targets.gradeLevel})`);
  console.log(`   Flesch Reading Ease:  ${result.metrics.fleschReadingEase} ${result.evaluation.readingEase} (target: ${result.targets.readingEase})`);
  console.log(`   Avg Sentence Length:  ${result.metrics.avgSentenceLength} words ${result.evaluation.sentenceLength} (target: ${result.targets.avgSentenceLength})`);
  console.log(`\n📝 Content Stats:`);
  console.log(`   Total Words:     ${result.metrics.totalWords}`);
  console.log(`   Total Sentences: ${result.metrics.totalSentences}`);
}

// Main execution
if (require.main === module) {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log('Usage: node analyze-readability.js <mdx-file-path>');
    console.log('Example: node analyze-readability.js docs/module1-robotic-nervous-system/01-focus-middleware-for-robot-control.mdx');
    process.exit(1);
  }

  const filePath = path.resolve(args[0]);

  if (!fs.existsSync(filePath)) {
    console.error(`❌ File not found: ${filePath}`);
    process.exit(1);
  }

  console.log('🔍 Analyzing readability...');
  const result = analyzeFile(filePath);
  formatReport(result);

  // Exit with error code if analysis failed or didn't meet targets
  if (result.error || result.status.includes('NEEDS IMPROVEMENT')) {
    process.exit(1);
  }
}

module.exports = { analyzeFile, extractTextContent };
