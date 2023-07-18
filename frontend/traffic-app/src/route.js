import React, { useEffect, useState } from 'react';

function RouteMap() {
  const [mapHtml, setMapHtml] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/route/?start=Berlin,Germany&end=Munich,Germany')
      .then(response => response.json())
      .then(data => {
        setMapHtml(data.map);
      });
  }, []);

  return (
    <div>
      <iframe srcDoc={mapHtml} width="100%" height="600" />
    </div>
  );
}

export default RouteMap;
