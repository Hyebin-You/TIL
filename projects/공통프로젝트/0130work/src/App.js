import { Routes, Route } from "react-router-dom";
import "./App.css";
import GameRoom from "./components/video/GameRoom";
import Lobby from "./components/lobby/Lobby";

function App() {
  const home = {
    roomId: "sessionA",
    nickname: "닉네임",
  };

  const room = {
    roomId: "sessionB",
    nickname: "두번째 방",
  };
  const room1 = {
    roomId: "sessionC",
    nickname: "두번째 방",
  };
  const room2 = {
    roomId: "sessionD",
    nickname: "두번째 방",
  };
  const room3 = {
    roomId: "sessionE",
    nickname: "두번째 방",
  };
  const room4 = {
    roomId: "dsagsdlkjklawejglk",
    nickname: "두번째 방",
  };
  const room5 = {
    roomId: "한글로제발",
    nickname: "두번째 방",
  };

  return (
    <div>
      <Routes>
        <Route path="/lobby" element={<Lobby />} />
        <Route path="/game" element={<GameRoom home={home} />} />
        <Route path="/game1" element={<GameRoom home={room} />} />
        <Route path="/game2" element={<GameRoom home={room1} />} />
        <Route path="/game3" element={<GameRoom home={room2} />} />
        <Route path="/game4" element={<GameRoom home={room3} />} />
        <Route path="/game5" element={<GameRoom home={room4} />} />
        <Route path="/game6" element={<GameRoom home={room5} />} />
      </Routes>
    </div>
  );
}

export default App;
