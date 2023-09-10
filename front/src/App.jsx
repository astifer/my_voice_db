import React, { useState, useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Accordion from 'react-bootstrap/Accordion';
import { ListGroup } from 'react-bootstrap';
import Spinner from 'react-bootstrap/Spinner';


const App = () => {
  const [file, setFile] = useState(null);
  const [data, setData] = useState([]);
  const [clusteredData, setClusteredData] = useState({});
  const [badData, setBadData] = useState([])
  const [numberOfDivs, setNumberOfDivs] = useState(1);
  const [divColors, setDivColors] = useState([]);

  const [loading, setLoading] = useState(false);

  const generateUniqueColors = async() => {
    const colors = [];
    for (let i = 0; i < numberOfDivs; i++) {
      const randomColor = getRandomColor();
      colors.push(randomColor);
    }
    setDivColors(colors);
    
  };

  const getRandomColor = () => {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 12)];
    }
    return color;
  };

  useEffect(() => {
    if (data.answer && data.text_labels && data.labels) {
      const inputData = Object.keys(data.answer).map((key) => [
        data.answer[key],
        data.labels[key],
      ]);

      
      const clusteredData = {}
      
      Object.keys(data.answer).map((key, index) => {
        const cluster = data.text_labels[key];
        if(cluster in clusteredData){
          clusteredData[cluster].push(data.answer[key])
        }else{
          clusteredData[cluster] = [data.answer[key]]
        }
      
    });
      
      generateUniqueColors();
      setClusteredData(clusteredData);
      
    }
  }, [data]);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleErrors = async () => {
    // setClusteredData({})
    setLoading(true);
    try{
      await fetch('https://useful-kite-settled.ngrok-free.app/get_errors', {method:'GET', headers: new Headers({
        "ngrok-skip-browser-warning": "69420",
      }),})
        .then(response=> response.json())
        .then(data=>{
          let texts = []
          Object.keys(data.text).map((key, index)=>{
            texts.push(data.text[key])
          })
          setBadData(texts)
          setLoading(false)
        })
        .catch(e=>console.log(e))

    } catch(e){
      console.log(e)
    }
  }

  const handleUpload = async () => {
    setBadData([])
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('https://useful-kite-settled.ngrok-free.app/upload', {
        method: 'POST',
        body: formData,
        headers: new Headers({
          "ngrok-skip-browser-warning": "69420",
        })
      });

      if (response.ok) {
        const responseData = await response.json();
        const { answer, labels, text_labels } = responseData;

        if (answer && labels && text_labels) {
          setData({ answer, labels, text_labels });
          const clusters = [];
          Object.keys(labels).map((key, index)=>{
            if (clusters.indexOf(key.labels) === -1) {
              clusters.push(labels[key])
            }
          })
          setNumberOfDivs(clusters.length)
          console.log('File uploaded successfully');
          setLoading(false)
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
    <div style={{margin:'2%'}}>
      <Container>
        <Form>
          <Form.Label>Загрузите JSON</Form.Label>
          <Form.Control  type="file" onChange={handleFileChange}></Form.Control > 
        </Form>
        

        <Button style={{marginTop:'1%'}} variant="primary" onClick={handleUpload}>Показать кластеризацию</Button>
        <Button style={{marginTop:'1%', marginLeft:'5%'}} variant="warning" onClick={handleErrors} disabled={Object.keys(clusteredData).length > 0 ? false : true}>Показать нежелательные ответы</Button>
      </Container>
      

      {Object.keys(clusteredData).length > 0 && (
      <div className="justify-content-md-center" style={{marginTop:'1%'}} >
        <Row style={styles.containingContainer}>
          
          {Object.keys(clusteredData).map((cluster, index) => {
            // console.log(cluster)
            const clusterColor = divColors[index]; 
            
            // styles.clusterContainer.backgroundColor = divColors[index];
            return (
            <Col  sm={clusteredData[cluster].length-1} key={index} >

              <Accordion className='rounded' style={{backgroundColor: clusterColor, margin: '0.3%'}}>
              <Accordion.Header  eventKey={index}><p className='text-bold' style={{color:clusterColor}}>{cluster.toUpperCase()}</p></Accordion.Header>

                  <Accordion.Body eventKey={index}>

                      {clusteredData[cluster].map((item, itemIndex) => (
                        <div key={itemIndex}>
                          <p className='text-white' style={{fontSize:'110%'}}>{item}</p>
                        </div>
                      ))}
                    
                  </Accordion.Body>

              </Accordion>
            </Col>
          )})}
        </Row>
      </div>
      )}

      {badData.length > 0 && (
        <ListGroup>
          <h3 style={{marginTop:'2%'}}>Нежелательные слова</h3>
          {badData.map((bad, index)=>(
            <ListGroup.Item style={{color:'black', fontSize:'110%'}}>{bad}</ListGroup.Item>
          ))}
        </ListGroup>
      )}

      {loading && (
        <Container style={{marginLeft:'50%', marginTop:'10%'}}>
          <Spinner ></Spinner>
        </Container>
        
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
    // border: '1px solid #ccc',
    borderRadius: '5px',
    // backgroundColor:'red'
  },
  clusterHeader: {
    width:'full',
    fontSize: '18px',
    fontWeight: 'bold',
    marginBottom: '5px',
  },
  itemContainer: {
    // marginBottom: '5px',
    // padding: '5px',
    // margin:'5px',
    // border: '1px solid #eee',
    // borderRadius: '3px',
    // backgroundColor: '#f9f9f9',
  },
};

export default App;