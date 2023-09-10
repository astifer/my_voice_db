import React, { useState, useEffect } from 'react';
import KMeans from 'kmeans-js';

const App = () => {
  const [file, setFile] = useState(null);
  const [data, setData] = useState([]);
  const [clusteredData, setClusteredData] = useState([]);

  useEffect(() => {
    if (data.answer && data.text_labels && data.labels) {
      const numClusters = 3;
      const inputData = Object.keys(data.answer).map((key) => [
        data.answer[key],
        data.labels[key],
      ]);
      const kmeans = new KMeans();
      const clusters = kmeans.cluster(inputData, { K: numClusters });
      const clusteredData = Object.keys(data.answer).map((key, index) => ({
        answer: data.answer[key],
        labels: data.text_labels[key],
        cluster: data.labels[key],
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
        const responseData = await response.json();
        const { answer, labels, text_labels } = responseData;

        if (answer && labels && text_labels) {
          setData({ answer, labels, text_labels });
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

  const groupByCluster = () => {
    const groupedData = clusteredData.reduce((result, item) => {
      if (!result[item.cluster]) {
        result[item.cluster] = [];
      }
      result[item.cluster].push(item);
      return result;
    }, {});
    return Object.values(groupedData);
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>

      {clusteredData.length > 0 && (
        <div style={styles.containingContainer}>
          <h2>результат кластеризации</h2>
          {groupByCluster().map((cluster, index) => (
            <div key={index} style={styles.clusterContainer}>
              {cluster.map((item, itemIndex) => (
                <div key={itemIndex} style={styles.itemContainer}>
                  <p>Ответ: {item.answer}</p>
                  <p>Кластер: {item.labels}</p>
                </div>
              ))}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

const styles = {

  containingContainer:{
  },
  clusterContainer: {
    display:'flex',
    justifyContent:'flex-start',
    flexDirection:'row',
    flexWrap:'wrap',
    marginBottom: '10px',
    padding: '5px',
    border: '1px solid #ccc',
    borderRadius: '5px',
    backgroundColor:''
  },
  clusterHeader: {
    width:'full',
    fontSize: '18px',
    fontWeight: 'bold',
    marginBottom: '5px',
  },
  itemContainer: {
    marginBottom: '5px',
    padding: '5px',
    margin:'5px',
    border: '1px solid #eee',
    borderRadius: '3px',
    backgroundColor: '#f9f9f9',
  },
};

export default App;