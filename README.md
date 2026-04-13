# Guess The Country

A modern, fullstack geography quiz app where users guess a country based on three interactive clues.

## Live Demo
**[https://guessthecountryforonomagic.netlify.app/](https://guessthecountryforonomagic.netlify.app/)**

## Features
- **Interactive Clues**: Reveal clues one by one to test your knowledge.
- **Premium UI**: Modern glassmorphism design with smooth animations.
- **Security & Reliability**: Built-in rate limiting and input validation.
- **FastAPI Backend**: Efficient Python-powered session management.
- **React Frontend**: Responsive and fast UI powered by Vite.

## Local Setup

### Prerequisites
- Python 3.8+
- Node.js 16+

### 1. Backend Setup
```bash
cd server
pip install -r requirements.txt
python main.py
```
The backend will start at `http://localhost:8000`.

### 2. Frontend Setup
```bash
cd client
npm install
npm run dev
```
The frontend will start at `http://localhost:5173`.

## AI Usage
This project was developed with the assistance of **Antigravity AI**. Detailed interaction history and technical interpretations can be found in [AI_USAGE.md](./AI_USAGE.md).
