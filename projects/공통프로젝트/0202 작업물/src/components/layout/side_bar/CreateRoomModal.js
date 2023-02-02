import { useState, useContext } from "react";
import Modal from "../../UI/Modal";
import Button from "../../UI/Button";
// import GameContext from "../../../store/game-context";
import InfoContext from "../../../store/infoContext";
import { useNavigate } from "react-router-dom";

const CreateRoom = () => {
  // 네비게이션을 위한 함수
  const navigate = useNavigate();

  // 게임방 관련 데이터 컨텍스트
  const gameCtx = useContext(InfoContext);

  // 모달을 열고 닫는 함수
  const [modalOpen, setModalOpen] = useState(false);
  const openModal = () => {
    setModalOpen(true);
  };
  const closeModal = () => {
    setModalOpen(false);
  };

  // const { makeroom } = useContext(GameContext);

  const [roomTitle, setRoomTitle] = useState("");
  const [teamTitle, setTeamTitle] = useState("");
  const [isopened, setIsopened] = useState(true);
  const [roomPassword, setRoomPassword] = useState(undefined);
  const [ischecked, setIschecked] = useState(false);

  const handleRoomTitleChange = (event) => {
    setRoomTitle(event.target.value);
  };

  const handleTeamTitleChange = (event) => {
    setTeamTitle(event.target.value);
    console.log(teamTitle);
  };

  const handleIsopenedChange = () => {
    setIsopened(!isopened);
  };

  const handleIscheckedChange = (event) => {
    setIschecked(!ischecked);
    handleIsopenedChange();
  };

  const handleRoomPasswordChange = (event) => {
    setRoomPassword(event.target.value);
  };

  const handleMakeRoom = () => {
    console.log("방 만들기");
    gameCtx.makeRoom(roomTitle, teamTitle, isopened, roomPassword);
    console.log(gameCtx.roomId);
  };

  return (
    <div>
      {/* 방 생성 모달 */}
      <Button onClick={openModal}>방 생성</Button>
      <Modal
        open={modalOpen}
        close={closeModal}
        header="게임 방 생성"
        isfooter={false}
      >
        {/* Modal.js <main> {props.children} </main>에 내용이 입력된다. 리액트 함수형 모달 */}
        <p>
          방 제목 : <input type="text" onChange={handleRoomTitleChange} />
        </p>
        <p>
          팀 명 : <input type="text" onChange={handleTeamTitleChange} />
        </p>
        <p>
          <label>
            비밀방{" "}
            <input
              type="checkbox"
              checked={ischecked}
              onChange={handleIscheckedChange}
            />
          </label>
        </p>
        {!isopened ? (
          <p>
            비밀번호 : <input type="text" onChange={handleRoomPasswordChange} />
          </p>
        ) : null}
        <button onClick={() => navigate("/gameroom", { roomInfo: teamTitle })}>
          게임방 생성
        </button>
        <button onClick={handleMakeRoom}>게임방 생성</button>
      </Modal>
    </div>
  );
};

export default CreateRoom;
