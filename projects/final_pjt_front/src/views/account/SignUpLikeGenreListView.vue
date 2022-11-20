<template>
	<div class="genre-listbox">
		<div>
			<h3>SignUpLikeGenreListView</h3>
			<div class="genrebox">
				<LikeGenreListItem
					v-for="(genre, index) in genreList"
					:key="index"
					:genre="genre" />
			</div>
		</div>
	</div>
</template>

<script>
import LikeGenreListItem from "@/components/account/signup/LikeGenreListItem";

export default {
	name: "SignUpLikeGenreListView",
	components: {
		LikeGenreListItem,
	},
	data() {
		return {
			genreList: ["공포", "코미디", "로맨스", "호러", "SF", "스릴러", "공포", "코미디", "로맨스", "호러", "SF", "스릴러"],
		};
	},
};
</script>

<style>
.genre-listbox {
	display: flex;

	flex-direction: column;
	align-items: center;
}
.genrebox {
	max-width: 1000px;
	display: flex;
	justify-content: center;
	flex-wrap: wrap;
}
</style>
