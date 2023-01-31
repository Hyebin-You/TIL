import React from "react";
import styled from "styled-components";
import "./RoomItem.css";

const Wrapper = styled.div`
  width: 100%;
  height: 230px;
  border: 5px solid black;
`;

const TitleWrapper = styled.div`
  margin-top: 5%;
  width: 100%;
  height: 25%;
  text-align: center;
  flex-wrap: wrap;
  font-size: 20px;
`;

const TeamWrapper = styled.div`
  justify-content: center;
  width: 80%;
  height: 15%;
  text-align: center;
  border: 1px solid black;
  border-radius: 25px;
`;

const RoomItem = (props) => {
  return (
    <Wrapper>
      <TitleWrapper>{props.room.roomTitle}</TitleWrapper>
      <TeamWrapper></TeamWrapper>
    </Wrapper>
  );
};

export default RoomItem;
