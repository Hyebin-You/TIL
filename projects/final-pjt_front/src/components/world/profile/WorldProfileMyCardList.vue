<template>
	<div>
		<div class="likelist-title">{{ userObject.nickname }}님이 보유하신 카드목록</div>
		<div class="flex-box">
			<div class="container">
				<carousel
					:items="7"
					:autoplay="false"
					:nav="true"
					:dots="false"
					>
					<WorldDeckCard
						v-for="card in userObject.usercard_set"
						:key="card.name"
						:card="card"
						class="eventhover" />
				</carousel>
			</div>
		</div>
	</div>
</template>

<script>
import carousel from "vue-owl-carousel";
import WorldDeckCard from "@/components/world/profile/WorldDeckCard";


export default {
	name: "WorldProfileMyCardList",
	components: {
		carousel,
		WorldDeckCard,
	},
	data() {
		return {
			myCardList: null,
		}
	},
	computed: {
		userObject() {
			return this.$store.state.userObject;
		}
	},
	mounted() {
		this.addArrow();
	},
	methods: {
		addArrow() {
			// console.log("addarrow", eventName);
			const nextBtnList = document.querySelectorAll(".owl-prev");
			const prevBtnList = document.querySelectorAll(".owl-next");

			nextBtnList.forEach(btn => {
				btn.innerText = "»";
			});
			prevBtnList.forEach(btn => {
				btn.innerText = "«";
			});
		},
	},


};
</script>

<style scoped>

.eventhover {
	width: 200px;
  height: 300px;
	transform: scale(0.9);
}
.flex-box {
	display: flex;
	justify-content: center;
	align-items: center;
}

.container {
	width: 1350px;
	max-height: 350px;

}
.likelist-title {
  font-size: 25px;
	text-align: start;
} 



.owl-next {
	font-size: 60px !important;
	position: absolute;
	left: -50px;
	top: 100px;
	background: none !important;
}

.owl-prev {
	font-size: 60px !important;
	position: absolute;
	right: -50px;
	top: 100px;
	background: none !important;
	transition: all 1s;
}
.owl-item {
	position: relative;
	display: flex;
	justify-content: center;
	align-items: center;
	/* margin: 0px -100px; */
}

.marginbox {
	margin-left: 200px;
}

.eventhover:hover {
	cursor: pointer;
	transform: scale(1);
	transition: all 1s;
}

</style>
