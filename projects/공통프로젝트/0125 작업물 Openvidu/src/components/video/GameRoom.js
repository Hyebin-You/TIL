import React, { Component } from "react";
import { Openvidu } from "openvidu-browser";
import axios from "axios";
import UserVideoComponent from "./UserVideoComponent";

const OPENVIDU_SERVER_URL = "http://localhost:4443/";
const OPENVIDU_SERVER_SECRET = "MY_SECRET";

class GameRoom extends Component {
  constructor(props) {
    super(props);

    this.state = {
      mySessionId: undefined,
      myUserNick: undefined,
      session: undefined,
      mainStreamManager: undefined,
      publisher: undefined,
      subscribers: [],
      status: "stand",
      count: 0,
      webcam: undefined,
      model: undefined,
      chats: [],
      chat: "",
      token: undefined,
      videostate: true,
      audiostate: false,
      ishost: false,
      chaton: false,
    };
  }

  componentDidMount() {
    setTimeout(() => {
      const { home } = this.props;
      const { token, roomId, nickname } = home;
      if (roomId === "") {
        // this.props.history.push('/error')
      }
      this.setState({
        token,
        mySessionId: roomId,
        myUserNick: nickname,
      });
      this.setmodel();
      this.joinSession();
    }, 500);
  }

  componentDidUpdate(previousProps, previousState) {
    if (this.refs.chatoutput != null) {
      this.refs.chatoutput.scrollTop = this.refs.chatoutput.scrollHeight;
    }
  }

  handleChatMessageChange(e) {
    this.setState({
      chat: e.target.value,
    });
  }

  sendChatByClick() {
    this.setState({
      chats: [
        ...this.state.chats,
        {
          userNick: this.state.myUserNick,
          text: this.state.chat,
          chatClass: "messages__item--operator",
        },
      ],
    });
    const mySession = this.state.session;

    mySession.signal({
      data: `${this.state.myUserNick}, ${this.state.chat}`,
      to: [],
      type: "chat",
    });

    this.setState({
      chat: "",
    });
  }

  sendChatByEnter(e) {
    if (e.key === "Enter") {
      this.setState({
        chats: [
          ...this.state.chats,
          {
            userNick: myUserNick,
            text: this.state.chat,
            chatClass: "messages__item--operator",
          },
        ],
      });
      const mySession = this.state.session;

      mySession.signal({
        data: `${this.state.myUserNick}, ${this.state.chat}`,
        to: [],
        type: "chat",
      });

      this.setState({
        chat: "",
      });
    }
  }

  handleMainVideoStream(stream) {
    if (this.state.mainStreamManager !== stream) {
      this.setState({
        mainStreamManager: stream,
      });
    }
  }

  deleteSubscriber(streamManager) {
    let subscribers = this.state.subscribers;
    let index = subscribers.indexOf(streamManager, 0);
    if (index > -1) {
      subscribers.splice(index, 1);
      this.setState({ subscribers });
    }
  }

  joinSession() {
    this.OV = new Openvidu();

    this.setState(
      {
        session: this.OV.initSession(),
      },
      () => {
        let mySession = this.state.session;
        mySession.on("streamCreated", (event) => {
          let subscriber = mySession.subscribe(event.stream, undefined);
          let subscribers = this.state.subscribers;
          subscribers.push(subscriber);
          this.setState({
            subscribers,
          });
        });
        mySession.on("signal:start", (event) => {
          this.start();
        });
        mySession.on("signal:chat", (event) => {
          let chatdata = event.data.split(",");
          if (chatdata[0] !== this.state.myUserNick) {
            this.setState({
              chats: [
                ...this.state.chats,
                {
                  userNick: chatdata[0],
                  text: chatdata[1],
                  chatClass: "messages__item--visitor",
                },
              ],
            });
          }
        });
        mySession.on("streamDestroyed", (event) => {
          this.updateHost().then((clientData) => {
            const host = JSON.parse(clientData).clientData;

            mySession
              .signal({
                data: host,
                to: [],
                type: "update-host",
              })
              .then(() => {});
          });
        });
        mySession.on("signal:update-host", (event) => {
          if (this.state.myUserNick === event.data) {
            this.setState({ ishost: true });
          }
        });
        mySession.on("exception", (exception) => {});

        this.getToken()
          .then((token) => {
            mySession
              .connect(token, { clientData: this.state.myUserNick })
              .then(() => {
                this.updateHost().then((firstUser) => {
                  const host = JSON.parse(firstUser).clientData;

                  if (this.state.myUserNick === host) {
                    this.setState({ ishost: true });
                  }
                });
              });

            let publisher = this.OV.initPublisher(undefined, {
              audioSource: undefined,
              videoSource: undefined,
              publishAudio: false,
              publishVideo: true,
              resolution: "640x480",
              frameRate: 30,
              insertMode: "APPEND",
              mirror: false,
            });

            mySession.publish(publisher);

            this.setState({
              mainStreamManager: publisher,
              publisher,
            });
          })
          .catch((error) => {});
      }
    );
  }

  updateHost() {
    return new Promise((resolve, reject) => {
      $.ajax({
        type: "GET",
        url: `${"http://localhost:4443/api/sessions/"}${
          this.state.mySessionId
        }/connection`,
        headers: {
          Authorization: `Basic ${btoa(
            `OPENVIDUAPP:${OPENVIDU_SERVER_SECRET}`
          )}`,
        },
        success: (response) => {
          let content = response.content;
          content.sort((a, b) => a.createAt - b.createdAt);

          resolve(content[0].clientData);
        },
        error: (error) => reject(error),
      });
    });
  }

  start() {
    setTimeout(() => {
      this.setState({
        count: 0,
        status: "stand",
      });
      this.init();
    }, 5000);
  }

  chattoggle() {
    this.setState({ chaton: !this.state.chaton });
  }

  startButton() {
    let mySession = this.state.session;
  }
}

export default GameRoom;
