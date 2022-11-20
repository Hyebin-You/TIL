<template>
  <div class="navBar">
    <nav>
      <router-link :to="{ name: 'index' }">Index</router-link> |
      <router-link :to="{ name: 'login' }">Login</router-link> |
      <router-link :to="{ name: 'signup' }">SignUp</router-link> |
      <router-link :to="{ name: 'nickname' }">SignUpNick</router-link> |
      <router-link :to="{ name: 'likegenre' }">SignUpGenre</router-link> |
      <router-link :to="{ name: 'update' }">Update</router-link> |
      <router-link :to="{ name: 'search' }">Search</router-link> |
      <router-link :to="{ name: 'movieshop' }">MovieShop</router-link> |
      <router-link :to="{ name: 'detail' }">Detail</router-link> |
      <router-link :to="{ name: 'movieprofile' }">MovieProfile</router-link> |
      <router-link :to="{ name: 'worldindex' }">WorldIndex</router-link> |
      <router-link :to="{ name: 'worldprofile' }">WorldProfile</router-link> |
      <router-link :to="{ name: 'worldfight' }">WorldFight</router-link> |
      <router-link :to="{ name: 'worldshop' }">WorldShopView</router-link> |
    </nav>
  </div>
</template>

<script>
export default {
  name: "NavBar"
}
</script>

<style>
.navBar {
  width: 100vw;
  border: 1px solid black;
  background-color: rgb(63, 0, 0);
  
}
</style>