<template>
	<div @mouseover="openContent" @mouseleave="closeContent" class="review-box">
    <div :style="{ display : visibleContent }" class="review-content">{{ review.content }}</div>
		<div class="review-nick-box">
			<div>
				<img :src="require(`@/assets/${userObject.user_icon}`)" alt="icon">
			</div>
			<div>
				{{ review.user.nickname }}
			</div>
      <div class="star-box2">
        <span class="star2">
          ★★★★★
          <span :style="{ width: starWidth }" >★★★★★</span>
        </span>
      </div>
		</div>
    <div>
      <div class="review-title-box">{{ review.title }}</div>
    </div>
	</div>
</template>

<script>
export default {
	name: "DetailSideReviewItem",
  data() {
    return {
      visibleContent: 'none',
      starWidth: `${this.review.score * 10}%`
    }
  },
	props: {
		review: Object,
	},
  methods: {
    openContent() {
      this.visibleContent = '';
    },
    closeContent() {
      this.visibleContent = 'none';
    },
  },
  computed: {
    userObject() {
      return this.$store.state.userObject;
    }
  }
};
</script>

<style scoped>
.review-box {
  display: flex;
  flex-direction: column;
  margin-top: 8px;
}

.review-nick-box {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.review-nick-box img {
  width: 25px;
  height: 25px;
}
.review-nick-box div {
  margin-left: 10px;
}
.review-title-box {
  width: fit-content;
  font-size: 18px;
  margin-left: 10px;
  /* text-align: start; */
}
.review-content {
  color: black;
  font-weight: bold;
  width: 290px;
  height: 60px;
  position: absolute;
  transition: all 0.5s;
}
.review-content:hover {
  cursor: pointer;
  background-color: rgba(238, 238, 238, 0.89);
  position: absolute;
  z-index: 99;
}
.star2 {
	position: relative;
	font-size: 1rem;
	color: rgba(255, 255, 255, 0.521);
}

.star2 span {
  width: 0;
	position: absolute;
	left: 0;
	color: rgb(255, 136, 0);
	overflow: hidden;
	pointer-events: none;
}
.star-box2 {
  padding-left: 5px;
	width: fit-content;
	margin: auto;
}

</style>
