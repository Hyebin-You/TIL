<template>
	<div class="navBar">
		<nav>
			<router-link :to="{ name: 'index' }">Index</router-link> |
			<router-link :to="{ name: 'login' }">Login</router-link> |
			<router-link :to="{ name: 'signup' }">SignUp</router-link> |
			<router-link :to="{ name: 'nickname' }">SignUpNick</router-link> |
			<router-link :to="{ name: 'likegenre' }">SignUpGenre</router-link> |
			<router-link :to="{ name: 'update' }">Update</router-link> |
			<router-link :to="{ name: 'search' }">Search</router-link> |
			<router-link :to="{ name: 'movieshop' }">MovieShop</router-link> |
			<router-link :to="{ name: 'movieprofile' }">MovieProfile</router-link> |
			<router-link :to="{ name: 'worldindex' }">WorldIndex</router-link> |
			<router-link :to="{ name: 'worldprofile' }">WorldProfile</router-link> |
			<router-link :to="{ name: 'worldfight' }">WorldFight</router-link> |
			<router-link :to="{ name: 'worldshop' }">WorldShopView</router-link> |
			<input 
				class="inputbox"
				placeholder="검색"
				type="text"
				v-model="searchWord"
				@keyup.enter="searching">
		</nav>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	name: "NavBar",
  data() {
    return {
      searchWord: null,
    }
  },
	methods: {
		searching() {
			axios({
				method: "get",
				url: `http://127.0.0.1:8000/movies/search/q?query=${this.searchWord}`,
			})
				.then(res => {
					this.$store.commit('SEARCH_LIST', res.data);
				})
				.catch(err => {
					console.log("error!!!!!", err);
				});
      if (this.$route.path !== '/search') {
        this.$router.push({ name: 'search' });
      }
			this.searchWord = null; 	
		},
	},
};
</script>

<style scoped>
.navBar {
	width: 100vw;
	border: none;
	background-color: #ffffff00;
}
.inputbox {
  padding: 4px;
  font-size: 17px;
  font-weight: bold;
  width: 40px;
  height: 15px;
	color: white;
	background-color: black;
  border: 1px solid black;
  text-align: center;
  outline: none;
  transition: all 0.5s;
}
.inputbox:hover {
	cursor: pointer;
	border: 1px solid gray;
}

.inputbox:focus {
  border-radius: 20px;
  border-color: lightblue;
  height: 20px;
  width: 500px;
  /* background-color: lightcyan; */

}


</style>
