import { Routes, Route } from "react-router-dom";
import "./App.css";
import GameRoom from "./components/video/GameRoom";
import Lobby from "./components/lobby/Lobby";

function App() {
  const home = {
    roomId: "sessionA",
    nickname: "닉네임,",
  };

  return (
    <div>
      <Routes>
        <Route path="/lobby" element={<Lobby />} />
        <Route path="/game" element={<GameRoom home={home} />} />
      </Routes>
    </div>
  );
}

export default App;
