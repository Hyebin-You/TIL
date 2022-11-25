<template>
	<div id="app">
		<NavBar />
		<transition name="fade" mode="out-in">
			<router-view />
		</transition>
		<!-- :class="maple? 'change-color-pink': 'change-color-black'" -->
	</div>
</template>

<script>
import NavBar from "@/components/movie/index/NavBar";

export default {
	name: "IndexView",
	components: {
		NavBar,
	},
	computed: {
		maple() {
			return this.$store.state.maple;
		}
	}
};
</script>

<style>
/* .change-color-pink {
	background-color: rgb(186 150 191);
}
.change-color-black {
	background-color: black;
} */



html {
	width: 100%;
  height: 100%;
}
body {
	touch-action: none;
	margin: 0;
	width: 100%;
}



#app {
	/* position: absolute;
	z-index: -99; */
	font-family: 'Noto Sans KR', sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: white;
	height: 100%;
}

::placeholder {
  color: gray;
	opacity: 0.8;
}

nav {
	padding: 10px 20px;
}

nav a {
	font-weight: bold;
	color: white;
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
