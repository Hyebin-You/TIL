<template>
  <div>
    MyMovieList
    <MyMovieListItem/>
  </div>
</template>

<script>
import MyMovieListItem from '@/components/movie/MyMovieListItem'

export default {
  name: 'MyMovieList',
  components: {
    MyMovieListItem,
  }
}
</script>

<style>

</style>