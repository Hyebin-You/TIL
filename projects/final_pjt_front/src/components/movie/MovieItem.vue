<template>
	<div class="test" @click="showDetail(movie)">
		<img
			:src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`"
			alt="movie" />
		<!-- <img src="@/assets/movie.jpg" :alt="movie" /> -->
		<div class="text-hidden">
			<p>{{ movie.title }}</p>
			<!-- <p>사일런트힐</p> -->
		</div>
	</div>
</template>

<script>
export default {
	name: "MovieItem",
	props: {
		movie: Object,
	},
	methods: {
    showDetail(movie) {
      this.$store.dispatch('show_detail', movie);
			const bodyScroll = document.querySelector('body');
			bodyScroll.style.overflow = 'hidden';
			// this.$router.push({ name: 'detail' });
			// 나중에 여기 axios요청으로 pk값 담아서 detail페이지 요청하면됨
			// 지금 캐러셀 디테일페이지 2마리씩 오류
    }
  },
	created() {
		this.$store.state.detailSwitch = false;
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
	font-family: maplestory;
	max-width: 150px;
	/* padding-top: 200px; */
	/* text-align: center; */
	word-break: break-all;
}
img {
	width: 100%;
	border-radius: 5px;
}

</style>
