<template>
  <div class="listbox">
    <span @click="goPlaylistDetail">{{ list.title }}</span>
    <div class="item-size-box">
      <LikeMovieListItem
        v-for="(movie, index) in list.in_movies"
        :key="movie.title" 
        :movie="movie"
        :index="index"
        class="eventhover"
        />
    </div>
  </div>
</template>

<script>
import LikeMovieListItem from '@/components/movie/profile/LikeMovieListItem'

export default {
  name: 'PeoPleMovieListItem',
  components: {
    LikeMovieListItem,
  },
  props: {
    list: Object,
  },
  methods: {
    goPlaylistDetail() {
      this.$store.commit('SAVE_PLAYLIST', this.list);
      this.$router.push({ name: 'playlist' });
    }
  },
  created() {
    console.log(this.list.in_movies[0]);
  }
}
</script>

<style scoped>

.listbox {
  width: 400px;
  height: 250px;
  border: 1px solid whitesmoke;
  margin: 10px;
}
/* .item-flex-box {
  display: flex;
  justify-content: flex-start;
} */

.item-size-box {
  width: 100%;
  display: flex;
  justify-content: flex-start;
  position: relative;

}
.eventhover {
	width: 140px;
	transform: scale(0.9);
}

.eventhover:hover {
	cursor: pointer;
	transform: scale(1.05);
	transition: all 1s;
  z-index: 100;
}


</style>