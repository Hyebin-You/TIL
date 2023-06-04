<template>
	<div class="iconlist-flex">
		<transition-group
			class="icons"
			v-if="IconList"
			tag="div"
			name="fade-move"
			mode="out-in"
			@enter="enter"
			@after-enter="afterEnter">
			<PublicIconListItem
				v-for="icon in IconList"
				:key="icon.id"
				:icon="icon" />
		</transition-group>
	</div>
</template>

<script>
import PublicIconListItem from "@/components/PublicIconListItem";
import axios from 'axios'

export default {
	name: "PublicIconList",
	components: {
		PublicIconListItem,
	},
	data() {
		return {
			IconList: null,
		};
	},
	methods: {
		enter(el) {
			el.style.transitionDelay = 200 + "ms";
		},
		afterEnter(el) {
			el.style.transitionDelay = "";
		},
		iconList() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/worlds/iconlists/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res.data);
          this.IconList = res.data;
        })
        .catch((err) => {
          console.log(err);
        })
		}
	},
	created() {
		this.iconList();
	}
};
</script>

<style scoped>
.icons {
	display: flex;
	width: 900px;
	flex-wrap: wrap;
	align-items: center;
	border-bottom: 3px white solid;
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
</style>
