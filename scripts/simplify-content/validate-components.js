#!/usr/bin/env node

/**
 * Component Validation Script
 * Validates that MDX files use simplification components correctly
 * Checks for WhatYouWillLearn, DoubtfulQA, and GrownUpWords components
 */

const fs = require('fs');
const path = require('path');

// Component patterns to detect
const componentPatterns = {
  WhatYouWillLearn: /<WhatYouWillLearn[\s\S]*?\/>/g,
  DoubtfulQA: /<DoubtfulQA[\s\S]*?\/>/g,
  GrownUpWords: /<GrownUpWords[\s\S]*?\/>/g
};

// Validate component structure
function validateComponent(componentName, componentText) {
  const issues = [];

  if (componentName === 'WhatYouWillLearn') {
    // Check for goals prop
    if (!componentText.includes('goals=')) {
      issues.push('Missing required "goals" prop');
    }

    // Check for minimum 3 goals
    const goalsMatch = componentText.match(/goals=\{(\[[\s\S]*?\])\}/);
    if (goalsMatch) {
      const goalsText = goalsMatch[1];
      const goalCount = (goalsText.match(/\{/g) || []).length;
      if (goalCount < 3) {
        issues.push(`Only ${goalCount} goals found, minimum 3 required`);
      }
      if (goalCount > 5) {
        issues.push(`${goalCount} goals found, maximum 5 recommended`);
      }
    }
  }

  if (componentName === 'DoubtfulQA') {
    // Check for questions prop
    if (!componentText.includes('questions=')) {
      issues.push('Missing required "questions" prop');
    }

    // Check for minimum 5 questions
    const questionsMatch = componentText.match(/questions=\{(\[[\s\S]*?\])\}/);
    if (questionsMatch) {
      const questionsText = questionsMatch[1];
      const questionCount = (questionsText.match(/question:/g) || []).length;
      if (questionCount < 5) {
        issues.push(`Only ${questionCount} questions found, minimum 5 required`);
      }
      if (questionCount > 8) {
        issues.push(`${questionCount} questions found, maximum 8 recommended`);
      }

      // Check for required fields in questions
      const hasIds = questionsText.includes('id:');
      const hasCategories = questionsText.includes('category:');
      const hasMisconceptions = questionsText.includes('misconception_addressed:');

      if (!hasIds) issues.push('Questions missing "id" field');
      if (!hasCategories) issues.push('Questions missing "category" field');
      if (!hasMisconceptions) issues.push('Questions missing "misconception_addressed" field');
    }
  }

  if (componentName === 'GrownUpWords') {
    // Check for terms prop
    if (!componentText.includes('terms=')) {
      issues.push('Missing required "terms" prop');
    }

    // Check for minimum 5 terms
    const termsMatch = componentText.match(/terms=\{(\[[\s\S]*?\])\}/);
    if (termsMatch) {
      const termsText = termsMatch[1];
      const termCount = (termsText.match(/simple_term:/g) || []).length;
      if (termCount < 5) {
        issues.push(`Only ${termCount} terms found, minimum 5 required`);
      }

      // Check for required fields
      const hasSimpleTerms = termsText.includes('simple_term:');
      const hasTechnicalTerms = termsText.includes('technical_term:');
      const hasContextExamples = termsText.includes('context_example:');

      if (!hasSimpleTerms) issues.push('Terms missing "simple_term" field');
      if (!hasTechnicalTerms) issues.push('Terms missing "technical_term" field');
      if (!hasContextExamples) issues.push('Terms missing "context_example" field');
    }
  }

  return issues;
}

function analyzeFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');

    const results = {
      filePath,
      componentsFound: {},
      issues: [],
      recommendations: []
    };

    // Check for each component type
    Object.keys(componentPatterns).forEach(componentName => {
      const pattern = componentPatterns[componentName];
      const matches = content.match(pattern);

      results.componentsFound[componentName] = {
        count: matches ? matches.length : 0,
        present: matches && matches.length > 0
      };

      if (matches) {
        matches.forEach((match, index) => {
          const componentIssues = validateComponent(componentName, match);
          if (componentIssues.length > 0) {
            results.issues.push({
              component: componentName,
              instance: index + 1,
              issues: componentIssues
            });
          }
        });
      }
    });

    // Generate recommendations
    if (!results.componentsFound.WhatYouWillLearn.present) {
      results.recommendations.push('Add <WhatYouWillLearn> component at the beginning of the chapter');
    }

    if (!results.componentsFound.DoubtfulQA.present) {
      results.recommendations.push('Add <DoubtfulQA> component after major concepts to address confusion points');
    }

    if (!results.componentsFound.GrownUpWords.present) {
      results.recommendations.push('Add <GrownUpWords> component at the end to map simplified terms to technical terminology');
    }

    // Check if this looks like simplified content
    const hasShortParagraphs = content.split('\n\n').some(para => {
      const sentences = para.split(/[.!?]/).filter(s => s.trim().length > 0);
      return sentences.length >= 1 && sentences.length <= 4;
    });

    if (!hasShortParagraphs && results.componentsFound.WhatYouWillLearn.present) {
      results.recommendations.push('Consider breaking long paragraphs into shorter ones (3-4 sentences max)');
    }

    return results;

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

  const fileName = path.basename(result.filePath);
  const allPresent = Object.values(result.componentsFound).every(c => c.present);
  const hasIssues = result.issues.length > 0;

  let status = '✅ VALID';
  if (!allPresent) status = '⚠️ INCOMPLETE';
  if (hasIssues) status = '❌ INVALID';

  console.log(`\n${status} ${fileName}`);
  console.log('─'.repeat(80));

  console.log('\n📦 Components Found:');
  Object.keys(result.componentsFound).forEach(name => {
    const comp = result.componentsFound[name];
    const icon = comp.present ? '✅' : '❌';
    console.log(`   ${icon} ${name}: ${comp.count} instance(s)`);
  });

  if (result.issues.length > 0) {
    console.log('\n❌ Validation Issues:');
    result.issues.forEach(issue => {
      console.log(`   ${issue.component} (instance ${issue.instance}):`);
      issue.issues.forEach(iss => {
        console.log(`      • ${iss}`);
      });
    });
  }

  if (result.recommendations.length > 0) {
    console.log('\n💡 Recommendations:');
    result.recommendations.forEach(rec => {
      console.log(`   • ${rec}`);
    });
  }

  if (allPresent && !hasIssues) {
    console.log('\n✨ All simplification components are correctly implemented!');
  }
}

// Main execution
if (require.main === module) {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log('Usage: node validate-components.js <mdx-file-path>');
    console.log('Example: node validate-components.js docs/module1-robotic-nervous-system/01-focus-middleware-for-robot-control.mdx');
    process.exit(1);
  }

  const filePath = path.resolve(args[0]);

  if (!fs.existsSync(filePath)) {
    console.error(`❌ File not found: ${filePath}`);
    process.exit(1);
  }

  console.log('🔍 Validating components...');
  const result = analyzeFile(filePath);
  formatReport(result);

  // Exit with error code if validation failed
  if (result.error || result.issues.length > 0 ||
      !Object.values(result.componentsFound).every(c => c.present)) {
    process.exit(1);
  }
}

module.exports = { analyzeFile, validateComponent };
