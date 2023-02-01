import React, { Component } from "react";
import OpenViduVideoComponent from "./OvVideo";
import styled from "styled-components";
import "./UserVideoComponent.css";

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

class UserVideoComponent extends Component {
  getNicknameTag() {
    return JSON.parse(this.props.streamManager.stream.connection.data)
      .clientData;
  }

  render() {
    return (
      <div className="video">
        {this.props.streamManager !== undefined ? (
          <StreamComponent>
            <OpenViduVideoComponent streamManager={this.props.streamManager} />
            <NickTag>{this.getNicknameTag()}</NickTag>
          </StreamComponent>
        ) : null}
      </div>
    );
  }
}

export default UserVideoComponent;
