# Engineering Journal

---

# Feature 2 — Structured Response Engine

## Objective

Enable the application to request structured responses from Gemini and process them programmatically.

---

## What We Built

- Prompt Builder
- Response Parser
- Response Format Selection
- JSON Parsing
- Modular Architecture

---

## Problems Faced

### 1. GitHub Secret Scanning

Problem:
GitHub rejected the push because the API key was committed.

Solution:
- Removed the secret from Git history
- Added `.env` to `.gitignore`

Lesson: Never commit secrets.

---

### 2. Deprecated Gemini Model

Problem:
`gemini-2.5-flash` returned 404.
The model endpoint had changed.

Solution:
Investigated available models and updated the configuration.

Lesson: Verify external dependencies rather than assuming.

---

### 3. API Quota Exceeded

Problem:
Received `429 RESOURCE_EXHAUSTED`.

Root Cause:
Google AI Studio Free Tier quota.

Solution:
I isolated the issue
Verified the application wasn't the issue by:
- Listing models
- Testing minimal API calls
- Creating a new project
- Isolating the issue

Conclusion:
The limitation was external.

Lesson: Not every error is caused by your code.

---

### 4. JSON Parsing

Problem:
LLMs may not always return perfectly formatted JSON.

Solution:
Added a dedicated response parser and response cleaning.

Lesson: AI outputs need validation and processing before applications rely on them.

---

## Key Learnings

- Modular Architecture
- Structured Outputs
- Prompt Engineering
- API Debugging
- Error Handling
- Separation of Concerns