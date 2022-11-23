<template>
  <div>
    <h2>익명 게시판</h2>
    <div style="text-align: start;">
      <li v-for='comment in rankCommentList' :key='comment.id'>
        {{ comment.content }}
      </li>
      <input type="text" v-model=inputContent @keyup.enter="createComment">
      <button @click="createComment">작성!</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RankComment',
  data() {
    return {
      inputContent: '',
    }
  },
  methods: {
    createComment() {
      if (!this.inputContent.trim()) {
        this.inputContent = ''
        return
      }

      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/worlds/create_rankcomment/',
        data: {
          'content': this.inputContent
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.$store.dispatch('getRankCommentList')
        this.inputContent = ''
      })
    },
    renewCommentList() {
      this.$store.dispatch('getRankCommentList')
    }
  },
  computed: {
    rankCommentList() {
      return this.$store.state.rankComment
    }
  },
  created() {
    this.$store.dispatch('getRankCommentList')
    // setInterval(this.renewCommentList, 3000)
  }
}
</script>

<style>

</style>