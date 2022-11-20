<template>
	<div class="search-listbox">
    <DetailView />
		<div>
			<h1>Search</h1>
			<input type="text" @keyup.enter="searching" v-model="searchWord">
			<div class="search-items" v-if="randomList">
				<MovieItem
					v-for="movie in randomList"
					:key="movie.id"
					:movie="movie"
					class="eventhover" />
			</div>
		</div>
	</div>
</template>

<script>
import axios from "axios";
import MovieItem from "@/components/movie/MovieItem";
import DetailView from "@/views/movie/DetailView";

export default {
	name: "SearchView",
	components: {
		MovieItem,
    DetailView,
	},
	data() {
		return {
			randomList: null,
			searchWord: null,
		};
	},
	// created() {
	// 	axios({
	// 		method: "get",
	// 		url: `http://127.0.0.1:8000/movies/search/q?query=${this}`,
	// 	})
	// 		.then(res => {
	// 			this.randomList = res.data;
	// 		})
	// 		.catch(err => {
	// 			console.log("error!!!!!", err);
	// 		});
	// },
	methods: {
		searching() {
		axios({
			method: "get",
			url: `http://127.0.0.1:8000/movies/search/q?query=${this.searchWord}`,
		})
			.then(res => {
				this.randomList = res.data;
			})
			.catch(err => {
				console.log("error!!!!!", err);
			});
		}
	},
};
</script>

<style>
.search-items  {
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
</style>
