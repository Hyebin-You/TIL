import { useState } from "react";
import Modal from "../../UI/Modal";
import { useNavigate } from "react-router-dom";

const CreateRoom = () => {
  // 네비게이션을 위한 함수
  const navigate = useNavigate();

  // 모달을 열고 닫는 함수
  const [modalOpen, setModalOpen] = useState(false);
  const openModal = () => {
    setModalOpen(true);
  };
  const closeModal = () => {
    setModalOpen(false);
  };

  const [roomTitle, setRoomTitle] = useState("");

  const getTitle = (event) => {
    setRoomTitle(event.target.value);
  };

  const [nickname, setNickname] = useState("");

  const getNickname = (event) => {
    setNickname(event.target.value);
  };

  return (
    <div>
      {/* 방 생성 모달 */}
      <button onClick={openModal}>방 생성</button>
      <Modal
        open={modalOpen}
        close={closeModal}
        header="게임 방 생성"
        isfooter={false}
      >
        {/* Modal.js <main> {props.children} </main>에 내용이 입력된다. 리액트 함수형 모달 */}
        <p>
          방 제목 : <input type="text" onChange={getTitle} />
        </p>
        <p>
          닉네임 : <input type="text" onChange={getNickname} />
        </p>
        <p>
          비밀번호 : <input type="text" />
        </p>

        <button onClick={() => navigate("/gameroom", { roomTitle, nickname })}>
          게임방 생성
        </button>
      </Modal>
    </div>
  );
};

export default CreateRoom;
