<template>
  <div>
    <h3>ProfileIconList</h3>
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
        url: `http://127.0.0.1:8000/accounts/change_usericon/`,
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
	width: 900px;
	flex-wrap: wrap;
	align-items: center;

}
.iconlist-flex {
  display: flex;
  justify-content: center;
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
  width: 60px;
  height: 60px;
  margin: 10px;
  border: 1px solid whitesmoke;
  border-radius: 10px;
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