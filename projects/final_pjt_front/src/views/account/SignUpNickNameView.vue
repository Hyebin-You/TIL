<template>
	<dir>
		<!-- <div class="login-box">
			<form @submit.prevent="signUpNick" class="form-box">
				<input placeholder="닉네임 입력부탁!!" type="text" v-model="nickName" maxlength="8"/>
				<input type="submit" value="선택">
			</form>
		</div> -->
		<div class="login-box">
			<form @submit.prevent="signUpNick">
				<div class="user-box">
					<input type="text" v-model="nickName" maxlength="8" required="true" />
					<label>닉네임</label>
				</div>
				<div id="submit-box2">
					<input type="submit" value="SELECT" />
				</div>
			</form>
		</div>
		<div class="img-box">
			<img src="@/assets/pinkcube.png" alt="gotcha" />
		</div>
	</dir>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from "axios";

export default {
	name: "SignUpNickNameView",
	data() {
		return {
			nickName: null,
		};
	},
	computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		},
	},
	created() {
		{
			if (!this.isLogin) {
				this.$router.push({ name: "login" });
			}
		}
	},
	methods: {
		signUpNick() {
			// console.log('닉생성오냐', this.nickName);
			axios({
				method: "post",
				url: `${API_URL}/accounts/set_nickname/`,
				data: {
					'nickname': this.nickName,
				},
				headers: {
					Authorization: `Token ${this.$store.state.token}`,
				},
			})
				.then(res => {
					// console.log('닉생성성공이염', res);
					this.$router.push({ name: "likegenre" });
				})
				.catch(err => {
					this.$swal("닉네임 중복입니다!!", "", "warning");
				});
		},
	},
};
</script>

<style scoped>
.img-box {
	width: fit-content;
	position: absolute;
	top: 46%;
	left: 42%;
	padding: 40px;
	transform: translate(-50%, -50%);
}

.login-box {
	position: absolute;
	top: 50%;
	left: 58%;
	width: 400px;
	padding: 40px;
	padding-bottom: 30px;
	transform: translate(-50%, -50%);
	background: rgba(255, 255, 255, 0.08);
	box-sizing: border-box;
	box-shadow: 0 15px 25px rgba(0, 0, 0, 0.6);
	border-radius: 10px;
}

.login-box #submit-box2 {
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
	top: 0;
	left: 0;
	padding: 10px 0;
	font-size: 16px;
	color: rgb(255, 255, 255);
	pointer-events: none;
	transition: 0.5s;
}

.login-box .user-box input:focus ~ label,
.login-box .user-box input:valid ~ label {
	top: -20px;
	left: 0;
	color: rgb(250, 186, 207);
	font-size: 12px;
}

.login-box form #submit-box2 div {
	height: fit-content;
	padding: 0 10px;
	position: relative;
	display: inline-block;
	color: #fff;
	font-size: 16px;
	text-decoration: none;
	text-transform: uppercase;
	overflow: hidden;
	transition: 0.5s;
	margin-top: 40px;
	margin-left: 5px;
	margin-right: 5px;
	letter-spacing: 1px;
}

.login-box form #submit-box2 input {
	position: relative;
	display: inline-block;
	color: #fff;
	font-size: 16px;
	text-decoration: none;
	text-transform: uppercase;
	overflow: hidden;
	transition: 0.5s;
	margin-top: 20px;
	margin-left: 5px;
	margin-right: 5px;
	letter-spacing: 1px;
	padding: 5px 10px;
	border: none;
	outline: none;
	background: transparent;
}

.login-box form #submit-box2 div:hover {
	background: rgba(248, 248, 248, 0.185);
	color: #fff;
	border-radius: 5px;
	box-shadow: 0 0 5px rgba(255, 5, 89, 0.2), 0 0 25px rgba(255, 5, 89, 0.2),
		0 0 50px rgba(255, 5, 89, 0.2), 0 0 100px rgba(255, 5, 89, 0.2);
}
.login-box form #submit-box2 input:hover {
	background: rgba(248, 248, 248, 0.185);
	color: #fff;
	border-radius: 5px;
	box-shadow: 0 0 5px rgba(255, 5, 89, 0.2), 0 0 25px rgba(255, 5, 89, 0.2),
		0 0 50px rgba(255, 5, 89, 0.2), 0 0 100px rgba(255, 5, 89, 0.2);
}
</style>
