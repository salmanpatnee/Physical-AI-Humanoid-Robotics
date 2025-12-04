const path = require('path');
const Ajv = require('ajv');

describe('Chapter Validation Plugin', () => {
  let ajv;
  let validate;

  beforeAll(() => {
    ajv = new Ajv({ allErrors: true });
    const schemaPath = path.resolve(
      __dirname,
      '../../../specs/003-chapter-template-system/contracts/ChapterMetadata.schema.json'
    );
    const schema = require(schemaPath);
    validate = ajv.compile(schema);
  });

  test('should validate correct chapter metadata', () => {
    const validMetadata = {
      title: 'Test Chapter',
      sidebar_position: 1,
      chapter_type: 'tutorial',
      learning_goals: ['Goal 1', 'Goal 2'],
      prerequisites: ['Prereq 1'],
      key_takeaways: ['Takeaway 1'],
    };

    const isValid = validate(validMetadata);
    expect(isValid).toBe(true);
  });

  test('should reject metadata with invalid chapter_type', () => {
    const invalidMetadata = {
      title: 'Test Chapter',
      sidebar_position: 1,
      chapter_type: 'invalid_type',
      learning_goals: ['Goal 1'],
      key_takeaways: ['Takeaway 1'],
    };

    const isValid = validate(invalidMetadata);
    expect(isValid).toBe(false);
    expect(validate.errors).toBeTruthy();
  });

  test('should reject metadata missing required fields', () => {
    const invalidMetadata = {
      title: 'Test Chapter',
      sidebar_position: 1,
      // missing chapter_type, learning_goals, and key_takeaways
    };

    const isValid = validate(invalidMetadata);
    expect(isValid).toBe(false);
    expect(validate.errors.length).toBeGreaterThan(0);
  });

  test('should reject metadata with empty learning_goals array', () => {
    const invalidMetadata = {
      title: 'Test Chapter',
      sidebar_position: 1,
      chapter_type: 'concept',
      learning_goals: [],
      key_takeaways: ['Takeaway 1'],
    };

    const isValid = validate(invalidMetadata);
    expect(isValid).toBe(false);
  });

  test('should accept metadata without prerequisites (optional field)', () => {
    const validMetadata = {
      title: 'Test Chapter',
      sidebar_position: 1,
      chapter_type: 'reference',
      learning_goals: ['Goal 1'],
      key_takeaways: ['Takeaway 1'],
      // prerequisites is optional
    };

    const isValid = validate(validMetadata);
    expect(isValid).toBe(true);
  });

  test('should validate all chapter types', () => {
    const chapterTypes = ['tutorial', 'concept', 'lab', 'reference'];

    chapterTypes.forEach((type) => {
      const metadata = {
        title: 'Test Chapter',
        sidebar_position: 1,
        chapter_type: type,
        learning_goals: ['Goal 1'],
        key_takeaways: ['Takeaway 1'],
      };

      const isValid = validate(metadata);
      expect(isValid).toBe(true);
    });
  });
});
