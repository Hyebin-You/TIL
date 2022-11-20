<template>
	<div>
		<DetailView />
		<h1>Index</h1>
		<IndexLatestList />
		<transition appear name="slide-fade" mode="out-in">
			<IndexLikeList />
		</transition>
		<transition appear name="slide-fade2" mode="out-in">
			<IndexRandomList />
		</transition>
		<MyMovieList />
	</div>
</template>

<script>
import IndexLatestList from "@/components/movie/index/IndexLatestList";
import IndexLikeList from "@/components/movie/index/IndexLikeList";
import IndexRandomList from "@/components/movie/index/IndexRandomList";
import MyMovieList from "@/components/movie/MyMovieList";
import DetailView from "@/views/movie/DetailView";

export default {
	name: "IndexView",
	components: {
		IndexLatestList,
		IndexLikeList,
		IndexRandomList,
		MyMovieList,
		DetailView,
	},
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');
@font-face {
	font-family: "maplestory";
	src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/MaplestoryOTFBold.woff")
		format("woff");
	font-weight: lighter;

}


.slide-fade-enter-active,
.slide-fade-leave-active {
	transition: all 0.5s ease 0.7s;
}

.slide-fade-enter {
	transform: translateX(30px);
	opacity: 0;
}

.slide-fade-leave-to {
	transform: translateX(-30px);
	opacity: 0;
}

.slide-fade2-enter-active,
.slide-fade-leave-active {
	transition: all 0.5s ease 1.2s;
}

.slide-fade2-enter {
	transform: translateX(-30px);
	opacity: 0;
}

.slide-fade2-leave-to {
	transform: translateX(30px);
	opacity: 0;
}
.centerbox {
	display: flex;
	justify-content: center;
	width: 2100px;
}

.titletext {
	text-align: initial;
	font-family: 'Noto Sans KR', sans-serif;
	/* font-family: "maplestory"; */
	font-weight: lighter;
	font-size: 25px;
	color: white;
}

.eventhover {
	max-width: 200px;
	transform: scale(0.9);
}

.eventhover:hover {
	cursor: pointer;
	transform: scale(1.05);
	transition: all 1s;
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


</style>
