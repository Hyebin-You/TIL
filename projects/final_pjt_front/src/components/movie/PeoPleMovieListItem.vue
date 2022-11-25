<template>
  <div class="listbox">
    <div @click="goPlaylistDetail">
      <span>{{ list.title }}</span>
    </div>
    <img v-if="showDelete" @click="deletePlaylist" class="x-delete" src="@/assets/x.png" alt="x">
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
const API_URL = 'http://3.112.52.213'
import axios from 'axios'
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
    },
    deletePlaylist() {
      axios({
        method: 'delete',
        url: `${API_URL}/movies/delete_playlist/${this.list.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.$store.dispatch('userData');
        })
        .catch((err) => {
          console.log(err);
        })
    }
  },
  computed: {
    showDelete() {
      if (this.$route.fullPath === '/index') {
        return false;
      } else {
        return true;
      }
    }
  }
}
</script>

<style scoped>

.listbox {
  width: 400px;
  height: 250px;
  margin: 25px;
  margin-top: 50px;
}
.listbox > div {
  text-align: start;
  font-size: 20px;
  display: flex;
  justify-content: space-between;
}
.listbox > div:hover {
  cursor: pointer;
  color: #A63268;
}
.x-delete {
  max-width: 20px;
  height: 20px;
  position: absolute;
  top: 58px;
  z-index: 10;
  right: 25px;
}
.x-delete:hover {
  cursor: pointer;
  transform: scale(1.2);
  color: #A63268;
}

.item-size-box {
  width: 100%;
  border-top: 1px solid seashell;
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