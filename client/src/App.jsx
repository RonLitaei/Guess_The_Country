import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [sessionId, setSessionId] = useState('')
  const [clues, setClues] = useState([])
  const [guess, setGuess] = useState('')
  const [feedback, setFeedback] = useState(null)
  const [loading, setLoading] = useState(false)
  const [gameOver, setGameOver] = useState(false)

  // Start a new game on mount
  useEffect(() => {
    startNewGame()
  }, [])

  const startNewGame = async () => {
    setLoading(true)
    setFeedback(null)
    setGameOver(false)
    setGuess('')
    try {
      const response = await fetch('http://localhost:8000/api/game/new')
      const data = await response.json()
      setSessionId(data.session_id)
      setClues([data.clue])
    } catch (error) {
      console.error('Error starting game:', error)
      alert('Could not connect to the backend. Make sure it is running on port 8000.')
    } finally {
      setLoading(false)
    }
  }

  const unlockClue = async () => {
    if (clues.length >= 3) return
    
    setLoading(true)
    try {
      const response = await fetch(`http://localhost:8000/api/game/clue?session_id=${sessionId}`)
      const data = await response.json()
      setClues([...clues, data.clue])
    } catch (error) {
      console.error('Error unlocking clue:', error)
    } finally {
      setLoading(false)
    }
  }

  const submitGuess = async (e) => {
    e.preventDefault()
    if (!guess.trim()) return

    setLoading(true)
    try {
      const response = await fetch('http://localhost:8000/api/game/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: sessionId, guess })
      })
      const data = await response.json()
      setFeedback(data)
      setGameOver(true)
    } catch (error) {
      console.error('Error submitting guess:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <h1>Guess The Country</h1>
      <p className="subtitle">Test your geography knowledge with three clues.</p>

      <div className="game-area">
        <div className="clues-container">
          {clues.map((clue, index) => (
            <div key={index} className="clue-card" style={{ animationDelay: `${index * 0.1}s` }}>
              <div className="clue-label">Clue {index + 1}</div>
              <div className="clue-text">{clue}</div>
            </div>
          ))}
        </div>

        {!gameOver ? (
          <form className="guess-section" onSubmit={submitGuess}>
            <input 
              type="text" 
              placeholder="Enter country name..." 
              value={guess}
              onChange={(e) => setGuess(e.target.value)}
              disabled={loading}
              autoFocus
            />
            <div className="button-group">
              <button 
                type="button" 
                className="btn-secondary" 
                onClick={unlockClue}
                disabled={loading || clues.length >= 3}
              >
                {clues.length < 3 ? `Unlock Clue ${clues.length + 1}` : 'All Clues Unlocked'}
              </button>
              <button 
                type="submit" 
                className="btn-primary" 
                disabled={loading || !guess.trim()}
              >
                Submit Guess
              </button>
            </div>
          </form>
        ) : (
          <div className="action-bar">
            <button className="btn-primary" onClick={startNewGame}>
              Play Again
            </button>
          </div>
        )}

        {feedback && (
          <div className={`feedback ${feedback.correct ? 'correct' : 'wrong'}`}>
            {feedback.message}
          </div>
        )}
      </div>
    </div>
  )
}

export default App
