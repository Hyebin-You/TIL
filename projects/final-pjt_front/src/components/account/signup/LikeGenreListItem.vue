<template>
  <div>
    <div @click="selectGenre" class="genre-box" >
      <p id="genre-box">{{ genre }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LikeGenreListItem',
  props: {
    genre: String,
  },
  data() {
    return {
    }
  },
  methods: {
    selectGenre(event) {
        this.selectGenreItem = event.target.innerText;
			// console.log('@@@@@@@@@@@', this.selectGenreItem);
        event.target.classList.toggle('select-box');
        this.$emit('genre-data', event.target.innerText);
      }
		}
  }

</script>

<style scoped>
.genre-box {
  font-family: "maplestory";
  font-size: 1.2rem;
  width: 150px;
  height: 70px;
  padding: 0px 10px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  color: white;
}

.genre-box > p {
  margin: 10px 0px;
  border: 2px solid white;
  border-radius: 20px;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.genre-box > p:hover {
  cursor: pointer;
  color: #A63268;
}
.select-box {
  color: #A63268;
}


</style>