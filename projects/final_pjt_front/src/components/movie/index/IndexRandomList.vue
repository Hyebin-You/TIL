<template>
	<div class="centerbox">
		<div>
			<div class="wholebox">
				<div class="titletext">오늘 이 영화는 어떨까요</div>
				<div class="container" v-if="randomList">
					<carousel
						:items="7"
						:autoplay="false"
						:nav="true"
						:dots="false"
						class="marginTop50">
						<MovieItem
							v-for="movie in randomList"
							:key="movie.id"
							:movie="movie"
							class="eventhover" />
					</carousel>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from "axios";
import carousel from "vue-owl-carousel";
import MovieItem from "@/components/movie/MovieItem";
// import _ from 'lodash'
export default {
	name: "IndexRandomList",
	components: {
		carousel,
		MovieItem,
	},
	data() {
		return {
			randomList: null,
			tests: [1, 2, 3, 4, 5, 6, 7, 8, 9],
		};
	},
	created() {
    axios({
      method: "get",
			url: `${API_URL}/movies/search/random/`,
			headers: {
				Authorization: `Token ${this.$store.state.token}`
			}			
		})
			.then(res => {
        this.randomList = res.data;
			})
			.catch(err => {
        console.log("error!!!!!", err);
			});
	},
  updated(){
    this.addArrow();
  },
	methods: {
    addArrow() {
			const nextBtnList = document.querySelectorAll(".owl-prev");
			const prevBtnList = document.querySelectorAll(".owl-next");

			nextBtnList.forEach(btn => {
				btn.innerText = "»";
			});
			prevBtnList.forEach(btn => {
				btn.innerText = "«";
			});
		},
	},
};
</script>

<style scoped>
@font-face {
	font-family: "maplestory";
	src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/MaplestoryOTFBold.woff")
		format("woff");
	font-weight: lighter;
	/* font-style: normal; */
}
.centerbox {
	display: flex;
	justify-content: center;
}

.titletext {
	text-align: initial;
	font-family: 'Noto Sans KR', sans-serif;
	font-weight: lighter;
	font-size: 25px;
	color: white;
}

.eventhover {
	max-width: 200px;
	transform: scale(0.9);
}
.container {
	width: 1350px;
	max-height: 350px;
}
.wholebox {
	display: flex;
	justify-content: center;
	flex-direction: column;
}

.owl-next {
	font-size: 60px !important;
	position: absolute;
	left: -50px;
	top: 100px;
	background: none !important;
}

.owl-prev {
	font-size: 60px !important;
	position: absolute;
	right: -50px;
	top: 100px;
	background: none !important;
	transition: all 1s;
}
.owl-item {
	position: relative;
	display: flex;
	justify-content: center;
	align-items: center;
	/* margin: 0px -100px; */
}

.marginbox {
	margin-left: 200px;
}

.eventhover:hover {
	cursor: pointer;
	transform: scale(1);
	transition: all 1s;
}
</style>
