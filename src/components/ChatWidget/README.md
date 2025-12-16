# Chat Widget Usage Guide

## Overview
The chat widget allows users to ask questions about the book content and receive answers with cited sources. Users can optionally include selected text for more context.

## Features
- Floating chat widget accessible from any page
- Text selection capture for contextual questions
- Display of answers with source citations
- Loading indicators during API requests
- Error handling for API failures

## How to Use
1. Click the floating "Chat" button in the bottom-right corner of the screen
2. Optionally select text on the page you're viewing for additional context
3. Type your question in the input field
4. The selected text (if any) will be included with your question
5. Click "Send" to submit your query
6. View the response and sources in the chat window

## Technical Details
- The widget communicates with the backend via the `/api/chat/query` endpoint
- Selected text is captured using the Selection API
- Responses include source references relevant to the answer
- The widget includes error handling for network issues and API failures

## Troubleshooting
- If the chat widget doesn't appear, ensure the page has loaded completely
- If API calls are failing, check browser console for CORS or network errors
- Ensure your backend API endpoint is accessible from your frontend environment