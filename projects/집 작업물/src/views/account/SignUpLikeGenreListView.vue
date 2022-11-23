<template>
	<div class="genre-listbox">
		<div>
			<h3>SignUpLikeGenreListView</h3>
			<div class="genrebox">
				<LikeGenreListItem
					@genre-data="genreGetData"
					v-for="(genre, index) in genreList"
					:key="index"
					:genre="genre"/>
			</div>
			<button @click="inputGenres">선택완료</button>
		</div>
	</div>
</template>

<script>
import LikeGenreListItem from "@/components/account/signup/LikeGenreListItem";
import axios from 'axios';

export default {
	name: "SignUpLikeGenreListView",
	components: {
		LikeGenreListItem,
	},
	data() {
		return {
			genreList: ["액션", "모험", "로맨스", "애니메이션", "코미디", "스릴러", "공포", "범죄", "판타지",],
			selectGenreList: [],
		};
	},
	methods: {
		genreGetData(inputData) {
			const array = this.selectGenreList
			if (array.includes(inputData)) {
				const idx = array.indexOf(inputData);
				array.splice(idx, 1);
				console.log(array);
			} else {
				array.push(inputData);
				console.log(array);
			}},
		inputGenres() {
			const array = this.selectGenreList
			if (array.length > 3) {
				this.$swal('3개만 선택할수있어요!!','','warning');
			} else {
			this.selectGenreList.forEach((genre) => {
				axios({
					method: 'post',
					url: `http://127.0.0.1:8000/accounts/set_like_genres/${genre}/`,
					headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
				})
					.then((res) => {
						this.$store.dispatch('userData');
						this.$router.push({ name: 'index' });
					})
					.catch((err) => {
						console.log(err);
					})
			})
			}

		}
		},


	}
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
