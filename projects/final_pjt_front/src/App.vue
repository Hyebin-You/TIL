<template>
	<div id="app">
		<NavBar />
		<!-- <nav>
      <router-link :to="{ name: 'index' }">Index</router-link> |
      <router-link :to="{ name: 'login' }">Login</router-link> |
      <router-link :to="{ name: 'signup' }">SignUp</router-link> |
      <router-link :to="{ name: 'nickname' }">SignUpNick</router-link> |
      <router-link :to="{ name: 'likegenre' }">SignUpGenre</router-link> |
      <router-link :to="{ name: 'update' }">Update</router-link> |
      <router-link :to="{ name: 'search' }">Search</router-link> |
      <router-link :to="{ name: 'movieshop' }">MovieShop</router-link> |
      <router-link :to="{ name: 'detail' }">Detail</router-link> |
      <router-link :to="{ name: 'movieprofile' }">MovieProfile</router-link> |
      <router-link :to="{ name: 'worldindex' }">WorldIndex</router-link> |
      <router-link :to="{ name: 'worldprofile' }">WorldProfile</router-link> |
      <hr>
      <router-link :to="{ name: 'worldfight' }">WorldFight</router-link> |
      <router-link :to="{ name: 'worldshop' }">WorldShopView</router-link> |
    </nav> -->
		<transition name="fade" mode="out-in">
			<router-view />
		</transition>
	</div>
</template>

<script>
import NavBar from "@/components/movie/index/NavBar";

export default {
	name: "IndexView",
	components: {
		NavBar,
	},
};
</script>

<style>
body {
	margin: 0;
}
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
}

nav {
	padding: 30px;
}

nav a {
	font-weight: bold;
	color: #2c3e50;
}

nav a.router-link-exact-active {
	color: #42b983;
}

.fade-enter-active,
.fade-leave-active {
	transition: opacity 0.5s ease-out;
}

.fade-enter {
	opacity: 0;
}

.fade-leave-to {
	opacity: 0;
}

</style>
