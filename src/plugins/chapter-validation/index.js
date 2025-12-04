const path = require('path');
const Ajv = require('ajv');

module.exports = function chapterValidationPlugin(context, options) {
  return {
    name: 'chapter-validation-plugin',

    async contentLoaded({ content, actions }) {
      const ajv = new Ajv({ allErrors: true });

      // Load the schema from the contracts directory
      const schemaPath = path.resolve(
        __dirname,
        '../../../specs/003-chapter-template-system/contracts/ChapterMetadata.schema.json'
      );
      const schema = require(schemaPath);
      const validate = ajv.compile(schema);

      // Get all docs from the content
      const { docs } = content || {};
      if (!docs) {
        return;
      }

      // Validate each document's frontmatter
      const errors = [];
      docs.forEach((doc) => {
        const { frontMatter, source } = doc;

        // Only validate if the document has a chapter_type (indicating it's a chapter)
        if (!frontMatter || !frontMatter.chapter_type) {
          return; // Skip non-chapter documents
        }

        const isValid = validate(frontMatter);
        if (!isValid) {
          errors.push({
            file: source,
            errors: validate.errors,
          });
        }
      });

      // If there are validation errors, fail the build
      if (errors.length > 0) {
        const errorMessages = errors.map((error) => {
          const errorDetails = error.errors
            .map((e) => `  - ${e.instancePath || 'root'}: ${e.message}`)
            .join('\n');
          return `\nFile: ${error.file}\n${errorDetails}`;
        });

        throw new Error(
          `Chapter frontmatter validation failed:\n${errorMessages.join('\n')}`
        );
      }
    },
  };
};
