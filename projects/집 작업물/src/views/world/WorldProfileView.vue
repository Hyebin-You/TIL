<template>
  <div>
    <WorldProfileUpdateDeck />
    <div style="height: 80px; font-size: 30px;"></div>
    <WorldCardDetail/>
		<div class="profile-box">
			<PublicProfile />
		</div>
    <button @click="updateAttackDeck">공격덱구성하기</button>
    <ProfileIconList />
    <WorldProfileMyCardList />
    <WorldProfileBattleLogList/>
    <WorldProfileCube/>

  </div>
</template>

<script>
import ProfileIconList from '@/components/ProfileIconList'
import PublicProfile from "@/components/PublicProfile";
import WorldProfileBattleLogList from '@/components/world/profile/WorldProfileBattleLogList'
import WorldProfileCube from '@/components/world/profile/WorldProfileCube'
import WorldCardDetail from '@/components/world/profile/WorldCardDetail'
import WorldProfileMyCardList  from '@/components/world/profile/WorldProfileMyCardList'
import WorldProfileUpdateDeck  from '@/components/world/profile/WorldProfileUpdateDeck'

export default {
  name: 'WorldProfileView',
  components: {
    PublicProfile,
    ProfileIconList,
    WorldProfileBattleLogList,
    WorldProfileCube,
    WorldCardDetail,
    WorldProfileMyCardList,
    WorldProfileUpdateDeck
  },
  computed: {
    user() {
      return this.$store.state.userObject
    }
  },
  methods: {
    updateAttackDeck() {
      const bodyScroll = document.querySelector("body");
			bodyScroll.style.overflow = "hidden";
      this.$store.commit('SHOW_DECKCARD_DETAIL');
    }
  }
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


</style>