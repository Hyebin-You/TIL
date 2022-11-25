<template>
	<transition name="fade-detail" mode="out-in">
		<div
			v-if="movie"
			id="dropshadow"
			:style="{ display: detailBoxShadowStyle }"
			@click="detailOff"
			class="dropshadow">
			<div class="detailbox">
				<div class="detail-flex">
					<DetailVideoContext
						:movie="movie" />
					<DetailSideReview :movie="movie"/>
				</div>
				<DetailSameGenre :movie-genres="movie.genres" />
			</div>
		</div>
	</transition>
</template>

<script>
import DetailVideoContext from "@/components/movie/detail/DetailVideoContext";
import DetailSideReview from "@/components/movie/detail/DetailSideReview";
import DetailSameGenre from "@/components/movie/detail/DetailSameGenre";

export default {
	name: "DetailView",
	components: {
		DetailVideoContext,
		DetailSideReview,
		DetailSameGenre,
	},
	data() {
		return {};
	},
	computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		},		
		detailBoxShadowStyle() {
			return this.$store.state.detailBoxShadowStyle;
		},
		movie() {
			return this.$store.state.detailMovie;
		},
	},
	created() { {
			if (!this.isLogin) {
				this.$router.push({ name: 'login'});
			}
		}
	},	
	methods: {
		detailOff(event) {
			if (event.target.id === "dropshadow") {
				const bodyScroll = document.querySelector("body");
				bodyScroll.style.overflowY = "scroll";
				this.$store.commit('OFF_DETAIL')
			}
		},
	},
};
</script>

<style scoped>
.hide {
	display: none;
}
.detail-flex {
	display: flex;
	justify-content: space-evenly;
}

.dropshadow {
	width: 100vw;
	height: 200%;
	background-color: rgba(0, 0, 0, 0.8);
	display: flex;
	justify-content: center;
	align-items: center;
	position: absolute;
	top: -100px;
	z-index: 10;
}

.detailbox {
	position: fixed;
	top: 20px;
	background-color: #161515;
	border-radius: 5px;
	width: 1200px;
	height: 900px;
}
.fade-detail-enter-active {
	transition: all 0.5s ease-out;
}
/* .fade-detail-leave-active {
	transition: all 0.1s ease-out;
} */

.fade-detail-enter {
	opacity: 0;
}

.fade-detail-leave-to {
	opacity: 0;
}
</style>
