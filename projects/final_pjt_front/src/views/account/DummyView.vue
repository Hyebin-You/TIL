<template>
	<div>
		<h1>dummy</h1>
		<div class="carousel-wrapper">
			<carousel
				:perPage="8"
				:loop="true"
				:navigation-enabled="true"
				:navigationNextLabel="'»'"
				:navigationPrevLabel="'«'"
				:adjustableHeight="false"
				:paginationEnabled="false"
				:navigationClickTargetSize="15"
				:center-mode="true">
				<slide
					data-index="0"
					data-name="MySlideName"
					v-for="movie in randomList"
					:key="movie.id">
					<MovieItem :movie="movie" class="eventhover" />
				</slide>
			</carousel>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import { Carousel, Slide } from "vue-carousel";
import MovieItem from "@/components/movie/MovieItem";
export default {
	name: "DummyView",
	components: {
		Carousel,
		Slide,
		MovieItem,
	},
	data() {
		return {
			randomList: [],
		};
	},
	created() {
		axios({
			method: "get",
			url: "http://127.0.0.1:8000/movies/search/random",
		})
			.then(res => {
				console.log(`beforec${this.randomList.length},${res.data.length}`);
				this.randomList = res.data;
				console.log("es@@@@@@@@@", res);
			})
			.catch(err => {
				console.log("error!!!!!", err);
			});
	},
};
</script>

<style scoped>
.img-size {
	max-width: 100%;
}

.carousel-wrapper {
	min-width: 90%;
	max-width: 90%;
	padding: 0 20px;
	margin: auto;
}

.VueCarousel-navigation-prev,
.VueCarousel-navigation-next {
	color: #fff !important;
	font-size: 60px;
	cursor: pointer;
	border-radius: 3px;
}
</style>