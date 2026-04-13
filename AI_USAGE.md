# AI Usage Documentation

This document summarizes the interaction between the user and the AI assistant during the development of the "Guess The Country" application.

## AI Tools Used
- **Antigravity (Google DeepMind)**: Used for architecture planning, backend development (FastAPI), frontend development (React), and documentation.
- **Vite**: Used for scaffolding the React application.
- **Git**: Used for version control.

## Prompts and interpretation

| Phase | User Prompt | AI Interpretation & Action |
|-------|-------------|----------------------------|
| **Initialization** | "can u see the pdf?" | Read and parsed `onomagic_fullstack_task.pdf` to extract project requirements. |
| **Planning** | "proceed" | Proposed a fullstack architecture (React + Node.js/Express) and premium design. |
| **Logic/Stack** | "use python for the backend" | Pivoted from Node.js to Python/FastAPI as requested. |
| **Game Mechanics**| "unlocking the clues sounds better - use that method." | Implemented a gamified "Unlock Clue" system instead of showing all clues at once. |
| **Compliance** | "also make sure to doucment this conversion and my prompts" | Created this `AI_USAGE.md` file to ensure full compliance with the assessment requirements. |
| **Refinement** | "make sure that the user can try to guess the county again without telling him the answer until he chooses to see it and move on to the next guess" | Updated API and UI to support multiple attempts and a semi-hidden answer reveal. |
| **Logging** | "add logs to users input for debugging" | Implemented server-side logging (to stream and `game.log`) for all user interactions. |
| **Security** | "limit input length... limit the requests"| Implemented Pydantic-based input validation and SlowAPI rate limiting. Added `maxLength` to the frontend input. |

## Code Generation vs. Manual Modification
- **AI Generated**: 
  - Entire FastAPI backend structure and game logic.
  - React frontend (Vite scaffolded, logic implemented by AI).
  - Premium CSS design system (glassmorphism UI).
  - Dataset of 10 countries with clues.
- **User Modified**:
  - The user guided the technology selection (Python) and the specific game mechanic (Clue unlocking).

## Configuration Tools
- No specific AI configuration tools (like `.cursor/rules`) were used beyond the default system instructions of the Antigravity assistant.
