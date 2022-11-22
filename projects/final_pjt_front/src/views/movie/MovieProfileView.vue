<template>
	<div>
		<h1>MovieProfile</h1>
		<div class="profile-box">
			<PublicProfile />
		</div>
		<div class="profile-itemlist">
			<form @submit.prevent="createMovieList">
				<input v-model="movieListTitle" type="text">
				<input type="checkbox" id="isopen" v-model="isopened">
				<label for="isopen">공개</label>
				<input type="submit" value="등록">
			</form>
			<ProfileIconList />
			<LikeMovieListItem 
				v-for="list in userObject.playlist_set" 
				:key="list.id"
				:list="list"/>
			<MovieProfileLikeMovieList />
		</div>
	</div>
</template>

<script>
import axios from 'axios'
import MovieProfileLikeMovieList from "@/components/movie/profile/MovieProfileLikeMovieList";
import ProfileIconList from "@/components/ProfileIconList";
import LikeMovieListItem from "@/components/movie/profile/LikeMovieListItem"
import PublicProfile from "@/components/PublicProfile";

export default {
	name: "MovieProfileView",
	components: {
		MovieProfileLikeMovieList,
		LikeMovieListItem,
		ProfileIconList,
		PublicProfile,
	},
	data() {
		return {
			movieListTitle: null,
			isopened: null,
		}
	},
	methods: {
		createMovieList() {
			axios({
				method: 'post',
				url: `http://127.0.0.1:8000/movies/create_playlist/`,
				data: {
					title: this.movieListTitle,
					isopened: this.isopened,
				},
				headers: {
					Authorization: `Token ${this.$store.state.token}`,
				},
			})
				.then((res) => {
					alert('보관함이 생성 되었습니다');
					this.$store.dispatch('userData');
				})
				.catch((err) => {
					console.log(err);
				})
		}
	},
	computed: {
		userObject() {
			return this.$store.state.userObject;
		}
	}
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
