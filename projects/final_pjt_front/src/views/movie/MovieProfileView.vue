<template>
	<div>
		<div style="height: 80px; font-size: 30px;"></div>
		<DetailView />
		<div class="profile-box">
			<PublicProfile />
		</div>
		<div class="profile-icon">
			<ProfileIconList />
		</div>
		<div class="profile-itemlist">
			<div>
				<div class="playlist-title">
					{{ userObject.nickname }}님의 PlayList
				</div>
				<form @submit.prevent="createMovieList">
					<div class="flex-box">
						<input v-model="movieListTitle" type="text" placeholder="PlayList Name" maxlength="15"/>
						<input type="checkbox" id="isopen" v-model="isopened" />
						<label for="isopen">공개</label>
						<input type="submit" value="생성" />
					</div>
				</form>
			</div>
			<div class="container" v-if="userObject.playlist_set">
				<carousel :items="3" :autoplay="false" :nav="true" :dots="false">
					<PeoPleMovieListItem
						v-for="list in userObject.playlist_set"
						:key="list.id"
						:list="list" />
				</carousel>
			</div>
			<MovieProfileLikeMovieList />
		</div>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from "axios";
import carousel from "vue-owl-carousel";
import MovieProfileLikeMovieList from "@/components/movie/profile/MovieProfileLikeMovieList";
import ProfileIconList from "@/components/ProfileIconList";
import PeoPleMovieListItem from "@/components/movie/PeoPleMovieListItem";
import PublicProfile from "@/components/PublicProfile";
import DetailView from "@/views/movie/DetailView";

export default {
	name: "MovieProfileView",
	components: {
		carousel,
		DetailView,
		MovieProfileLikeMovieList,
		PeoPleMovieListItem,
		ProfileIconList,
		PublicProfile,
	},
	data() {
		return {
			movieListTitle: null,
			isopened: false,
		};
	},
	methods: {
		createMovieList() {
			// console.log(this.isopened);
			axios({
				method: "post",
				url: `${API_URL}/movies/create_playlist/`,
				data: {
					title: this.movieListTitle,
					isopened: this.isopened,
				},
				headers: {
					Authorization: `Token ${this.$store.state.token}`,
				},
			})
				.then(res => {
					this.$store.dispatch("userData");
					this.$swal('보관함이 생성되었습니다!', 'success');
					setTimeout(() => this.$router.go(), 1000);
					
				})
				.catch(err => {
					console.log(err);
				});
		},
		addArrow() {
			// console.log("addarrow", eventName);
			const nextBtnList = document.querySelectorAll(".owl-prev");
			const prevBtnList = document.querySelectorAll(".owl-next");

			nextBtnList.forEach(btn => {
				btn.innerText = "»";
			});
			prevBtnList.forEach(btn => {
				btn.innerText = "«";
			});
		},
	},
	computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		},		
		userObject() {
			return this.$store.state.userObject;
		},
	},
	created() { {
			if (!this.isLogin) {
				this.$router.push({ name: 'login'});
			}
		}
	},	
	beforeMount() {
		this.$store.dispatch("userData");
		this.addArrow();
	},
};
</script>

<style scoped>
.profile-box {
	width: 80vw;
	height: 230px;
	margin: 0px auto;
	/* border: 1px solid whitesmoke; */
}
.profile-itemlist {
	width: 70vw;
	margin: auto;
}
.profile-icon {
	width: 70vw;
	margin: 30px auto;
}

.profile-itemlist > div:nth-child(1) {
	display: flex;
	justify-content: flex-start;
	align-items: center;
}


.flex-box {
	display: flex;
	justify-content: space-between;
}
form {
	z-index: 5;

}

form > div > input:nth-child(1) {
	width: 120px;
}
form > div input {
	margin-left: 10px;
	cursor: pointer;
}

.playlist-title {
	font-size: 25px;
	/* margin-right: 10px; */
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
.list-size {
	width: 500px;
}
</style>
