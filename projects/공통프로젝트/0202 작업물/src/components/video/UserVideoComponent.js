import React, { Component } from "react";
import OpenViduVideoComponent from "./OvVideo";
import styled from "styled-components";
import "./UserVideoComponent.css";
import AlarmImage from "../../assets/alarm.png";

const StreamComponent = styled.div`
  position: relative;
`;

const NickTag = styled.div`
  background-color: white;
  position: absolute;
  top: 0;
  left: 0;
  margin-left: 10px;
`;

const Warning = styled.div`
  position: absolute;
  top: 25px;
  right: -80px;
  width: 100px;
  background-color: rgba(128, 128, 128, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
`;

class UserVideoComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isActive: false,
    };

    this.handleIsActive = this.handleIsActive.bind(this);
  }

  getNicknameTag() {
    return JSON.parse(this.props.streamManager.stream.connection.data)
      .clientData;
  }

  handleIsActive() {
    this.setState({ isActive: !this.state.isActive });
  }

  render() {
    return (
      <div className="video">
        {this.props.streamManager !== undefined ? (
          <StreamComponent>
            <OpenViduVideoComponent streamManager={this.props.streamManager} />
            <NickTag>{this.getNicknameTag()}</NickTag>
            <img
              src={AlarmImage}
              className="alert"
              alt="신고/강퇴 버튼"
              onClick={this.handleIsActive}
            />
            <Warning className={this.state.isActive ? "active" : "notActive"}>
              <ul>
                <li>신고하기</li>
                <li>강퇴</li>
              </ul>
            </Warning>
          </StreamComponent>
        ) : null}
      </div>
    );
  }
}

export default UserVideoComponent;
