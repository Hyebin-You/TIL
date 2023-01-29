import React, { Component, createRef } from "react";
import { OpenVidu } from "openvidu-browser";
import axios from "axios";
import UserVideoComponent from "./UserVideoComponent";
import UnityGame from "./UnityGame";
import "./GameRoom.css";
import jQuery from "jquery";
window.$ = window.jQuery = jQuery;

const OPENVIDU_SERVER_URL = "http://localhost:4443/";
const APPLICATION_SERVER_URL = "http://localhost:5000/";
const OPENVIDU_SERVER_SECRET = "MY_SECRET";

class GameRoom extends Component {
  constructor(props) {
    super(props);

    this.state = {
      mySessionId: props.home.roomId,
      myUserNick: props.home.nickname,
      session: undefined,
      mainStreamManager: undefined,
      publisher: undefined,
      subscribers: [],
      status: "stand",
      count: 0,
      webcam: new tmPose.Webcam(600, 600, true),
      model: undefined,
      chats: [],
      chat: "",
      token: undefined,
      videostate: true,
      audiostate: false,
      ishost: false,
      chaton: false,
      myRef: createRef({}),
    };

    this.joinSession = this.joinSession.bind(this);
    this.leaveSession = this.leaveSession.bind(this);
    this.handleChatMessageChange = this.handleChatMessageChange.bind(this);
    this.sendChatByClick = this.sendChatByClick.bind(this);
    this.sendChatByEnter = this.sendChatByEnter.bind(this);
    this.handleMainVideoStream = this.handleMainVideoStream.bind(this);
    this.startButton = this.startButton.bind(this);
    this.loop = this.loop.bind(this);
    this.start = this.start.bind(this);
    this.init = this.init.bind(this);
    this.predict = this.predict.bind(this);
    this.chattoggle = this.chattoggle.bind(this);
  }

  componentDidMount() {
    setTimeout(() => {
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
    this.OV = new OpenVidu();

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
            subscribers: subscribers,
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

        this.getToken().then((token) => {
          mySession
            .connect(token, { clientData: this.state.myUserNick })
            .then(async () => {
              this.updateHost().then((firstUser) => {
                const host = JSON.parse(firstUser).clientData;

                if (this.state.myUserNick === host) {
                  this.setState({ ishost: true });
                }
              });
              let publisher = await this.OV.initPublisherAsync(undefined, {
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
            });
        });
      }
    );
  }

  updateHost() {
    return new Promise((resolve, reject) => {
      window.$.ajax({
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
    console.log(this.state.model);
    setTimeout(() => {
      this.setState({
        count: 0,
        status: "stand",
      });
      this.init();
    }, 3000);
  }

  chattoggle() {
    this.setState({ chaton: !this.state.chaton });
  }

  startButton() {
    let mySession = this.state.session;
    // axios 요청을 back으로 보낼지 말지
    // 참고용 자료에서는 back으로 게임 중이라는 상태를 보냈음
  }

  leaveSession() {
    const mySession = this.state.session;
    if (mySession) {
      mySession.disconnect();
    }
    // back으로 axios요청을 보내 방 정보 갱신
    // back에서는 현재 방 인원수가 1명일때 방 관리하는 곳에서 방을 삭제하고
    // 1명보다 많을 때는 방의 인원수를 한명 줄인다.
    this.OV = null;
    this.setState({
      session: "",
      subscribers: [],
      mySessionId: "",
      mainStreamManager: undefined,
      publisher: undefined,
    });

    this.props.history.push("/");
  }

  async setmodel() {
    // const URL = "https://teachablemachine.withgoogle.com/models/UQcyvhIye/";
    // 내가 학습시킨 간단한 스쿼트 모델
    // const modelURL =
    //   "https://teachablemachine.withgoogle.com/models/UQcyvhIye/model.json";
    // const metadataURL =
    //   "https://teachablemachine.withgoogle.com/models/UQcyvhIye/metadata.json";

    // 동섭이 학습데이터 바탕으로 제작한 모델
    const modelURL =
      "https://teachablemachine.withgoogle.com/models/M7lirMMFj/model.json";
    const metadataURL =
      "https://teachablemachine.withgoogle.com/models/M7lirMMFj/metadata.json";

    this.setState({
      model: await tmPose.load(modelURL, metadataURL),
    });

    // const a = await tmPose.load(metadataURL, modelURL);
    // console.log(a);
  }

  async init() {
    // this.setState({ webcam: new tmPose.Webcam(size, size, flip) });
    await this.state.webcam.setup();
    console.log(this.state.webcam);
    this.state.webcam.play();
    window.requestAnimationFrame(this.loop);
  }

  async loop() {
    this.state.webcam.update();
    await this.predict();
    window.requestAnimationFrame(this.loop);
  }

  // prediction[0] is squat, prediction[1] is stand
  async predict() {
    const { pose, posenetOutput } = await this.state.model.estimatePose(
      this.state.webcam.canvas
    );

    const prediction = await this.state.model.predict(posenetOutput);
    if (prediction[0].probability.toFixed(2) >= 0.9) {
      this.setState({ status: "stand" });
      if (this.state.status === "squat") {
        this.setState({ count: 1 });
        this.setState({ status: "stand" });
      }
    } else if (prediction[1].probability.toFixed(2) >= 0.9) {
      this.setState({ status: "squat" });
    }

    if (this.state.count === 1) {
      await this.sendKey();
      this.setState({ count: 0 });
    }
  }

  async sendKey() {
    console.log("공격 신호 보낸다");
    this.state.myRef.current.sendAttack();
  }

  async getToken() {
    const sessionId = await this.createSession(this.state.mySessionId);
    return await this.createToken(sessionId);
  }

  async createSession(sessionId) {
    const response = await axios.post(
      APPLICATION_SERVER_URL + "api/sessions",
      { customSessionId: sessionId },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    return response.data;
  }

  async createToken(sessionId) {
    const response = await axios.post(
      APPLICATION_SERVER_URL + "api/sessions/" + sessionId + "/connections",
      {},
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    return response.data;
  }

  render() {
    const chats = this.state.chats;
    // const myRef = useRef({})

    return (
      <div>
        <button onClick={this.start}>start</button>
        {this.state.session !== undefined ? (
          <div id="session">
            <div id="video-container1" className="video-container">
              {this.state.publisher !== undefined ? (
                <div
                  className="stream-container"
                  onClick={() =>
                    this.handleMainVideoStream(this.state.publisher)
                  }
                >
                  <UserVideoComponent streamManager={this.state.publisher} />
                </div>
              ) : null}
              {this.state.subscribers[0] !== undefined ? (
                <div
                  className="stream-container"
                  onClick={() =>
                    this.handleMainVideoStream(this.state.subscribers[0])
                  }
                >
                  <UserVideoComponent
                    streamManager={this.state.subscribers[0]}
                  />
                </div>
              ) : null}
            </div>
            <UnityGame data={this.predict} ref={this.state.myRef} />
            <div id="video-container2" className="video-container">
              {this.state.subscribers[1] !== undefined ? (
                <div
                  className="stream-container"
                  onClick={() =>
                    this.handleMainVideoStream(this.state.subscribers[1])
                  }
                >
                  <UserVideoComponent
                    streamManager={this.state.subscribers[1]}
                  />
                </div>
              ) : null}
              {this.state.subscribers[2] !== undefined ? (
                <div
                  className="stream-container"
                  onClick={() =>
                    this.handleMainVideoStream(this.state.subscribers[2])
                  }
                >
                  <UserVideoComponent
                    streamManager={this.state.subscribers[2]}
                  />
                </div>
              ) : null}
            </div>
          </div>
        ) : null}
      </div>
    );
  }
}

export default GameRoom;
