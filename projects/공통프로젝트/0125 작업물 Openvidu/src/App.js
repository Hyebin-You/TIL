import { Routes, Route } from "react-router-dom";
import "./App.css";
// import GameRoom from "./components/video/GameRoom";
import Lobby from "./components/lobby/Lobby";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/lobby" element={<Lobby />} />
      </Routes>
    </div>
  );
}

export default App;
