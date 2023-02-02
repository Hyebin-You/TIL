import { createContext, useState } from "react";

const InfoContext = createContext({
  roomId: "",
  roomTitle: "",
  teamTitle: "",
  isopened: true,
  roomPassword: "",
  makeRoom: () => {},
  enterPublic: () => {},
  enterPrivate: () => {},
});

export const InfoProvider = ({ children }) => {
  const makeRoom = (roomTitle, teamTitle, isopened, roomPassword) => {
    console.log("됬냐");
    setState((prevState) => ({
      ...prevState,

      roomTitle,
      teamTitle,
      isopened,
      roomPassword,
    }));
  };

  const enterPublic = (roomId, roomTitle, teamTitle) => {
    setState((prev) => ({ ...prev, roomId, roomTitle, teamTitle }));
  };

  const enterPrivate = (
    roomId,
    roomTitle,
    teamTitle,
    isopened,
    roomPassword
  ) => {
    setState((prevState) => ({
      ...prevState,
      roomId,
      roomTitle,
      teamTitle,
      isopened,
      roomPassword,
    }));
  };

  const initialState = {
    roomId: "",
    roomTitle: "",
    teamTitle: "",
    isopened: true,
    roomPassword: "",
    makeRoom,
    enterPublic,
    enterPrivate,
  };

  const [state, setState] = useState(initialState);

  return <InfoContext.Provider value={state}>{children}</InfoContext.Provider>;
};

export default InfoContext;
