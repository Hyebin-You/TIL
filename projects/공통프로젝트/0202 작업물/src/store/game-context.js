import React, { useState } from "react";
import axios from "axios";

const GameContext = React.createContext({
  roomId: "",
  roomTitle: "",
  teamTitle: "",
  isopened: true,
  roomPassword: "",
  makeroom: (roomTitle, teamTitle, isopened, roomPassword) => {},
  enterPublicRoom: () => {},
  enterPrivateRoom: () => {},
});

export const GameContextProvider = (props) => {
  const APPLICATION_SERVER_URL = "http://localhost:5000/";
  const [roomId, setRoomId] = useState("");
  const [roomTitle, setRoomTitle] = useState("");
  const [teamTitle, setTeamTitle] = useState("");
  const [isopened, setIsopened] = useState(true);
  const [roomPassword, setRoomPassword] = useState(undefined);

  const makeRoom = (roomTitle, teamTitle, isopened, roomPassword) => {
    console.log("makeroom");
    axios
      .post(
        APPLICATION_SERVER_URL + "api/rooms",
        {},
        {
          headers: {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST",
          },
        }
      )
      .then((response) => {
        setRoomId(response);
        setRoomTitle(roomTitle);
        setTeamTitle(teamTitle);
        setIsopened(isopened);
        setRoomPassword(roomPassword);
        console.log(response);
      });
  };

  const enterPublicRoom = (roomId, roomTitle, teamTitle) => {
    setRoomId(roomId);
    setRoomTitle(roomTitle);
    setTeamTitle(teamTitle);
  };

  const enterPrivateRoom = (
    roomId,
    roomTitle,
    teamTitle,
    isopened,
    roomPassword
  ) => {
    setRoomId(roomId);
    setRoomTitle(roomTitle);
    setTeamTitle(teamTitle);
    setIsopened(isopened);
    setRoomPassword(roomPassword);
  };

  const contextValue = {
    roomId: roomId,
    roomTitle: roomTitle,
    teamTitle: teamTitle,
    isopened: isopened,
    roomPassword: roomPassword,
    makeroom: makeRoom,
    enterPublicRoom: enterPublicRoom,
    enterPrivateRoom: enterPrivateRoom,
  };

  const [state, setState] = useState(contextValue);

  return (
    <GameContext.Provider value={state}>{props.children}</GameContext.Provider>
  );
};

export default GameContext;
