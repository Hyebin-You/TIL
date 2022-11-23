<template>
  <div style="display:flex;">
    <p style="margin-right: 2px">{{ user.nickname }}</p>
    <p style="margin-left:1px; margin-right:1px">{{ user.tier }}</p>
    <p style="margin-left:1px; margin-right:1px">{{ user.win_point }}</p>
    <WorldDeckCard
      class='cardbox eventhover'
      :card='user.attacklist_set[0].card1'
    />
    <WorldDeckCard
      class='cardbox eventhover'
      :card='user.attacklist_set[0].card2'
    />
    <WorldDeckCard
      class='cardbox eventhover'
      :card='user.attacklist_set[0].card3'
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
    user: Object
  }
}
</script>

<style scoped>
.cardbox {
  height: 100px;
  width: 70px;
}

.eventhover {
  height: 100px;
	width: 70px;
	transform: scale(0.9);
}
</style>