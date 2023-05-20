import { React, useState, useEffect } from "react";
import Note from "./components/Note";

import "./App.scss";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import About from "./pages/About";
import Favourites from "./pages/Favourites";
import Nav from "./components/navbar";
import axios from "axios";

export default function App() {
  return (
    <Router>
      <div className="App">
        <Nav />
        <Routes>
          <Route path="/" exact element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/favourites" element={<Favourites />} />
        </Routes>
      </div>
    </Router>
  );
}

function Home() {
  const [notes, setNotes] = useState([]);
  useEffect(() => {
    console.log("effect");
    axios.get("http://localhost:3001/results").then((response) => {
      console.log("promise fulfilled");
      setNotes(response.data);
    });
  }, []);

  console.log(notes.Title);

  return (
    <div>
      <ul>
        {notes.map((note) => (
          <Note key={note.Title} note={note} />
        ))}
      </ul>
    </div>
  );
}
