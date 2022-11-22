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
				v-for="(icon, index) in IconList"
				:key="index"
				:icon="icon" />
		</transition-group>
	</div>
</template>

<script>
import PublicIconListItem from "@/components/PublicIconListItem";


export default {
	name: "PublicIconList",
	components: {
		PublicIconListItem,
	},
	data() {
		return {
			IconList: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
		};
	},
	methods: {
		enter(el) {
			el.style.transitionDelay = 200 + "ms";
		},
		afterEnter(el) {
			el.style.transitionDelay = "";
		},
	},
};
</script>

<style>
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
</style>
