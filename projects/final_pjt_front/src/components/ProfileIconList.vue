<template>
  <div>
    <div class="iconlist-title">{{userObject.nickname}}님의 보유 아이콘</div>
    <div class="iconlist-flex">
		<transition-group
			class="icons"
			v-if="userObject.icons"
			tag="div"
			name="fade-move"
			mode="out-in"
			@enter="enter"
			@after-enter="afterEnter">
      <div
        @click="changeUserIcon(icon)"
        class="icon-box"
        v-for="icon in userObject.icons"
        :key="icon.id">
        <img :src="require(`@/assets/${icon.img_path}`)" alt="icon">
        </div>
      </transition-group>
    </div>
  </div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from 'axios'

export default {
  name: 'ProfileIconList',
  computed: {
    userObject() {
      return this.$store.state.userObject;
    }
  },
  methods: {
		enter(el) {
			el.style.transitionDelay = 200 + "ms";
		},
		afterEnter(el) {
			el.style.transitionDelay = "";
		},
    changeUserIcon(icon) {
      axios({
        method: 'put',
        url: `${API_URL}/accounts/change_usericon/`,
        data: {
          'img_url': icon.img_path
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.$store.dispatch('userData');

        })
        .catch((err) => {
          console.log(err);
        })
    }
  }
}
</script>

<style scoped>
.icons {
	display: flex;
	width: 1000px;
	flex-wrap: wrap;
	align-items: center;
  justify-content: flex-start;

}
.iconlist-flex {
  display: flex;
  justify-content: center;
}
.iconlist-title {
  font-size: 25px;
  text-align: start;
}


.fade-move-enter-active {
	transition: all 0.5s ease-out;
}
.fade-move-enter {
	transform: translateX(50px);
	opacity: 0;
}
.fade-move-leave {
	opacity: 0;
}
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