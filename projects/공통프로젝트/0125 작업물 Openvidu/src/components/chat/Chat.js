import React, { Component } from "react";
import "./Chat.module.css";

class Chat extends Component {
  render() {
    const { text, userNick } = this.props;

    return (
      <div className="Mcontainer">
        <p>{userNick}</p>
        <p>{text}</p>
      </div>
    );
  }
}
