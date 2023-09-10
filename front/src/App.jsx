import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  
  const uploadFile = async(file) =>{
    
    await fetch('https://dafe-212-46-18-171.ngrok-free.app/upload', {
      // content-type header should not be specified!
      method: 'POST',
      Headers: {'Content-Type': 'multipart/form-data',
               'accept': 'application/json'
               },
      body: {file},
    })
      .then(response => response.json())
      .then(success => {
        console.log(success)
      })
      .catch(error => console.log(error)
    );
  }
  return(
    <>
      <form>
          <input type="file" id='myinput' onSubmit={uploadFile}></input>
        <button type="submit">Convert</button>
      </form>
    </>
  )
}

export default App
