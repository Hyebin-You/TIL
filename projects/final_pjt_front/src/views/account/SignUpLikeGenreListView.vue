<template>
	<div>
		<div class="img-box">
			<img src="@/assets/pinkcube.png" alt="gotcha" />
		</div>
		<div class="genre-listbox">
			<div>
				<div class="genrebox">
					<LikeGenreListItem
						@genre-data="genreGetData"
						v-for="(genre, index) in genreList"
						:key="index"
						:genre="genre" />
				</div>
				<input @click="inputGenres" type="submit" value="선택완료" />
			</div>
		</div>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import LikeGenreListItem from "@/components/account/signup/LikeGenreListItem";
import axios from "axios";

export default {
	name: "SignUpLikeGenreListView",
	components: {
		LikeGenreListItem,
	},
	data() {
		return {
			genreList: [
				"액션",
				"모험",
				"로맨스",
				"애니메이션",
				"코미디",
				"스릴러",
				"공포",
				"범죄",
				"판타지",
				"드라마"
			],
			selectGenreList: [],
		};
	},
	computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		}
	},
	created() { {
			if (!this.isLogin) {
				this.$router.push({ name: 'login'});
			}
		}
	},
	methods: {
		genreGetData(inputData) {
			const array = this.selectGenreList;
			if (array.includes(inputData)) {
				const idx = array.indexOf(inputData);
				array.splice(idx, 1);
				// console.log(array);
			} else {
				array.push(inputData);
				// console.log(array);
			}
		},
		inputGenres() {
			const array = this.selectGenreList;
			if (array.length > 3) {
				this.$swal("3개만 선택할수있어요!!", "", "warning");
			} else {
				this.selectGenreList.forEach(genre => {
					axios({
						method: "post",
						url: `${API_URL}/accounts/set_like_genres/${genre}/`,
						headers: {
							Authorization: `Token ${this.$store.state.token}`,
						},
					})
						.then(res => {
							this.$store.dispatch("userData");
							this.$router.push({ name: "index" });
						})
						.catch(err => {
							console.log(err);
						});
				});
			}
		},
	},
};
</script>

<style scoped>
.img-box {
	width: fit-content;
	position: absolute;
	top: 35%;
	left: 50%;
	padding: 40px;
  transform: translate(-50%, -50%);
}

.genre-listbox {
	display: flex;

	flex-direction: column;
	align-items: center;
	position: absolute;
	top: 60%;
	left: 50.5%;
	padding: 40px;
	transform: translate(-50%, -50%);
}
/* .login-box {
	position: absolute;
	top: 50%;
	left: 58%;
	width: 400px;
	padding: 40px;
	padding-bottom: 30px;
	transform: translate(-50%, -50%);
	background: rgba(255, 255, 255, 0.08);
	box-sizing: border-box;
	box-shadow: 0 15px 25px rgba(0, 0, 0, 0.6);
	border-radius: 10px;
} */

.genrebox {
	max-width: 900px;
	display: flex;
	justify-content: flex-start;
	flex-wrap: wrap;
}
.genre-listbox input {
	font-family: "maplestory";
  font-size: 1.2rem;
  position: relative;
  display: inline-block;
  color: #fff;
	font-weight: 100;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: .5s;
	margin-left: 5px;
	margin-right: 5px;
  padding: 5px 60px;
  margin-bottom: 5px;
	margin-top: 10px;
  border: none;
  outline: none;
  background: transparent;
}


.genre-listbox input:hover {
  background: rgba(248, 248, 248, 0.185);
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(255, 5, 89, 0.2),
              0 0 25px rgba(255, 5, 89, 0.2),
              0 0 50px rgba(255, 5, 89, 0.2),
              0 0 100px rgba(255, 5, 89, 0.2);
}



</style>
