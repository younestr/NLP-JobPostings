import React, { useState } from 'react';
import './App.css';

function App() {
  const [jobText, setJobText] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/classify', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: jobText }),
      });
      const data = await response.json();
      setPrediction(data.prediction);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <h1>Job Posting Classification</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="Enter the job posting text"
          value={jobText}
          onChange={(e) => setJobText(e.target.value)}
        />
        <button type="submit">Classify</button>
      </form>
      {prediction && (
        <div>
          <h2>Prediction: {prediction}</h2>
        </div>
      )}
    </div>
  );
}

export default App;
