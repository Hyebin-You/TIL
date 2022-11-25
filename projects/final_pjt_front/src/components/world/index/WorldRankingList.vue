<template>
  <div>
    <div class="rank-title">현재 랭킹</div>
    <div
      class="ranking-line-box"
      v-for='(rank, index) in rankList'
      :key='rank.id'>
      <RankingListItem
        :user='rank'
        :index="index"
      />
    </div>
  </div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
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
      url: `${API_URL}/worlds/ranklist/`,
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      this.rankList = res.data.slice(0, 5)
      // console.log(this.rankList)
    })
    .catch((err) => {
      console.log(err);
    })
  }
}
</script>

<style scoped>
ul {
  list-style: none;
}
.rank-title {
  font-size: 35px;
}

.ranking-line-box {
  width: 100%;

}

</style>