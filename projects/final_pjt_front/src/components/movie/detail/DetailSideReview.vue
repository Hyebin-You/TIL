<template>
	<div>
		<div class="detail-review">
			<h3>영화 한줄 리뷰</h3>
			<div v-for="review in movie.review_set.slice(-7)" :key="review.id">
				<DetailSideReviewItem :review="review" />
			</div>
			<div v-for="revi in reviews" :key="revi.id">
        <DetailSideReviewItem :review="revi" />
			</div>
		</div>
		<form class="create-review-box" @submit.prevent="createReview">
			<textarea
				class="inputbox"
				v-model="reviewTitle"
				placeholder="제목"
				type="text"
        required
				maxlength="20" />
			<div style="width: 100%; opacity: 0; z-index: -1; height: 30px">a</div>
			<textarea
				class="inputbox2"
				v-model="reviewContent"
				placeholder="내용"
				type="text"
        required
				maxlength="38" />
			<div class="star-flex-box">
				<div class="star-box">
					<span class="star">
						★★★★★
						<span>★★★★★</span>
						<input
							type="range"
							@input="drawStar"
							v-model="reviewScore"
							value="1"
							step="1"
							min="0"
							max="10" />
					</span>
				</div>
				<input type="submit" value="리뷰등록" />
			</div>
		</form>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from "axios";
import DetailSideReviewItem from "@/components/movie/detail/DetailSideReviewItem";

export default {
	name: "DetailSideReview",
	components: {
		DetailSideReviewItem,
	},
	data() {
		return {
			reviewTitle: null,
			reviewContent: null,
			reviewScore: null,
			reviewLength: null,
			reviews: null,
		};
	},
	props: {
		movie: Object,
	},
	computed: {
		userNick() {
			return this.$store.state.userObject.nickname;
		},
	},
	methods: {
		drawStar(event) {
			document.querySelector(`.star span`).style.width = `${
				event.target.value * 10
			}%`;
			// document.querySelector(`.star span`).style.width = `${53.5}%`;
		},
		createReview() {
			// console.log('$$$$$$$$$$$$$$', this.movie.review_set);
			axios({
				method: "post",
				url: `${API_URL}/movies/create_review/${this.movie.id}/`,
				data: {
					title: this.reviewTitle,
					content: this.reviewContent,
					score: this.reviewScore,
				},
				headers: {
					Authorization: `Token ${this.$store.state.token}`,
				},
			})
				.then(res => {
					axios({
						method: "post",
						url: `${API_URL}/accounts/change_point/`,
						data: {
							'status': 'add',
							'point': 500,
						},
						headers: {
							Authorization: `Token ${this.$store.state.token}`
						}
					})
						.then(res => {
							this.$store.dispatch("userData");
						})
						.catch(err => {
							console.log("error", err);
						});

					this.reviewLength = this.movie.review_set.length;


					const newData = {
						title: this.reviewTitle,
						content: this.reviewContent,
						score: this.reviewScore,
						user: {nickname : this.userNick},
					};
					if (this.reviews === null) {
						this.reviews = [];
						this.reviews.push(newData);
					} else {
						this.reviews.push(newData);
					}
          this.reviewTitle = null;
          this.reviewContent = null;
          this.reviewScore = null;
          console.log('닉왜안옴', this.userNick)
				})
				.catch(err => {
					console.log(err);
					console.log(this.$store.state.token);
				});
		},
	},
	watch: {
		movie: function () {
      this.reviews = null;
      const reviewLength = this.movie.review_set.length;
      console.log('리뷰개수', );
      
      if (reviewLength >= 6) {
        document.querySelector('.detail-review').style.overflowY = 'scroll';
      } else {
        document.querySelector('.detail-review').style.overflow = 'hidden';
      }
		},
	},
};
</script>

<style scoped>
.detail-review {
	margin-top: 10px;
	/* border: 1px solid black; */
	width: 300px;
	height: 530px;
}
.create-review-box {
	display: flex;
	flex-direction: column;
	position: relative;
}
.inputbox {
	position: absolute;
	left: 0;
	padding: 2px;
	font-size: 15px;
	font-weight: bold;
	width: 47%;
	height: 20px;
	color: black;
	border: 1px solid black;
	text-align: start;
	outline: none;
	z-index: 1;
	word-break: break-all;
	transition: all 0.5s;
}
.inputbox:hover {
	cursor: pointer;
	border: 1px solid gray;
}

.inputbox:focus {
	height: 55px;
	width: 98%;
	max-width: 98%;
	position: absolute;
	z-index: 100;
}

.inputbox2 {
	position: absolute;
	right: 0;
	padding: 2px;
	font-size: 15px;
	font-weight: bold;
	width: 47%;
	height: 20px;
	color: black;
	border: 1px solid black;
	text-align: start;
	outline: none;
	z-index: 1;
	transition: all 0.5s;
}
.inputbox2:hover {
	cursor: pointer;
	border: 1px solid gray;
}

.inputbox2:focus {
	height: 55px;
	width: 98%;
	z-index: 100;
}
form input:hover {
	cursor: pointer;
	background-color: lightgray;
}

.star {
	position: relative;
	font-size: 1.5rem;
	color: #ddd;
}

.star input {
	width: 100%;
	height: 100%;
	position: absolute;
	left: 0;
	opacity: 0;
	cursor: pointer;
}

.star span {
	width: 0;
	position: absolute;
	left: 0;
	color: crimson;
	overflow: hidden;
	pointer-events: none;
}
.star-box {
	width: fit-content;
	margin: auto;
}

</style>
