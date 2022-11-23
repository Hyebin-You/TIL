<template>
  <dir>
    <h3>SignUpNickName</h3>
    <div class="login-box">
			<form @submit.prevent="signUpNick" class="form-box">
				<input placeholder="닉네임 입력부탁!!" type="text" v-model="nickName" maxlength="8"/>
				<input type="submit" value="선택">
			</form>
		</div>
  </dir>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUpNickNameView',
  data() {
    return {
      nickName: null,  
    } 
  },
  methods: {
    signUpNick() {
      // console.log('닉생성오냐', this.nickName);
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/set_nickname/`,
        data: {
          'nickname': this.nickName,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          // console.log('닉생성성공이염', res);
          this.$router.push({ name: 'likegenre' });
        })
        .catch((err) => {
          alert('중복입니다!!');
        })
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