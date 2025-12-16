# Quickstart Guide: Chatbot-Docusaurus Integration

## Overview
This guide provides instructions to quickly get the chatbot integration feature up and running in the Docusaurus frontend.

## Prerequisites
- Node.js 18+ and npm/yarn
- Python 3.11+ with pip
- Access to the FastAPI backend API

## Setting up the Frontend (Docusaurus)

1. Navigate to your Docusaurus project directory:
   ```bash
   cd your-docusaurus-project
   ```

2. Install required dependencies:
   ```bash
   npm install # or yarn
   ```

3. Create a new React component for the chat widget:
   - Create `src/components/ChatWidget/index.js`
   - Create accompanying CSS at `src/components/ChatWidget/styles.css`

4. Add the component to your Docusaurus pages where needed:
   - Import the component in your MDX files
   - Add text selection functionality to capture selected content

## Setting up the Backend (FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the backend server:
   ```bash
   uvicorn src.api.main:app --reload
   ```

## Environment Configuration

1. Create a `.env` file in your frontend directory with the following:
   ```
   REACT_APP_CHATBOT_API_URL=http://localhost:8000
   REACT_APP_API_KEY=your-api-key-here
   ```

## Running the Application

1. Start the Docusaurus development server:
   ```bash
   npm run start
   ```

2. The chatbot widget should now be visible on your pages, allowing users to ask questions and optionally provide selected text context.

## Testing the Integration

1. Visit any book page in your Docusaurus site
2. Select some text on the page
3. Type a question in the chat widget
4. Verify that the selected text is passed along with your query
5. Check that the response includes relevant sources

## Troubleshooting

- If the chat widget doesn't appear, verify that you've correctly added the component to your layout/page
- If API calls are failing, check the console for CORS or network errors
- Ensure your backend API endpoint is accessible from your frontend environment