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
				<MovieItem
					v-for="movie in playList"
					:key="movie.title"
					:movie="movie"
					class="eventhover" />
			</transition-group>
		</div>
	</div>
</template>

<script>
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
		playList() {
			console.log(this.$store.state.playList.in_movies)
			return this.$store.state.playList.in_movies;
		},
	},
	methods: {
		enter(el) {
			el.style.transitionDelay = 200 + "ms";
		},
		afterEnter(el) {
			el.style.transitionDelay = "";
		},
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
</style>
