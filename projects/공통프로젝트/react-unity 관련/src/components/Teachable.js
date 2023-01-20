import React, { Component } from "react";
import * as tmPose from "@teachablemachine/pose";

class Teachable extends Component {
  constructor(props) {
    super(props);
    this.state = {
      webcam: undefined,
      model: undefined,
      status: "stand",
      count: 0,
      check: false,
    };
  }

  async setmodel() {
    const modelURL = "../squatModel/model.json";
    const metadataURL = "../squatModel/metadata.json";
    this.setState({
      model: await tmPose.load(modelURL, metadataURL),
    });
  }

  // setState에서 undefinded 관련 에러 발생 해결해야 함
  async init() {
    const size = 200;
    const flip = true;
    this.setState({ webcam: new tmPose.Webcam(size, size, flip) });
    await this.state.webcam.setup();
    await this.state.webcam.play();
    window.requestAnimationFrame(this.loop);
  }

  async loop() {
    this.state.webcam.update();
    await this.predict();
    window.requestAnimationFrame(this.loop);
  }

  async sendKey() {
    console.log("공격 인식");
  }

  async predict() {
    const { pose, posenetOutput } = await this.state.model.estimatePose(
      this.state.webcam.canvas
    );
    const prediction = await this.state.model.predict(posenetOutput);

    if (prediction[2].probability.toFixed(2) >= 0.9) {
      if (this.state.status === "jump") {
        this.setState({ count: 1 });
        this.setState({ status: "stand" });
      }
    }

    if (prediction[3].probability.toFixed(2) >= 0.9) {
      this.setState({ status: "jump" });
    }

    if (this.state.count === 1) {
      await this.sendKey();
      this.setState({ count: 0 });
    }
  }

  render() {
    return (
      <div>
        <button onClick={this.init}>start game</button>
      </div>
    );
  }
}

export default Teachable;
