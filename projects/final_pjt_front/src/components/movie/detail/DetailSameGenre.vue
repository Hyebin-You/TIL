<template>
  <div class="detail-same">
    <h3>DetailSameGenre</h3>
    <DetailSameGenreItem/>
  </div>
</template>

<script>
import DetailSameGenreItem from "@/components/movie/detail/DetailSameGenreItem";

export default {
  name: 'DetailSameGenre',
  components: {
    DetailSameGenreItem,
  }
}
</script>

<style>
.detail-same {
  width: 800px;
  border: 1px solid black;
}
</style>