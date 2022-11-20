<template>
	<div>
		<h1>Login</h1>
		<div class="login-box">
			<form @submit.prevent="goIndex" class="form-box" action="">
				<input id="userid" placeholder="아이디 입력부탁!!" type="text" />
				<input placeholder="비밀번호 !!" type="text" />
				<input type="submit" value="로그인">
			</form>
		</div>
	</div>
</template>

<script>
export default {
	name: "LoginView",
	components: {},
	methods: {
		goIndex() {
			this.$router.push('index');
		}
	}
};
</script>

<style >
.login-box {
	display: flex;
	justify-content: center;
	align-items: center;
	
}

.form-box {
	border: 1px solid plum;
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
