<template>
	<div>
		<h1>MovieProfile</h1>
		<div class="profile-box">
			<PublicProfile />
		</div>
		<div class="profile-itemlist">
			<ProfileIconList />
			<MovieProfileLikeMovieList />
		</div>
	</div>
</template>

<script>
import MovieProfileLikeMovieList from "@/components/movie/profile/MovieProfileLikeMovieList";
import ProfileIconList from "@/components/ProfileIconList";
import PublicProfile from "@/components/PublicProfile";

export default {
	name: "MovieProfileView",
	components: {
		MovieProfileLikeMovieList,
		ProfileIconList,
		PublicProfile,
	},
};
</script>

<style>
.profile-box {
	width: 70vw;
	height: 200px;
	margin: 50px auto;
	border: 1px solid whitesmoke;
}
.profile-itemlist {
	border: 1px white solid;
	width: 70vw;
	margin: auto;
}
</style>
