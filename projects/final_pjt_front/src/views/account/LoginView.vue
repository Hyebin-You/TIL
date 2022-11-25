<template>
	<div>
		<div class="img-box">
			<img src="@/assets/pinkcube.png" alt="gotcha">
		</div>
		<div class="login-box">
			<!-- <h2>Login</h2> -->
			<!-- <img src="@/assets/gotcha.png" alt="logo"> -->
			<form @submit.prevent="logIn">
				<div class="user-box">
					<input type="text" v-model="username" required="true" />
					<label>아이디</label>
				</div>
				<div class="user-box">
					<input type="password" v-model="password" required="true" />
					<label>비밀번호</label>
				</div>
				<div id="submit-box">
					<input type="submit" value="LogIn">
					<div @click="goToSignUp">SignUp</div>
				</div>
			</form>
		</div>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from "axios";

export default {
	name: "LoginView",
	data() {
		return {
			username: null,
			password: null,
		};
	},
	methods: {
		logIn() {
			axios({
				method: "post",
				url: `${API_URL}/accounts/login/`,
				data: {
					username: this.username,
					password: this.password,
				},
			})
				.then(res => {
					this.$store.commit("SAVE_TOKEN", res.data.key);
					this.$store.dispatch("userData");
					this.$router.push("index");
				})
				.catch(err => {
					console.log(err);
				});
		},
		goToSignUp() {
			this.$router.push("signup");
		},
	},
};
</script>

<style scoped>
.img-box {
	width: fit-content;
	position: absolute;
	top: 50%;
	left: 40%;
	padding: 40px;
	transform: translate(-50%, -50%);
}

.login-box {
  position: absolute;
  top: 50%;
  left: 58%;
  width: 400px;
  padding: 40px;
	padding-bottom: 10px;
  transform: translate(-50%, -50%);
  background: rgba(255, 255, 255, 0.08);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0,0,0,.6);
  border-radius: 10px;
}

.login-box #submit-box {
	display: flex;
	justify-content: flex-end;
	text-decoration: none;
}

.login-box img {
	width: 170px;
  margin: 0 0 30px;
  padding: 0;
  color: #fff;
  text-align: center;
}
.login-box .user-box {
  position: relative;
}

.login-box .user-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 16px;
  color: rgb(255, 255, 255);
  margin-bottom: 30px;
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  background: transparent;
}
.login-box .user-box label {
  position: absolute;
  top:0;
  left: 0;
  padding: 10px 0;
  font-size: 16px;
  color: rgb(255, 255, 255);
  pointer-events: none;
  transition: .5s;
}

.login-box .user-box input:focus ~ label,
.login-box .user-box input:valid ~ label {
  top: -20px;
  left: 0;
  color: rgb(250, 186, 207);
  font-size: 12px;
}

.login-box form #submit-box div {
	height: fit-content;
	padding: 0 10px;
  position: relative;
  display: inline-block;
  color: #fff;
  font-size: 16px;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: .5s;
  margin-top: 30px;
	margin-left: 5px;
	margin-right: 5px;
  letter-spacing: 1px;
}

.login-box form #submit-box input {
  position: relative;
  display: inline-block;
  color: #fff;
  font-size: 16px;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: .5s;
  margin-top: 30px;
	margin-left: 5px;
	margin-right: 5px;
  letter-spacing: 1px;
  padding: 5px 10px;
  margin-bottom: 30px;
  border: none;
  outline: none;
  background: transparent;
}


.login-box form #submit-box div:hover {
  background: rgba(248, 248, 248, 0.185);
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(255, 5, 89, 0.2),
              0 0 25px rgba(255, 5, 89, 0.2),
              0 0 50px rgba(255, 5, 89, 0.2),
              0 0 100px rgba(255, 5, 89, 0.2);
}
.login-box form #submit-box input:hover {
  background: rgba(248, 248, 248, 0.185);
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(255, 5, 89, 0.2),
              0 0 25px rgba(255, 5, 89, 0.2),
              0 0 50px rgba(255, 5, 89, 0.2),
              0 0 100px rgba(255, 5, 89, 0.2);
}

</style>
