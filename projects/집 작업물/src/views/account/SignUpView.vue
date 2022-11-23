<template>
  <div>
    <h1>SignUp</h1>
    <div class="login-box">
			<form @submit.prevent="signUp" class="form-box" action="">
				<input id="userid" placeholder="아이디 입력부탁!!" type="text" v-model="username"/>
				<input placeholder="비밀번호 !!" type="password" v-model="password1"/>
				<input placeholder="비밀번호 확인!!" type="password" v-model="password2"/>
				<input type="submit" value="회원가입">
			</form>
		</div>
    

  </div>
</template>

<script>

export default {
  name: 'SignUpView',
  components: {

  },
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;

      const payload = {
        username, password1, password2
      }

      if(password1 !== password2) {
        this.$swal('비밀번호가 일치하지 않습니다', '', 'warning');
        this.password1 = null;
        this.password2 = null;
        return
      } else {
        this.$store.dispatch('signUp', payload);
      }      
   }
  }
}
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