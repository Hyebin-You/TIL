<template>
  <!-- 아래의 div 태그에 @click="showUsercardDetail(card)" -->
  <div v-if="card" class="test" @click='showUsercardDetail'>
    <img :src="require(`@/assets/${card.img_url}`)" :class=" card.isnormal? 'isSilver': 'isGold' " alt="card img">
    <div v-if="card.ability1" class="text-hidden">
      <p style="font-size: 17px">{{ card?.cardname }}</p>
      <br>
			<div :style="{ border : cardGrade }">
				<span>{{ card?.ability1 }}</span>
				<span>{{ card?.ability2 }}</span>
				<span>{{ card?.ability3 }}</span>
			</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WorldCard',
	data() {
		return {
			// cardGrade: `4px solid purple`
		}
	},
  props: {
    card: Object,
  },
	computed: {
		cardGrade() {
			if(this.card.ability_grade === '에픽') {
				return `4px solid purple`;
			} else if (this.card.ability_grade === '유니크') {
				return `4px solid yellow`;
			} else {
				return `4px solid green`;
			}
		}
	},
	methods: {
		showUsercardDetail() {
			if (this.card.ability1) {
				const bodyScroll = document.querySelector('body')
				bodyScroll.style.overflow = 'hidden';
				this.$store.commit('SHOW_USERCARD_DETAIL', this.card)

			}
		}
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
	display: flex;
  flex-direction: column;
	align-items: center;
	justify-content: center;
	width: 100%;
	height: 90%;
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
	font-size: 12px;
	font-weight: 500;
	margin: 0;
	/* padding-top: 150px; */
	/* padding-top: 200px; */
	/* text-align: left; */
	word-break: break-all;
}

.text-hidden > div {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	/* border: 4px solid purple; */
	padding: 3px 15px;
	border-radius: 5px;
}

img {
	width: 100%;
	height: 90%;
	border-radius: 5px;
}

.isGold {
  border: solid gold 3px;
}

.isSilver {
	border: solid rgb(130, 130, 130) 3px;
}


</style>