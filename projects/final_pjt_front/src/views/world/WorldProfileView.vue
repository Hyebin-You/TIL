<template>
  <div>
    <WorldCardDetail/>
    <h1>WorldProfile</h1>
    <PublicIconListItem/>
    <WorldProfileBattleLogList/>
    <WorldProfileCube/>
    <div style="display: flex">
      <WorldDeck
        deck-name='Attack List'
        :deck-list='user.attacklist_set[0]'
      />
      <WorldDeck
        deck-name='Defense List'
        :deck-list='user.defenselist_set[0]'
      />
    </div>
  </div>
</template>

<script>
import PublicIconListItem from '@/components/PublicIconListItem'
import WorldProfileBattleLogList from '@/components/world/profile/WorldProfileBattleLogList'
import WorldProfileCube from '@/components/world/profile/WorldProfileCube'
import WorldDeck from '@/components/world/profile/WorldDeck'
import WorldCardDetail from '@/components/world/profile/WorldCardDetail'

export default {
  name: 'WorldProfileView',
  components: {
    PublicIconListItem,
    WorldProfileBattleLogList,
    WorldProfileCube,
    WorldDeck,
    WorldCardDetail
  },
  computed: {
    user() {
      return this.$store.state.userObject
    }
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