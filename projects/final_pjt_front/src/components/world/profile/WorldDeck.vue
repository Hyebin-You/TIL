<template>
  <div class="listbox">
    <div>{{ deckName }}</div>
    <div class="item-size-box">
      <WorldDeckCard
        :card="deckList.card1"
        class="eventhover"
      />
      <WorldDeckCard
        :card="deckList.card2"
        class="eventhover"
      />
      <WorldDeckCard
        :card="deckList.card3"
        class="eventhover"
      />
    </div>
  </div>
</template>

<script>
import WorldDeckCard from '@/components/world/profile/WorldDeckCard'

export default {
  name: 'WorldDeck',
  components: {
    WorldDeckCard,
  },
  props: {
    deckList: Object,
    deckName: String
  },
  computed: {
    // user() {
    //   return this.
    // }
  }
}
</script>

<style scoped>
.listbox {
  width: 400px;
  height: 250px;
  /* border: 1px solid whitesmoke; */
  margin: 10px;
}
.listbox > div:nth-child(1) {
  font-size: 20px;
}


.item-size-box {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  position: relative;

}
.eventhover {
	width: 140px;
  height: 210px;
	transform: scale(0.9);
}

.eventhover:hover {
	cursor: pointer;
	transform: scale(1.05);
	transition: all 1s;
  z-index: 100;
}
</style>