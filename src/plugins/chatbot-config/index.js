// Docusaurus plugin to inject chatbot configuration into the window object
module.exports = function (context, options) {
  return {
    name: 'chatbot-config-plugin',
    injectHtmlTags() {
      // Read from environment variables or use defaults
      const chatbotApiUrl = process.env.CHATBOT_API_URL || 'http://localhost:8000';
      const chatbotApiKey = process.env.CHATBOT_API_KEY || '';

      return {
        headTags: [
          {
            tagName: 'script',
            innerHTML: `
              window.CHATBOT_API_URL = '${chatbotApiUrl}';
              window.CHATBOT_API_KEY = '${chatbotApiKey}';
            `,
          },
        ],
      };
    },
  };
};
