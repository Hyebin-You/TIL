<template>
  <div v-if="icon" @click="buyIcon" class="icon-box">
    <img :src="require(`@/assets/${icon.img_path}`)" alt="slime">
  </div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from 'axios'

export default {
  name: 'PublicIconListItem',
  props: {
    icon: Object,
  },
  computed: {
    userObject() {
      return this.$store.state.userObject;
    }
  },
  methods: {
    buyIcon() {
      const result = confirm(
      `정말로 ${this.icon.name}을 구매하시겠습니까?


      보유포인트 : ${this.userObject.point}
      Icon 가격 : ${this.icon.price}`);
      if (!result) {
        return
      }

      const existIcon = this.userObject.icons.some((userIcon) => {
        return userIcon.id === this.icon.id;
      })
    
      if (existIcon) {
        this.$swal('이미 보유중인 아이콘 입니다.','', 'warning')
      } else {
        if (this.userObject.point >= this.icon.price) {
          axios({
            method: 'post',
            url: `${API_URL}/accounts/buy_icon/`,
            data: {
              'price': this.icon.price,
              'icon_id': this.icon.id,
            },
            headers: {
              Authorization: `Token ${this.$store.state.token}`
            }
          })
            .then((res) => {
              console.log(res);
              this.$store.dispatch('userData');
              this.$swal('아이콘이 구매되었습니다.', '', 'success')
            })
            .catch((err) => {
              console.log(err);
            })
        } else {
          this.$swal('보유하신 포인트가 부족합니다.');
      }
      }


    }
  }
}
</script>

<style scoped>
.icon-box {
  width: 100px;
  height: 100px;
  margin: 10px;
  border: 4px solid whitesmoke;
  border-radius: 10px;
  box-sizing: border-box;
}
.icon-box:hover {
  cursor: pointer;
  transform: scale(1.1);
  transition: all 0.5s;
}

.icon-box > img {
  width: 100%;
  height: 100%;
}

</style>