<template>
	<div>
		<h3>MovieProfileLikeMovieList</h3>
		<div v-for="movie in myMovieList" :key="movie.id">
			<!-- <LikeMovieListItem /> -->
		</div>
	</div>
</template>

<script>
import LikeMovieListItem from "@/components/movie/profile/LikeMovieListItem";

export default {
	name: "MovieProfileLikeMovieList",
	components: {
		// LikeMovieListItem,
	},
	data() {
		return {
			myMovieList: null,
		}
	}
};
</script>

<style></style>
