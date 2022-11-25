<template>
	<div class="search-listbox">
		<DetailView />
		<div>
			<h1>PlayList</h1>
			<transition-group
				class="search-items"
				v-if="playList"
				tag="div"
				name="fade-move"
				mode="out-in"
				@enter="enter"
				@after-enter="afterEnter">
				<div style="position: relative;" v-for="movie in playList" :key="movie.title">
					<img
						style="right: 3px; top: 3px"
						@click="deletePlaylistMovie(movie)"
						class="x-delete"
						src="@/assets/x.png"
						alt="x" />
					<MovieItem :movie="movie" class="eventhover" />
				</div>
			</transition-group>
		</div>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from 'axios'
import MovieItem from "@/components/movie/MovieItem";
import DetailView from "@/views/movie/DetailView";

export default {
	name: "MoviePlayListDetailView",
	components: {
		MovieItem,
		DetailView,
	},
	data() {
		return {
			// searchList: null,
		};
	},
	computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		},		
		playList() {
			return this.$store.state.playList.in_movies;
		},
		playListId() {
			return this.$store.state.playList.id;
		}
	},
	created() { {
			if (!this.isLogin) {
				this.$router.push({ name: 'login'});
			}
		}
	},
	methods: {
		enter(el) {
			el.style.transitionDelay = 200 + "ms";
		},
		afterEnter(el) {
			el.style.transitionDelay = "";
		},
    deletePlaylistMovie(movie) {
      axios({
        method: 'post',
        url: `${API_URL}/movies/playlist_movie/${this.playListId}/${movie.id}/ `,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          // console.log('리스트안 영화 삭 ㅡ 제');
          this.$store.dispatch('savePlayListDetail', this.playListId);
        })
        .catch((err) => {
          console.log(err);
        })
    }
	},
};
</script>

<style scoped>
.search-items {
	display: flex;
	max-width: 1000px;
	flex-wrap: wrap;
	align-items: center;
}
.search-listbox {
	width: 100vw;
	height: 100%;
	display: flex;
	justify-content: center;
	position: relative;
}
.fade-move-enter-active {
	transition: all 0.5s ease-out;
}
.fade-move-enter {
	transform: translateX(50px);
	opacity: 0;
}
.fade-move-leave {
	opacity: 0;
}
.x-delete {
	max-width: 20px;
	height: 20px;
	position: absolute;
	z-index: 10;
}
.x-delete:hover {
	cursor: pointer;
	transform: scale(1.2);
}
/* img {
	right: 0;
} */
</style>
