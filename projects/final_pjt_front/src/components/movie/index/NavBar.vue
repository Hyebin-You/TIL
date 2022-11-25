<template>
	<div v-show="showNavbar" class="navBar">
		<nav>
			<div>
				<img @click="goHome" src="@/assets/gotcha2.png" alt="logo" />
			</div>
			<div class="nav-items">
				<!-- <router-link :to="{ name: 'signup' }">SignUp</router-link> |
				<router-link :to="{ name: 'nickname' }">SignUpNick</router-link> |
				<router-link :to="{ name: 'likegenre' }">SignUpGenre</router-link> | -->
				<!-- <router-link :to="{ name: 'update' }">Update</router-link> | -->
				<!-- <router-link :to="{ name: 'worldindex' }">WorldIndex</router-link> |
				<router-link :to="{ name: 'worldprofile' }">WorldProfile</router-link> |
				<router-link :to="{ name: 'worldfight' }">WorldFight</router-link> |
				<router-link :to="{ name: 'worldshop' }">WorldShopView</router-link> |
				<router-link :to="{ name: 'pinkbean' }">PinkBean</router-link> | -->
				<!-- <router-link :to="{ name: 'login' }">Login</router-link> -->
				<input
					v-if="!maple"
					class="inputbox"
					type="text"
					v-model="searchWord"
					@keyup.enter="searching" />
				<div v-if="maple" @click="goFight" class="max-img-size">
					<img src="@/assets/fight.png" alt="fight">
				</div>					
				<div v-if="maple" @click="goPink" class="max-img-size">
					<img src="@/assets/meat_icon2.png" alt="pink">
				</div>
				<div @click="goShop" class="max-img-size">
					<img src="@/assets/shop.png" alt="shop">
				</div>
				<div @click="goProfile" class="max-img-size">
					<img src="@/assets/people.png" alt="profile">
				</div>
				<div @click="goLogOut" class="max-img-size">
					<img src="@/assets/logout.png" alt="logout">
				</div>
				<div class="margin-box"></div>
			</div>
		</nav>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from "axios";

export default {
	name: "NavBar",
	data() {
		return {
			searchWord: null,
		};
	},

	methods: {
		searching() {
			axios({
				method: "get",
				url: `${API_URL}/movies/search/q?query=${this.searchWord}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }				
			})
				.then(res => {
					this.$store.commit("SEARCH_LIST", res.data);
				})
				.catch(err => {
					console.log("error!!!!!", err);
				});
			if (this.$route.path !== "/search") {
				this.$router.push({ name: "search" });
			}
			this.searchWord = null;
		},
		goHome() {
			// console.log('!!!여기어딘데', this.$route.fullPath);
			if (this.maple) {
				if (this.$route.fullPath === "/worldindex") {
				this.$router.go();
			} else {
				this.$router.push({ name: "worldindex" });
			}
			} else {
				if (this.$route.fullPath === "/index") {
					this.$router.go();
				} else {
					this.$router.push({ name: "index" });
				}
			}
		},
		goShop() {

			if (this.maple) {
				if (this.$route.fullPath === "/worldshop") {
				this.$router.go();
			} else {
				this.$router.push({ name: "worldshop" });
			}
			} else {
				if (this.$route.fullPath === "/movieshop") {
				this.$router.go();
				} else {
					this.$router.push({ name: "movieshop" });
				}
			}
			
		},
		goProfile() {
			if (this.maple) {
				if (this.$route.fullPath === "/worldprofile") {
				this.$router.go();
				} else {
					this.$router.push({ name: "worldprofile" });
				}
			} else {
				if (this.$route.fullPath === "/movieprofile") {
				this.$router.go();
				} else {
					this.$router.push({ name: "movieprofile" });
				}
			}			
		},
		goPink() {
			if (this.maple) {
				if (this.$route.fullPath === "/pinkbean") {
				this.$router.go();
				} else {
					this.$router.push({ name: "pinkbean" });
				}
			}			
		},
		goFight() {
			if (this.maple) {
				if (this.$route.fullPath === "/worldfight") {
				this.$router.go();
				} else {
					this.$router.push({ name: "worldfight" });
				}
			}			
		},						
		goLogOut() {
			axios({
				method: 'post',
				url: `${API_URL}/accounts/logout/`,
				headers: {
					Authorization: `Token ${this.$store.state.token}`
				}
			})
				.then((res) => {
					this.$store.commit('USER_LOGOUT');
				})
				.catch((err) => {
					console.log(err);
				})
		},

	},
	computed: {
		maple() {
			return this.$store.state.maple;
		},
		showNavbar() {
			if (
				this.$route.fullPath === "/login" ||
				this.$route.fullPath === "/signup" ||
				this.$route.fullPath === "/nickname" ||
				this.$route.fullPath === "/likegenre"
			) {
				return false;
			} else {
				return true;
			}
		},
	},
};
</script>

<style scoped>
.margin-box {
	margin-right: 50px;
}

.max-img-size {
	cursor: pointer;
	width: 28px;
	height: 28px;
	margin: 0 20px;
}
/* .max-img-size:hover img {
	transform: scale(1.2);
	transition: all 0.5s;
} */

.max-img-size img {
	width: 100%;
	height: 100%;
}
.nav-items {
	display: flex;
	justify-content: center;
	align-items: center;
}

.navBar {
	width: 100vw;
	height: 80px;
	border: none;
	background-color: #00000052;
}
.navBar > nav {
	display: flex;
	justify-content: space-between;
	align-items: center;
}


.navBar > nav > div > img {
	width: 120px;
	cursor: pointer;
}
/* .search:hover ~ .inputbox {
	cursor: pointer;
	border-radius: 20px;
	border: 2px solid rgba(107, 3, 12, 0.755);
	height: 20px;
	width: 500px;
} */


.inputbox {
	padding: 4px;
	font-size: 17px;
	font-weight: bold;
	width: 45px;
	/* height: 15px; */
	color: white;
	background-color: rgba(0, 0, 0, 0);
	background-image: url('@/assets/search.png');
	background-repeat : no-repeat;
	background-size : 28px;
	background-position: 10px center;
	border: none;
	text-align: center;
	outline: none;
	
}
.inputbox:hover {
	cursor: pointer;
	transform: scale(1.05);
	transition: all 0.5s;
}

.inputbox:focus {
	border-radius: 20px;
	border: 2px solid rgba(107, 3, 12, 0.755);
	height: 28px;
	width: 500px;

}
</style>
