<template>
	<div>
		<h3>MovieProfileLikeMovieList</h3>
		<LikeMovieListItem />
	</div>
</template>

<script>
import LikeMovieListItem from "@/components/movie/profile/LikeMovieListItem";

export default {
	name: "MovieProfileLikeMovieList",
	components: {
		LikeMovieListItem,
	},
};
</script>

<style></style>
