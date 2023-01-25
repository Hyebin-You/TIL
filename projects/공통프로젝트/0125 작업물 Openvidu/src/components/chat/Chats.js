import React, { Component } from "react";
import Chat from "./Chat";

// class Chats extends Component {
//   render() {
//     const { chats } = this.props;
//     return chats.map((chat) => {
//       <div>
//         <Chat text={chat.text} userNick={chat.userNick} />
//       </div>;
//     });
//   }
// }

const Chats = (props) => {
  const { chats } = props;
  return chats.map((chat) => {
    <div>
      <Chat text={chat.text} userNick={chat.userNick} />
    </div>;
  });
};

export default Chats;
