<template>
  <div>
    <h1>WorldProfile</h1>
    <ProfileIconListItem/>
    <WorldProfileBattleLogList/>
    <WorldProfileCube/>
    <WorldDeck/>
    <WorldCardDetail/>
  </div>
</template>

<script>
import ProfileIconListItem from '@/components/ProfileIconListItem'
import WorldProfileBattleLogList from '@/components/world/profile/WorldProfileBattleLogList'
import WorldProfileCube from '@/components/world/profile/WorldProfileCube'
import WorldDeck from '@/components/world/profile/WorldDeck'
import WorldCardDetail from '@/components/world/profile/WorldCardDetail'

export default {
  name: 'WorldProfileView',
  components: {
    ProfileIconListItem,
    WorldProfileBattleLogList,
    WorldProfileCube,
    WorldDeck,
    WorldCardDetail
  }
}
</script>

<style>
.profile-worlddeck {
  border: 1px white solid;
	width: 70vw;
  margin: auto;
}
</style>