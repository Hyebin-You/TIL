import axios from "axios";
import React, { Component } from "react";
import RoomItem from "./RoomItem";
import { Grid } from "@mui/material";
import styled from "styled-components";

const RoomContainer = styled.div`
  align-items: center;
`;

class RoomList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      rooms: [],
    };
  }

  componentDidMount() {
    axios
      .get("https://i8e107.p.ssafy.io:8443/openvidu/api/sessions", {
        headers: {
          Authorization: `Basic ${btoa(`OPENVIDUAPP:MY_SECRET`)}`,
        },
      })
      .then((response) => {
        console.log(response.data.content);
        const info = response.data.content.map((room) => {
          const roomTitle = room.customSessionId;
          const peopleNum = room.connections.numberOfElements;

          return { roomTitle, peopleNum, roomNum: 1, isopened: true };
        });
        console.log(info);
        this.setState({ rooms: info });
      });
  }

  render() {
    return (
      <RoomContainer>
        <Grid container spacing={6}>
          {this.state.rooms.map((room, i) => {
            return (
              <Grid
                item
                xs={3}
                style={{
                  justifyContent: "center",
                  alignItems: "center",
                  paddingTop: 40,
                  paddingLeft: 20,
                  paddingBottom: 20,
                  paddingRight: 20,
                }}
                key={i}
              >
                <RoomItem room={room}></RoomItem>
              </Grid>
            );
          })}
        </Grid>
      </RoomContainer>
    );
  }
}

export default RoomList;
