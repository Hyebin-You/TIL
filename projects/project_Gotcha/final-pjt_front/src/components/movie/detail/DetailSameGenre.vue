<template>
	<div class="detail-same">
		<div class="container" v-if="genreList">
			<p>비슷한 장르의 영화가 많아요!</p>
			<div v-for="movie in genreList" :key="movie.id">
				<MovieItem :movie="movie" class="eventhover" />
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
// import carousel from "vue-owl-carousel";
import MovieItem from "@/components/movie/MovieItem";

export default {
	name: "DetailSameGenre",
	components: {
		// carousel,
		MovieItem,
	},
	data() {
		return {
			genreList: null,
		};
	},
	props: {
		movieGenres: Array,
	},
	watch: {
		movieGenres() {
			// console.log("테스트", this.movieGenres);
			const first = _.sample(this.movieGenres);
			const { name: selectedGenre } = first;
			// console.log("@!#!@@@", selectedGenre);

			axios({
				method: "get",
				url: `http://127.0.0.1:8000/movies/search/genre?genre=${selectedGenre}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }				
			})
				.then(res => {
					// console.log("!@#!@#!@#!", res.data);
					this.genreList = _.sampleSize(res.data, 5);
				})
				.catch(err => {
					console.log("error!!!!!", err);
				});
		},
	},

	created() {
		const first = _.sample(this.movieGenres);
		const { name: selectedGenre } = first;
		// console.log("@!#!@@@", selectedGenre);

		axios({
			method: "get",
			url: `http://127.0.0.1:8000/movies/search/genre?genre=${selectedGenre}/`,
			headers: {
				Authorization: `Token ${this.$store.state.token}`
			}			
		})
			.then(res => {
				// console.log("!@#!@#!@#!", res.data);
				this.genreList = _.sampleSize(res.data, 5);
			})
			.catch(err => {
				console.log("error!!!!!", err);
			});
	},
};
</script>

<style scoped>
.detail-same {
	width: 100%;
	height: 170px;
}

.eventhover {
	max-width: 150px;
	transform: scale(0.9);
	margin: auto;
}
.container {
	width: 100%;
	height: 170px;
	display: flex;
	justify-content: center;
}
.container > div {
	width: 150px;
	height: 170px;
}
.container > p {
	position: absolute;
	z-index: 20;
	font-size: 20px;
	left: 150px;
	bottom: 210px;
}

.owl-next {
	font-size: 60px !important;
	position: absolute;
	left: -50px;
	top: 20px;
	background: none !important;
}

.owl-prev {
	font-size: 60px !important;
	position: absolute;
	right: -50px;
	top: 20px;
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

.eventhover:hover {
	cursor: pointer;
	transform: scale(1);
	transition: all 1s;
}
.text-hidden > p {
	font-size: 10px;
}
</style>
