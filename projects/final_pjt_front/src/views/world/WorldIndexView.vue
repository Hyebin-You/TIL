<template>
  <div>
    <h1>WorldIndexView</h1>
    <WorldIndexNavBar/>
    <WorldRankingList/>
  </div>
</template>

<script>
import WorldRankingList from '@/components/world/index/WorldRankingList'
import WorldIndexNavBar from '@/components/world/index/WorldIndexNavBar'

export default {
  name: 'WorldIndexView',
  components: {
    WorldRankingList,
    WorldIndexNavBar,
  }
}
</script>

<style>

</style>