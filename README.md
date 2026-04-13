# Guess The Country

A modern, fullstack geography quiz app where users guess a country based on three interactive clues.

## Features
- **Interactive Clues**: Reveal clues one by one to test your knowledge.
- **Premium UI**: Modern glassmorphism design with smooth animations.
- **FastAPI Backend**: Efficient Python-powered session management.
- **React Frontend**: Responsive and fast UI powered by Vite.

## Setup Instructions

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
The frontend will start at `http://localhost:5173` (or similar).

## Deployment Guide

This app is designed to be deployed with the **Backend on Render** and the **Frontend on Netlify**.

### 1. Backend (Render)
1. Create a new **Web Service** on [Render](https://render.com/).
2. Connect your GitHub repository.
3. Set the following:
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r server/requirements.txt`
   - **Start Command**: `uvicorn server.main:app --host 0.0.0.0 --port $PORT`
   - **Root Directory**: `.` (root of the repo)
4. Once deployed, copy your Render URL (e.g., `https://guess-backend.onrender.com`).

### 2. Frontend (Netlify)
1. Build settings are already configured in `netlify.toml`.
2. In the Netlify dashboard, go to **Site settings > Environment variables**.
3. Add a new variable:
   - **Key**: `VITE_API_URL`
   - **Value**: Your Render URL (from step 1).
4. Trigger a new deploy.

## AI Usage
This project was developed with the assistance of **Antigravity AI**. Detailed prompt history and interpretation can be found in [AI_USAGE.md](./AI_USAGE.md).

