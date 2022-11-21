<template>
  <div @click="showUsercardDetail(card)">
    <h3>WorldCard</h3>
  </div>
</template>

<script>
export default {
  name: 'WorldCard',
  props: {
    card: Object,
  },
  methods: {
    showUsercardDetail(card) {
      this.$store.commit('SHOW_USERCARD_DETAIL', card)
    }
  }
}
</script>

<style>

</style>