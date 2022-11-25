<template>
  <div>
    <WorldProfileUpdateDeck />
    <div style="height: 80px; font-size: 30px;"></div>
    <WorldCardDetail/>
		<div class="profile-box">
			<PublicProfile />
		</div>
    <div class="button-flex">
      <div class="myButton" @click="updateAttackDeck">공격덱구성하기</div>
      <div class="myButton" @click="updateDefenseDeck">방어덱구성하기</div>
    </div>
    <div class="profile-icon">
			<ProfileIconList />
		</div>
    <div class="profile-itemlist">
      <WorldProfileMyCardList />
    </div>
    <WorldProfileBattleLogList/>


  </div>
</template>

<script>
import ProfileIconList from '@/components/ProfileIconList'
import PublicProfile from "@/components/PublicProfile";
import WorldProfileBattleLogList from '@/components/world/profile/WorldProfileBattleLogList'
import WorldCardDetail from '@/components/world/profile/WorldCardDetail'
import WorldProfileMyCardList  from '@/components/world/profile/WorldProfileMyCardList'
import WorldProfileUpdateDeck  from '@/components/world/profile/WorldProfileUpdateDeck'

export default {
  name: 'WorldProfileView',
  components: {
    PublicProfile,
    ProfileIconList,
    WorldProfileBattleLogList,
    WorldCardDetail,
    WorldProfileMyCardList,
    WorldProfileUpdateDeck
  },
  computed: {
    user() {
      return this.$store.state.userObject
    },
		isLogin() {
			return this.$store.getters.isLogin;
		},    
  },
  methods: {
    updateAttackDeck() {
      const bodyScroll = document.querySelector("body");
			bodyScroll.style.overflow = "hidden";
      this.$store.commit('SHOW_DECKCARD_DETAIL', 'attack');
    },
    updateDefenseDeck() {
      const bodyScroll = document.querySelector("body");
			bodyScroll.style.overflow = "hidden";
      this.$store.commit('SHOW_DECKCARD_DETAIL', 'defense');
    }
  },
	created() { {
			if (!this.isLogin) {
				this.$router.push({ name: 'login'});
			}
		}
	},  
}
</script>

<style scoped>
.profile-worlddeck {
  border: 1px white solid;
	width: 70vw;
  margin: auto;
}
.profile-box {
	width: 80vw;
	height: 230px;
	margin: 0px auto;
	/* border: 1px solid whitesmoke; */
}
.profile-icon {
	width: 70vw;
	margin: 30px auto;
}
.profile-itemlist {
	width: 70vw;
	margin: auto;
}

.button-flex {
  display: flex;
  justify-content: space-evenly;
  width: 1100px;
  margin-left: 580px;
}

.myButton {
	box-shadow:inset 0px 1px 0px 0px #efdcfb;
	background-color:#dfbdfa;
	border-radius:6px;
	border: 2px solid #c584f3;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size: 17px;
	font-weight:bold;
	padding:6px 24px;
	text-decoration:none;
	text-shadow:0px 0.5px 0px #9752cc;
}
.myButton:hover {
	background-color:#bc80ea;
}
.myButton:active {
	position:relative;
	top: 1px;
}


</style>