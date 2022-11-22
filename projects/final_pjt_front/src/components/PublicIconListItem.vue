<template>
  <div class="icon-box">
    <img src="@/assets/icons/mushroom.gif" alt="slime">
  </div>
</template>

<script>
export default {
  name: 'PublicIconListItem'
}
</script>

<style scoped>
.icon-box {
  width: 100px;
  height: 100px;
  margin: 10px;
  border: 1px dotted whitesmoke;
  border-radius: 10px;
}
.icon-box:hover {
  cursor: pointer;
}

.icon-box > img {
  width: 100%;
  height: 100%;
}

</style>