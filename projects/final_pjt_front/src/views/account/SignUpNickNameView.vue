<template>
  <dir>
    <h3>SignUpNickName</h3>
    <div class="login-box">
			<form @submit.prevent="goGenre" class="form-box" action="">
				<input placeholder="닉네임 입력부탁!!" type="text" />
				<input type="submit" value="선택">
			</form>
		</div>
  </dir>
</template>

<script>
export default {
  name: 'SignUpNickNameView',
  methods: {
    goGenre(event) {
      console.log('##', event);
      this.$router.push({ name: 'likegenre' });
    }
  }
}
</script>

<style>

</style>