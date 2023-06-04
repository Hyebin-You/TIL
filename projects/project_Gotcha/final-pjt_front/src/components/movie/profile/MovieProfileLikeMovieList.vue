<template>
	<div>
		<div class="likelist-title">{{ userObject.nickname }}님이 좋아요 하신 영화목록</div>
		<div class="container">
			<carousel
				:items="7"
				:autoplay="false"
				:nav="true"
				:dots="false"
				>
				<MovieItem
					v-for="movie in userObject.like_movies"
					:key="movie.id"
					:movie="movie"
					class="eventhover" />
			</carousel>
		</div>
	</div>
</template>

<script>
import carousel from "vue-owl-carousel";
import MovieItem from "@/components/movie/MovieItem";


export default {
	name: "MovieProfileLikeMovieList",
	components: {
		carousel,
		MovieItem,
	},
	data() {
		return {
			myMovieList: null,
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
	max-width: 200px;
	transform: scale(0.9);
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
