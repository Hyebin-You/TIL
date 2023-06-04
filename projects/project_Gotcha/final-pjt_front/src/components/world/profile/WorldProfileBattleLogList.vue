<template>
  <div class="battle-log-whole">
    <div style="font-size: 25px;"> {{ user.nickname }}님의 대전기록</div>
    <div class="battle-log-box">
      <!-- <p>{{ userLogList }}</p> -->
      <div  v-for="log in userLogList.slice(-5)" :key='log.id'>
        <div>
          <div >{{ user.nickname }}</div>
          <img :src="require(`@/assets/${log.my_card1_img}`)" alt="">
          <img :src="require(`@/assets/${log.my_card2_img}`)" alt="">
          <img :src="require(`@/assets/${log.my_card3_img}`)" alt="">
        </div>
        <div style="margin: 20px;" >
          <p>{{ log.log }}</p>
        </div>
        <div >
          <div style="color: crimson;">{{ log.enermy_nickname }}</div>
          <img :src="require(`@/assets/${log.enermy_card1_img}`)" alt="">
          <img :src="require(`@/assets/${log.enermy_card2_img}`)" alt="">
          <img :src="require(`@/assets/${log.enermy_card3_img}`)" alt="">
        </div>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'WorldProfileBattleLogList',
  computed: {
    userLogList() {
      return this.$store.state.userObject.battlelog_set
    },
    user() {
      return this.$store.state.userObject
    }
  },
  created() {
    this.$store.dispatch('userData')
  }
}
</script>

<style scoped>
img {
  width: 50px;
  height: 60px;
}
.battle-log-whole {
  display: flex; 
  justify-content: center;
  flex-wrap: wrap;
}

.battle-log-box {
  display: flex; 
  justify-content: space-evenly;
  flex-wrap: wrap;
  width: 500px;
}

.battle-log-box > div {
  display: flex;
  justify-content: center;
  border: white 1px solid;
  padding: 5px 40px;
  font-size: 20px;
}


/* .battle-result {
  display: flex; 
  border: 2px solid white;
} */
</style>