<template>
	<div class="test" @click="showDetail">
		<img
			:src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`"
			alt="movie" />
		<!-- <img src="@/assets/movie.jpg" :alt="movie" /> -->
		<div class="text-hidden">
			<p>{{ movie.title }}</p>
			<div>
				<span v-for="genre in movie.genres" :key="genre.name">{{ genre.name }}</span>
			</div>
		</div>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from 'axios'

export default {
	name: "MovieItem",
	props: {
		movie: Object,
	},
	methods: {
    showDetail() {
			const bodyScroll = document.querySelector('body');
			bodyScroll.style.overflow = 'hidden';
			// TODO: Vuestyle로 수정
			axios({
				methods: 'get',
				url: `${API_URL}/movies/movie_detail/${this.movie.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }				
			})
				.then((res) => {
					// console.log('!!!!!!!!!!!!!', res.data);
					this.$store.commit('SHOW_DETAIL', res.data);
				})
				.catch((err) => {
					console.log(err);
				})
    }
  },
	// created() {
	// 	this.$store.state.detailSwitch = false;
	// }
};
</script>

<style scoped>
@font-face {
	font-family: "maplestory";
	src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/MaplestoryOTFBold.woff")
		format("woff");
	font-weight: normal;
	font-style: normal;
}

.text-hidden {
	display: flex;
	align-items: center;
	justify-content: center;
	flex-direction: column;
	width: 100%;
	height: 100%;
	opacity: 0;
	background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.9) 100%);
	/* background-color: rgba(0, 0, 0, 0.7); */
	cursor: pointer;
	position: absolute;
	top: 0%;
	left: 0%;
}

.text-hidden:hover {
	opacity: 1;
	color: white;
	transition: all 1s;
	/* background-image: brightness(0.5); */
}

.text-hidden > p {
	max-width: 150px;
	font-size: 18px;
	font-weight: 800;
	padding-top: 150px;
	/* padding-top: 200px; */
	/* text-align: left; */
	word-break: break-all;
}
img {
	width: 100%;
	border-radius: 5px;
}
.text-hidden > div > span{
	/* margin-top: 30px;  */
	font-size: 12px;
	/* font-weight: 300; */
	border: solid 1px;
	border-radius: 3px;
	margin-right: 5px;
	min-width: 30px;
	display: inline-flex;
	align-items: center;
	justify-content: center;
	background: #ffffff;
	color: #4e4e4e;
	font-weight: bold;
	padding: 0 5px;
}


</style>
