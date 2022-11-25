<template>
	<div v-if="movie">
		<div class="detail-video">
			<iframe
				width="100%;"
				height="100%"
				:src="`https://www.youtube.com/embed/${movie.video_key}?autoplay=1&mute=1&loop=1&rel=0&controls=0&showinfo=0`"
				frameborder="0"
				allow="encrypted-media; autoplay;"></iframe>
		</div>
		<div class="detail-context">
			<div>{{ movie.title }}
				<div class="detail-like-list">
					<span v-if="!isLiked" @click="likeMovie">🤍
					</span>
					<span v-if="isLiked" @click="likeMovie">🧡</span>
					<div class="dropdown">
						<img src="@/assets/playlist.png" alt="">
						<div class="dropdown-content">
							<a @click="addPlayList(list.id)" v-for="list in playLists" :key="list.id">{{ list.title }}</a>
						</div>
					</div>
				</div>
			</div>
			<span>{{
				movie.overview.length > 400 ? movie.overview.substr(0, 400) + '...' : movie.overview
			}}</span>
		</div>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from 'axios'
import _ from 'lodash'

export default {
	name: "DetailVideoContext",
	props: {
		movie: Object,
	},
	methods: {
		likeMovie() {
			axios({
				method: 'post',
				url: `${API_URL}/movies/likes/${this.movie.id}/`,
				headers: {
					Authorization: `Token ${this.$store.state.token}`
				},
			})
				.then((res) => {
					this.$store.dispatch('userData');
				})
				.catch((err) => {
					console.log(err);
				})
		},
		addPlayList(playlist_id) {
			axios({
				method: 'post',
				url: `${API_URL}/movies/playlist_movie/${playlist_id}/${this.movie.id}/`,
				headers: {
					Authorization: `Token ${this.$store.state.token}`
				}
			})
				.then((res) => {
					this.$store.dispatch('userData');
				})
				.catch((err) => {
					console.log(err);
				})
		}
	},
	computed: {
		playLists() {
			const myMovieList = this.$store.state.userObject.playlist_set;
			const mmList = myMovieList.filter((list) => {
				const inlist = list.in_movies
				return inlist.every((movie) => movie.id !== this.movie.id)		
			})
			const mmmList = mmList.filter((list) => {
				return list.in_movies.length <= 5
			})
			return mmmList;
		},
		user_like_movies() {
			return this.$store.state.userObject.like_movies
		},
		isLiked() {
			return this.user_like_movies.some((movie) => 
				{ return movie.id === this.movie.id })
		}
	}
};
</script>

<style>

.detail-video {
  margin-top: 10px;
	width: 100%;
	height: 350px;
	border-radius: 3px;
}

.detail-context {
	margin: 25px 0;
	width: 700px;
	height: 250px;
	text-align: left;
	font-size: 17px;
  font-weight: 100;
}


.detail-context > div {
	display: flex;
	justify-content: space-between;
  font-family: 'Nanum Gothic', sans-serif;
	width: 700px;
  margin-bottom: 15px;
	text-align: left;
	font-size: 27px;
}

.detail-context > div span:hover {
	cursor: pointer;
	transform: scale(1.2);
	transition: all 0.5s;
}
.detail-context img {
	margin-left: 5px;
	width: 27px;
	height: 27px;
}
.detail-context img:hover {
	cursor: pointer;
	transform: scale(1.2);
	transition: all 0.5s;
}


.detail-like-list {
	display: flex;
	align-items: center;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
	margin-top: 5px;
	width: 30px;
	height: 32px;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 80px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.266);
  z-index: 1;
	border-radius: 3px;
	left: 3px;
}

/* Links inside the dropdown */
.dropdown-content a {
	cursor: pointer;
  color: black;
  padding: 4px 6px;
  text-decoration: none;
  display: block;
	font-size: 15px;
	border-radius: 3px;
}

.dropdown-content a:hover {
	background-color: #37010126
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}


</style>
