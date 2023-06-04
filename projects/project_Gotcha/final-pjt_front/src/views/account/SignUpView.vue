<template>
	<div>
		<div class="login-box">
			<form @submit.prevent="signUp">
				<div class="user-box">
					<input type="text" v-model="username" required="true" />
					<label>아이디</label>
				</div>
				<div class="user-box">
					<input type="password" v-model="password1" required="true" />
					<label>비밀번호</label>
				</div>
        <div class="user-box">
					<input type="password" v-model="password2" required="true" />
					<label>비밀번호 확인</label>
				</div>
				<div id="submit-box3">
					<input type="submit" value="SignUp" />
				</div>
			</form>
		</div>
		<div class="img-box">
			<img src="@/assets/pinkcube.png" alt="gotcha" />
		</div>
	</div>
</template>

<script>
export default {
	name: "SignUpView",
	components: {},
	data() {
		return {
			username: null,
			password1: null,
			password2: null,
		};
	},
	methods: {
		signUp() {
			const username = this.username;
			const password1 = this.password1;
			const password2 = this.password2;

			const payload = {
				username,
				password1,
				password2,
			};

			if (password1 !== password2) {
				this.$swal("비밀번호가 일치하지 않습니다", "", "warning");
				this.password1 = null;
				this.password2 = null;
				return;
			} else {
				this.$store.dispatch("signUp", payload);
			}
		},
	},
};
</script>

<style scoped>
.img-box {
	width: fit-content;
	position: absolute;
	top: 50%;
	left: 63%;
	padding: 40px;
  transform: translate(-50%, -50%);
}

.login-box {
  position: absolute;
  top: 50%;
  left: 45%;
  width: 400px;
  padding: 40px;
  padding-bottom: 30px;
  transform: translate(-50%, -50%);
  background: rgba(255, 255, 255, 0.08);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0,0,0,.6);
  border-radius: 10px;
}

.login-box #submit-box3 {
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

.login-box form #submit-box3 div {
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
  margin-top: 40px;
	margin-left: 5px;
	margin-right: 5px;
  letter-spacing: 1px;
}

.login-box form #submit-box3 input {
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
  margin-bottom: 10px;
  border: none;
  outline: none;
  background: transparent;
}


.login-box form #submit-box3 div:hover {
  background: rgba(248, 248, 248, 0.185);
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(255, 5, 89, 0.2),
              0 0 25px rgba(255, 5, 89, 0.2),
              0 0 50px rgba(255, 5, 89, 0.2),
              0 0 100px rgba(255, 5, 89, 0.2);
}
.login-box form #submit-box3 input:hover {
  background: rgba(248, 248, 248, 0.185);
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(255, 5, 89, 0.2),
              0 0 25px rgba(255, 5, 89, 0.2),
              0 0 50px rgba(255, 5, 89, 0.2),
              0 0 100px rgba(255, 5, 89, 0.2);
}



/* .login-box {
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
	/* width: 250px;
	padding: 5px;
	border-radius: 10px;
} */ 
</style>
