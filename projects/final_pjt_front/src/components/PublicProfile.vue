<template>
  <div class="profile-whole">
    <h3>PublicProfile</h3>
    <div class="img-box">
      <img src="@/assets/pink.png" alt="">
    </div>
  </div>
</template>

<script>
export default {
  name: 'PublicProfile',
}
</script>

<style scoped>
.profile-whole {
  border: 1px solid skyblue;
  margin: auto;
  height: 90%;
  width: 90%;
}
.img-box {
  width: 150px;
  height: 150px;
}
.img-box > img {
  width: 100%;
  height: 100%;
}



</style>