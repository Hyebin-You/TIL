<template>
  <!-- 아래의 div 태그에 @click="showUsercardDetail(card)" -->
  <div class="test" :class="{'isGold' : !card.isnormal}">
    <img :src="require(`@/assets/${card.img_url}`)" alt="card img">
    <div class="text-hidden">
      <p style="font-size: 13px">{{ card.cardname }}</p>
      <br>
      <p>{{ card.ability1 }}</p>
      <p>{{ card.ability2 }}</p>
      <p>{{ card.ability3 }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WorldCard',
  props: {
    card: Object,
  },
  methods: {
    // showUsercardDetail(card) {
    //   const bodyScroll = document.querySelector('body')
		// 	bodyScroll.style.overflow = 'hidden'
    //   this.$store.commit('SHOW_USERCARD_DETAIL', card)
    // }
  }
}
</script>

<style scoped>
@font-face {
	font-family: "maplestory";
	src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@2.1/MaplestoryOTFBold.woff")
		format("woff");
	font-weight: normal;
	font-style: normal;
}

.text-hidden {
	/* display: flex; */
	align-items: center;
	justify-content: center;
	width: 100%;
	height: 100%;
	opacity: 0;
	background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.9) 100%);
	/* background-color: rgba(0, 0, 0, 0.7); */
	cursor: pointer;
	position: absolute;
	top: 0%;
	left: 0%;
}

.text-hidden:hover {
	opacity: 1;
	color: white;
	transition: all 1s;
	/* background-image: brightness(0.5); */
}

.text-hidden > p {
	max-width: 150px;
	font-size: 10px;
	font-weight: 500;
	/* padding-top: 150px; */
	/* padding-top: 200px; */
	/* text-align: left; */
	word-break: break-all;
}
img {
	width: 100%;
	border-radius: 5px;
}

.isGold {
  border: solid gold 2px;
}
</style>