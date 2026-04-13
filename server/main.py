from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import random
import uuid
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("game.log")
    ]
)
logger = logging.getLogger("guess-the-country")

app = FastAPI(title="Guess The Country API")


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
# In a real app, this would be in Redis or a DB
sessions = {}

class GuessRequest(BaseModel):
    session_id: str
    guess: str

@app.get("/api/game/new")
async def start_new_game():
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
async def get_next_clue(session_id: str):
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
async def reveal_answer(session_id: str):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[session_id]
    logger.info(f"Answer Revealed | Session: {session_id} | Answer: {session['country_name']}")
    return {

        "answer": session["country_name"],
        "message": f"The correct answer was {session['country_name']}."
    }

@app.post("/api/game/guess")
async def submit_guess(request: GuessRequest):
    if request.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = sessions[request.session_id]
    correct_name = session["country_name"].lower()
    user_guess = request.guess.strip().lower()
    
    is_correct = user_guess == correct_name
    
    logger.info(f"Guess Submitted | Session: {request.session_id} | Guess: '{request.guess}' | Correct: {is_correct}")
    
    response = {

        "correct": is_correct,
        "message": "Correct!" if is_correct else "Wrong. Try again!"
    }
    
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
