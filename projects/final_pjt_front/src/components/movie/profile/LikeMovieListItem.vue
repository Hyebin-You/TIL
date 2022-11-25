<template>
	<div :style="{ left: leftSize }" class="size-layer" @click="showDetail">
		<img
			:src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`"
			alt="movie" />
		<!-- <img src="@/assets/movie.jpg" :alt="movie" /> -->
		<div class="text-hidden">
			<p>{{ movie.title }}</p>
		</div>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from 'axios'

export default {
	name: "LikeMovieListItem",
	props: {
		movie: Object,
		index: Number,
	},
	data() {
		return {
			// leftSize: '100px',
		}
	},
	methods: {
    showDetail() {
			const bodyScroll = document.querySelector('body');
			bodyScroll.style.overflow = 'hidden';

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
	computed: {
		leftSize() {
			// console.log('!!!@@@!!', typeof(`${this.index * 10}px`));
			const value = this.index * 50
			return `${value}px`
		}
	}
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
	width: 100%;
	height: 100%;
	opacity: 0;
	background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.9) 100%);
	cursor: pointer;
	position: absolute;
	top: 0%;
	left: 0%;
}

.text-hidden:hover {
	opacity: 1;
	color: white;
	transition: all 1s;

}

.text-hidden > p {
	max-width: 150px;
	font-size: 15px;
	font-weight: 500;
	padding-top: 150px;
	word-break: break-all;
}
img {
	width: 100%;
	border-radius: 5px;
}
.size-layer {
	position: absolute;
	left: 0;
}
</style>