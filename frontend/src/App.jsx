import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { Navigate, Route, Routes } from "react-router-dom";
import FRR from "./pages/FRR";
import Layout from "./Layout";
function App() {
  return (
    <>
      <Routes>
     
       
        <Route element={<Layout />}>
        
          <Route path="/" element={<FRR />} />
      
        </Route>
       
      </Routes>
    </>
  );
}

export default App;
