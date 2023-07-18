import React, { useState } from 'react';

function App() {
  const [mapHtml, setMapHtml] = useState('');
  const [start, setStart] = useState('');
  const [end, setEnd] = useState('');

  const handleSubmit = () => {
    fetch(`http://localhost:8000/route/?start=${start}&end=${end}`)
      .then(response => response.json())
      .then(data => {
        setMapHtml(data.map);
      });
  };

  return (
    <div className="App">
      <h1>Route Map</h1>
      <div>
        <input 
          type="text"
          value={start}
          onChange={e => setStart(e.target.value)}
          placeholder="Start location"
        />
        <input 
          type="text"
          value={end}
          onChange={e => setEnd(e.target.value)}
          placeholder="End location"
        />
        <button onClick={handleSubmit}>Submit</button>
      </div>
      <iframe srcDoc={mapHtml} width="100%" height="600" />
    </div>
  );
}

export default App;
