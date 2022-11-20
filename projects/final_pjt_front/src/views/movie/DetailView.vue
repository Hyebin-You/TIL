<template>
	<div
		id="dropshadow"
		@click="detailOff"
		v-if="detailSwitch"
		class="dropshadow">
		<div class="detailbox">
			<h1>{{ Movie.title }}</h1>
			<div class="detail-flex">
				<DetailVideoContext />
				<DetailSideReview />
			</div>
			<DetailSameGenre style="margin: 0 auto; margin-top: 20px" />
		</div>
	</div>
</template>

<script>
import DetailVideoContext from "@/components/movie/detail/DetailVideoContext";
import DetailSideReview from "@/components/movie/detail/DetailSideReview";
import DetailSameGenre from "@/components/movie/detail/DetailSameGenre";

export default {
	name: "DetailView",
	components: {
		DetailVideoContext,
		DetailSideReview,
		DetailSameGenre,
	},
	data() {
		return {};
	},
	computed: {
		detailSwitch() {
			console.log("switch", this.$store.state.detailSwitch);
			return this.$store.state.detailSwitch;
		},
		Movie() {
			return this.$store.state.detailMovie;
		},
	},
	methods: {
		detailOff(event) {
			if (event.target.id === "dropshadow") {
				const bodyScroll = document.querySelector('body');
				bodyScroll.style.overflow = 'scroll';
				this.$store.state.detailSwitch = false;
			}
		},
	},
};
</script>

<style>
.detail-flex {
	display: flex;
	justify-content: space-evenly;
}

.dropshadow {
	width: 100vw;
	height: 110%;
	background-color: rgba(0, 0, 0, 0.8);
	display: flex;
	justify-content: center;
	align-items: center;
	position: absolute;
	top: -100px;
	z-index: 10;
}

.detailbox {
	position: fixed;
	top: 100px;
	background-color: plum;
	width: 1200px;
	height: 800px;

	font-family: Roboto;
	font-family:"Noto Sans KR";
	font-family: "Apple SD Gothic Neo";
	font-family: "Nanum Gothic";
	font-family: Roboto, "Noto Sans KR", "Apple SD Gothic Neo", "Nanum Gothic",
		"Malgun Gothic", sans-serif;
	font-family: Roboto, "Noto Sans KR", "Apple SD Gothic Neo", "Nanum Gothic",
		"Malgun Gothic", sans-serif;
	font-family: Roboto, "Noto Sans KR", "Apple SD Gothic Neo", "Nanum Gothic",
		"Malgun Gothic", sans-serif;
}
</style>
