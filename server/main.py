from fastapi import FastAPI, HTTPException, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import json
import random
import uuid
import os
import logging

# Configure rate limiting
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Guess The Country API")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("guess-the-country")

# Enable CORS for frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load country data
countries_path = os.path.join(os.path.dirname(__file__), "countries.json")
with open(countries_path, "r") as f:
    COUNTRIES = json.load(f)

# In-memory storage for active games (sessions)
sessions = {}

@app.get("/")
async def health_check():
    return {"status": "healthy"}

class GuessRequest(BaseModel):
    session_id: str = Field(..., max_length=100)
    guess: str = Field(..., max_length=50)

@app.get("/api/game/new")
@limiter.limit("10/minute")
async def start_new_game(request: Request):
    country = random.choice(COUNTRIES)
    session_id = str(uuid.uuid4())
    
    sessions[session_id] = {
        "country_name": country["name"],
        "clues": country["clues"],
        "unlocked_clues": 1
    }
    
    logger.info(f"New Game Started | Session: {session_id} | Target: {country['name']}")
    
    return {
        "session_id": session_id,
        "clue": country["clues"][0],
        "total_clues": len(country["clues"])
    }

@app.get("/api/game/clue")
@limiter.limit("20/minute")
async def get_next_clue(request: Request, session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[session_id]
    if session["unlocked_clues"] >= len(session["clues"]):
        raise HTTPException(status_code=400, detail="No more clues available")
    
    clue_index = session["unlocked_clues"]
    session["unlocked_clues"] += 1
    
    logger.info(f"Clue Unlocked | Session: {session_id} | Clue Number: {session['unlocked_clues']}")
    
    return {
        "clue": session["clues"][clue_index],
        "clue_number": session["unlocked_clues"]
    }

@app.get("/api/game/reveal")
@limiter.limit("10/minute")
async def reveal_answer(request: Request, session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[session_id]
    logger.info(f"Answer Revealed | Session: {session_id} | Answer: {session['country_name']}")
    return {
        "answer": session["country_name"],
        "message": f"The correct answer was {session['country_name']}."
    }

@app.post("/api/game/guess")
@limiter.limit("30/minute")
async def submit_guess(request: Request, guess_req: GuessRequest = Body(...)):
    session_id = guess_req.session_id
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[session_id]
    correct_name = session["country_name"].lower()
    user_guess = guess_req.guess.strip().lower()
    
    is_correct = user_guess == correct_name
    
    logger.info(f"Guess Submitted | Session: {session_id} | Guess: '{guess_req.guess}' | Correct: {is_correct}")
    
    response = {
        "correct": is_correct,
        "message": "Correct!" if is_correct else "Wrong. Try again!"
    }
    
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
