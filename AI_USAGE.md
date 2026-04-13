# AI Usage Documentation

This document summarizes the interaction between the user and the AI assistant during the development of the "Guess The Country" application.

## AI Tools Used
- **Antigravity (Google DeepMind)**: Used for architecture planning, backend development (FastAPI), frontend development (React), and documentation.
- **Vite**: Used for scaffolding the React application.
- **Git**: Used for version control.

## Development Phases and AI Interaction

| Development Phase | User Guidance & Direction | AI Interpretation & Action |
|-------------------|---------------------------|----------------------------|
| **Initialization** | Requirement Analysis | Read and parsed the task PDF to extract core project requirements. |
| **Technology Stack** | Backend Selection | Transitioned from Node.js to Python/FastAPI as requested by the user. |
| **UX Design** | Game Mechanics | Implemented an interactive "Unlock Clue" system based on user preference. |
| **Logic Refinement** | Game Loop Polish | Refined the guess validation to allow multiple attempts and manual answer revelation. |
| **Observability** | Debugging Infrastructure | Integrated comprehensive server-side logging for user inputs and game events. |
| **Security Oversight** | Resource Protection | Implemented Pydantic-based input validation and SlowAPI rate limiting per user direction. |
| **Deployment** | Production Readiness | Decoupled API configurations and optimized build settings for Netlify/Render deployment. |

## Code Generation vs. Manual Modification
- **AI Generated**: 
  - Entire FastAPI backend structure and game logic.
  - React frontend (Vite scaffolded, logic implemented by AI).
  - Premium CSS design system (glassmorphism UI).
  - Dataset of 10 countries with clues.
- **User Oversight & Modification**:
  - The user directed the choice of technology and specific gameplay mechanics.
  - **The user performed critical security oversight**, identifying the need for input sanitization and request rate limiting.
  - The user verified the local and production stability of the application.

## Configuration Tools
- No specific AI configuration tools (like `.cursor/rules`) were used beyond the default system instructions of the Antigravity assistant.
