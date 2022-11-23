<template>
	<div>
		<h1>Login</h1>
		<div class="login-box">
			<form @submit.prevent="logIn" class="form-box">
				<input id="userid" placeholder="아이디 입력" v-model="username" type="text" />
				<input placeholder="비밀번호 입력" v-model="password" type="password" />
				<input type="submit" value="로그인">
				<input @click="goToSignUp" type="submit" value="회원가입">
			</form>
		</div>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: "LoginView",
	data() {
		return {
			username: null,
			password: null,
		}
	},
	methods: {
		logIn() {
			axios({
				method: 'post',
				url: `http://127.0.0.1:8000/accounts/login/`,
				data: {
					'username': this.username,
					'password': this.password,
				},
				})
					.then((res) => {
						this.$store.commit('SAVE_TOKEN', res.data.key);
						this.$store.dispatch('userData');
						this.$router.push('index');
					})
					.catch((err) => {
						console.log(err);
					})

		},
		goToSignUp() {
			this.$router.push('signup');
		}
	}
};
</script>

<style scoped>
.login-box {
	display: flex;
	justify-content: center;
	align-items: center;
	
}

.form-box {
	border: 1px solid #260712;
	width: 500px;
	height: 400px;
	display: flex;
	justify-content: center;
	flex-direction: column;
}


.form-box > input {
	margin: 0 auto;
	margin-bottom: 10px;
	box-sizing: border-box;
	border: none;
	/* outline: none; */
	width: 250px;
	padding: 5px;
	border-radius: 10px;
}



</style>
