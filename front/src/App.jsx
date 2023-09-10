import React, { useState } from 'react';
import { KMeans } from 'node-kmeans';

const App = () => {
  const [file, setFile] = useState(null);
  const [metrics, setMetrics] = useState(null);
  const [clusteredData, setClusteredData] = useState([]);

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
        setMetrics(data);
        console.log('File uploaded successfully');

        // Выполняем кластеризацию данных
        const numClusters = 3;
        const inputData = data.map((item) => [item.answer, item.labels]);
        const kmeans = new KMeans({ k: numClusters });
        const clusters = data.cluster(inputData);
        const clusteredData = data.map((item, index) => ({
          ...item,
          cluster: clusters[index].clusterIndex,
        }));
        setClusteredData(clusteredData);
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
              <p>Label: {item.labels}</p>
              <p>Cluster: {item.cluster}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default App;
