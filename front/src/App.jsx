import React, { useState, useEffect } from 'react';
import KMeans from 'kmeans-js';

const App = () => {
  const [file, setFile] = useState(null);
  const [data, setData] = useState([]);
  const [clusteredData, setClusteredData] = useState([]);

  useEffect(() => {
    if (data.length > 0) {
      const numClusters = 3;
      const inputData = Object.keys(data[0].answer).map((key) => [data[0].answer[key], data[0].labels[key]]);
      const kmeans = new KMeans();
      const clusters = kmeans.cluster(inputData, { K: numClusters });
      const clusteredData = Object.keys(data[0].answer).map((key, index) => ({
        answer: data[0].answer[key],
        labels: data[0].labels[key],
        cluster: clusters[index].centroidIndex,
      }));
      setClusteredData(clusteredData);
    }
  }, [data]);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('https://dafe-212-46-18-171.ngrok-free.app/upload', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const data = await response.json();
        if (Array.isArray(data) && data.length > 0 && data[0].answer && data[0].labels) {
          setData(data);
          console.log('File uploaded successfully');
        } else {
          console.error('Invalid data structure');
        }
      } else {
        console.error('File upload failed');
      }
    } catch (error) {
      console.error('Error occurred while uploading file:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {clusteredData.length > 0 && (
        <div>
          <h2>Clustering Results</h2>
          {clusteredData.map((item, index) => (
            <div key={index}>
              <p>Answer: {item.answer}</p>
              <p>Labels: {item.labels}</p>
              <p>Cluster: {item.cluster}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default App;