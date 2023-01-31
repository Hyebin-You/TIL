import axios from "axios";
import React, { Component } from "react";
import RoomItem from "./RoomItem";
import { Grid } from "@mui/material";

class RoomList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      rooms: [],
    };
  }

  componentDidMount() {
    axios
      .get("https://i8e107.p.ssafy.io/openvidu/api/sessions", {
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
      <div id="Room-container">
        <Grid container spacing={6}>
          {this.state.rooms.map((room, i) => {
            return (
              <Grid item xs={3} style={{ justifyContent: "center" }} key={i}>
                <RoomItem room={room}></RoomItem>
              </Grid>
            );
          })}
        </Grid>
      </div>
    );
  }
}

export default RoomList;
