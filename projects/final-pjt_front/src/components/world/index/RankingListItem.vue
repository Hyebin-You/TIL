<template>
  <div class="ranking-box" v-if='user'>
    <div>{{ index + 1 }}위 </div>
    <img :src="require(`@/assets/${user.user_icon}`)" alt="icon" />
    <div class="ranking-private-box">{{ user?.nickname }}</div>
    <div class="ranking-private-box">{{ user?.tier }}</div>
    <div class="ranking-private-box">{{ user?.win_point }}</div>
    <WorldDeckCard
      class='eventhover'
      :card='user?.attacklist_set[0].card1'
    />
    <WorldDeckCard
      class='eventhover'
      :card='user?.attacklist_set[0].card2'
    />
    <WorldDeckCard
      class='eventhover'
      :card='user?.attacklist_set[0].card3'
    />
  </div>
</template>

<script>
import WorldDeckCard from '@/components/world/profile/WorldDeckCard'

export default {
  name: 'RankingListItem',
  components: {
    WorldDeckCard
  },
  props: {
    user: Object,
    index: Number,
  }
}
</script>

<style scoped>
.ranking-box {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  border: 1px solid white;
}
.ranking-box > div:nth-child(1) {
  font-size: 50px;
  width: 120px;
}


.ranking-box > img:nth-child(2) {
  width: 80px;
  height: 80px;
}

.ranking-private-box {
  width: 150px;
  text-align: center;
  height: fit-content;
}


.eventhover {
  height: 100px;
	width: 70px;
	transform: scale(0.9);
}
</style>