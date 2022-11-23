<template>
	<div class="play-list-flex">
		<div>당신의 추천리스트를 만나보세요</div>
		<PeoPleMovieListItem
			v-for="list in peopleMovieList"
			:key="list.id"
			:list="list" />
	</div>
</template>

<script>
import axios from "axios";
import _ from "lodash";
import PeoPleMovieListItem from "@/components/movie/PeoPleMovieListItem";

export default {
	name: "MyPlayMovieList",
	components: {
		PeoPleMovieListItem,
	},
	data() {
		return {
			peopleMovieList: null,
		};
	},
	created() {
		axios({
			method: "get",
			url: `http://127.0.0.1:8000/movies/user_playlists/ `,
			headers: {
				Authorization: `Token ${this.$store.state.token}`,
			},
		})
			.then(res => {
				this.peopleMovieList = res.data;
			})
			.catch(err => {
				console.log(err);
			});
	},
};
</script>

<style scoped>
.play-list-flex {
	display: flex;
	justify-content: center;
}
.play-list-flex > div:nth-child(1) {
	position: absolute;
  left: 278px;
  font-size: 25px;
}
</style>
