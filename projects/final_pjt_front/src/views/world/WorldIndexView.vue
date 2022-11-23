<template>
  <div>
    <h1>WorldIndexView</h1>
    <WorldIndexNavBar/>
    <div style="display: flex; justify-content: space-evenly">
      <WorldRankingList/>
      <RankComment/>
    </div>
  </div>
</template>

<script>
import WorldRankingList from '@/components/world/index/WorldRankingList'
import WorldIndexNavBar from '@/components/world/index/WorldIndexNavBar'
import RankComment from '@/components/world/index/RankComment'

export default {
  name: 'WorldIndexView',
  components: {
    WorldRankingList,
    WorldIndexNavBar,
    RankComment
  }
}
</script>

<style>

</style>