import { useState } from 'react'
import './App.css'
import { Routes,Route } from "react-router-dom";
import Login from './pages/Login.jsx'
import StudentReg from "./pages/StudentReg";

function App() {
  const [count, setCount] = useState(0)

  return (
    <Routes>
      <Route path='/'element={<Login/>}/>
      <Route path='/StudentReg' element={<StudentReg/>} />
      {/* <Route path='/WardenReg' element={<WardenReg/>} /> */}
    </Routes>
  )
}

export default App
