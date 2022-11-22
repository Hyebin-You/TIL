<template>
	<div v-if="movie">
		<div class="detail-video">
			<iframe
				width="100%;"
				height="100%"
				:src="`https://www.youtube.com/embed/${movie.video_key}?autoplay=1&mute=1&loop=1&rel=0&controls=0&showinfo=0`"
				frameborder="0"
				allow="encrypted-media; autoplay;"></iframe>
		</div>
		<div class="detail-context">
			<div>{{ movie.title }}</div>
			<span>{{
				movie.overview.length > 400 ? movie.overview.substr(0, 400) + '...' : movie.overview
			}}</span>
		</div>
	</div>
</template>

<script>
export default {
	name: "DetailVideoContext",
	props: {
		movie: Object,
	},
};
</script>

<style>

.detail-video {
  margin-top: 10px;
	width: 100%;
	height: 350px;
	border-radius: 3px;
}

.detail-context {
	margin: 30px 0;
	width: 700px;
	height: 250px;
	text-align: left;
	font-size: 17px;
  font-weight: 100;
}
.detail-context > div {
  font-family: 'Nanum Gothic', sans-serif;
	width: 700px;
  margin-bottom: 15px;
	text-align: left;
	font-size: 27px;
}

</style>
