<template>
  <div>
    <h1>SignUp</h1>
    <div class="login-box">
			<form @submit.prevent="goNick" class="form-box" action="">
				<input id="userid" placeholder="아이디 입력부탁!!" type="text" />
				<input placeholder="비밀번호 !!" type="text" />
				<input placeholder="비밀번호 확인!!" type="text" />
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

    }
  },
  methods: {
    goNick() {
      this.$router.push({ name: 'nickname'});
    }
  }
}
</script>

<style>

</style>