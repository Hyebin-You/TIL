<template>
	<div class="index-box" v-if="video">
		<DetailView />
		<div class="iframe-title">
			<div>
				<div>{{ video.title }}</div>
				<div>{{ video.overview }}</div>
				<!-- <div v-for="genre in videoGenre" :key="genre">{{ genre }}</div> -->
				<span v-for="genre in videoGenre" :key="genre">{{ genre }}</span>
			</div>
		</div>
		<div class="iframe-box">
			<div class="iframe-shadow"></div>
			<iframe
				width="100%;"
				height="100%"
				:src="`https://www.youtube.com/embed/${video.video_key}?autoplay=1&mute=1&loop=1&rel=0&controls=0&showinfo=0`"
				frameborder="0"
				allow="encrypted-media; autoplay;"></iframe>
		</div>
		<div style="padding-top: 700px">
			<transition appear name="slide-fade" mode="out-in">
				<IndexLikeList />
			</transition>
			<transition appear name="slide-fade2" mode="out-in">
				<IndexRandomList />
			</transition>
		</div>
		<PeoPleMovieList />
		<img @click="goWorld" class="jump_pink" src="@/assets/pinkbean_jump.gif" alt="pink">
		<!-- <img @click="goWorld" class="sticky-door" src="@/assets/door.png" alt="door"> -->
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from "axios";
import _ from "lodash";
import IndexLikeList from "@/components/movie/index/IndexLikeList";
import IndexRandomList from "@/components/movie/index/IndexRandomList";
import PeoPleMovieList from "@/components/movie/PeoPleMovieList";
import DetailView from "@/views/movie/DetailView";

export default {
	name: "IndexView",
	components: {
		IndexLikeList,
		IndexRandomList,
		PeoPleMovieList,
		DetailView,
	},
	data() {
		return {
			video: null,
			videoGenre: [],
		};
	},
	methods: {
		goWorld() {
			this.$store.commit('CHANGE_WORLD');
			this.$router.push({ name: 'worldindex' });
		}
	},
	computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		},
	},	
	created() {
		if (!this.isLogin) {
			this.$router.push({ name: 'login'});
		}	
		axios({
			method: "get",
			url: `${API_URL}/movies/search/latest/`,
			headers: {
				Authorization: `Token ${this.$store.state.token}`
			}			
		})
			.then(res => {
				this.video = _.sample(res.data);
				if (this.video.overview.length > 150) {
					this.video.overview = this.video.overview.substr(0, 150) + '...';
				}
				this.video.genres.forEach(gen => {
					this.videoGenre.push(gen.name);
				});


			})
			.catch(error => {
				console.log(error);
			});
	},
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@800&display=swap');
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR&100;300;500;800;display=swap");
@font-face {
	font-family: "maplestory";
	src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/MaplestoryOTFBold.woff")
		format("woff");
	font-weight: lighter;
}
/* .sticky-door {
	position: sticky;
	bottom: 10px;
	left: 95%;
	z-index: 60;
	width: 60px;
	transform-style: preserve-3d;
	transform: rotateY(0deg);
}

.sticky-door:hover {
	cursor: pointer;
	transform-origin: left;
	transform: rotateY(60deg);
	transition: all 1s;
} */
.jump_pink {
	position: sticky;
	bottom: 10px;
	left: 90%;
	z-index: 61;
	width: 40px;
	transition: all 1s;
	animation-duration: 12s;
  animation-name: slidein;
  animation-iteration-count: infinite;
  animation-direction: alternate;

}
.jump_pink:hover {
	cursor: pointer;
	transform: scale(1.4);
}


@keyframes slidein {
  0% {
    left: 80%;
  }

  70% {
    left: 99%;
  }
	
	100% {
    left: 89%;
  }
}



.slide-fade-enter-active,
.slide-fade-leave-active {
	transition: all 0.5s ease 0.7s;
}

.slide-fade-enter {
	transform: translateX(30px);
	opacity: 0;
}

.slide-fade-leave-to {
	transform: translateX(-30px);
	opacity: 0;
}

.slide-fade2-enter-active,
.slide-fade-leave-active {
	transition: all 0.5s ease 1.2s;
}

.slide-fade2-enter {
	transform: translateX(-30px);
	opacity: 0;
}

.slide-fade2-leave-to {
	transform: translateX(30px);
	opacity: 0;
}
.indexbox {
	height: 100%;
}

.centerbox {
	display: flex;
	justify-content: center;
}

.titletext {
	text-align: initial;
	font-family: "Noto Sans KR", sans-serif;
	/* font-family: "maplestory"; */
	font-weight: lighter;
	font-size: 25px;
	color: white;
}

.eventhover {
	max-width: 200px;
	transform: scale(0.9);
}

.eventhover:hover {
	cursor: pointer;
	transform: scale(1.05);
	transition: all 1s;
}

.container {
	width: 1350px;
	max-height: 350px;
}
.wholebox {
	display: flex;
	justify-content: center;
	flex-direction: column;
}

.owl-next {
	font-size: 60px !important;
	position: absolute;
	left: -50px;
	top: 100px;
	background: none !important;
}

.owl-prev {
	font-size: 60px !important;
	position: absolute;
	right: -50px;
	top: 100px;
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

.marginbox {
	margin-left: 200px;
}
.iframe-box {
	position: absolute;
	z-index: -50;
	width: 100%;
	height: 70%;
	transform: scaleX(1.6) scaleY(1.15);
}
.iframe-title {
	color: white;
	position: absolute;
	width: 100%;
	height: 90%;
	display: flex;
	align-items: center;
	left: 100px;
}
.iframe-title > div {
	width: 1000px;
	text-align: left;
}


.iframe-title > div > div:nth-child(1){
	font-size: 50px;
	font-weight: bolder;
}
.iframe-title > div > div:nth-child(2){
	margin-top: 10px; 
	width: 550px;
	font-size: 20px;
	font-weight: 300;
}
.iframe-title > div > span{
	margin-top: 30px; 
	font-size: 15px;
	font-weight: 300;
	border: solid 1px;
	border-radius: 3px;
	margin-right: 5px;
	min-width: 78px;
	display: inline-flex;
	align-items: center;
	justify-content: center;
	background: #ffffff;
	color: #4e4e4e;
	font-weight: bold;
	padding: 0 5px;
}


.iframe-shadow {
	position: absolute;
	width: 100%;
	height: 100%;
	/* background-color: red; */
	background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 1) 100%);
}
</style>
