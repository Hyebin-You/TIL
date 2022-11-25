<template>
  <div>
    <WorldCardDetail />
    <div class="world-index-title">핑크빈 월드</div>
		<div class="profile-box">
			<PublicProfile />
		</div>
    <div class="world-index-box">
      <div>
        <WorldRankingList/>
      </div>
      <div>
        <RankComment />
      </div>
    </div>
    <img @click="goMovie" class="jump_pink" src="@/assets/pinkbean_jump.gif" alt="pink">
  </div>
</template>

<script>
import WorldRankingList from '@/components/world/index/WorldRankingList'
import WorldCardDetail from '@/components/world/profile/WorldCardDetail'
import PublicProfile from "@/components/PublicProfile";
import RankComment from "@/components/world/index/RankComment";

export default {
  name: 'WorldIndexView',
  components: {
    WorldRankingList,
    PublicProfile,
    RankComment,
    WorldCardDetail,
  },
	computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		},
	},
	created() { {
			if (!this.isLogin) {
				this.$router.push({ name: 'login'});
			}
		}
	},    
	methods: {
		goMovie() {
      this.$store.commit('CHANGE_WORLD');
			this.$router.push({ name: 'index' });
		}
	},  
}
</script>

<style scoped>
* {
  font-family: 'maplestory';
}


.world-index-title {
  font-size: 50px;
  margin-bottom: 50px;
}

.profile-box {
	width: 80vw;
	height: 230px;
	margin: 0px auto;
	/* border: 1px solid whitesmoke; */
}

.world-index-box {
  display: flex;
  justify-content: space-evenly;
	width: 80vw;
	height: 500px;
	margin: 0px auto;
	/* border: 1px solid whitesmoke; */
}
.world-index-box > div:nth-child(1) {
  width: 60%;
}

.world-index-box > div:nth-child(2) {
  width: 20%;
}

.jump_pink {
	position: sticky;
	bottom: 10px;
	left: 90%;
	z-index: 61;
	width: 40px;
	transition: all 1s;
	animation-duration: 12s;
  animation-name: slidein;
  animation-iteration-count: infinite;
  animation-direction: alternate;

}
.jump_pink:hover {
	cursor: pointer;
	transform: scale(1.4);
}
@keyframes slidein {
  0% {
    left: 80%;
  }

  70% {
    left: 99%;
  }
	
	100% {
    left: 89%;
  }
}



</style>