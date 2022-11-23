<template>
  <div>
    <h3>WorldRankingList</h3>
    <div>
      <h3>현재 랭킹</h3>
        <RankingListItem
          v-for='rank in rankList'
          :key='rank.nickname'
          :user='rank'
        />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import RankingListItem from '@/components/world/index/RankingListItem'

export default {
  name: 'WorldRankingList',
  components: {
    RankingListItem
  },
  data() {
    return {
      rankList: null,
    }
  },
  created() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/worlds/ranklist/',
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      this.rankList = res.data
    })
  }
}
</script>

<style scoped>
ul {
  list-style: none;
}
</style>