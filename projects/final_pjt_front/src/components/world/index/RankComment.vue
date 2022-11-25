<template>
  <div style="height: 100%;">
    <div class="comment-title">익명 게시판</div>
    <div class="scroll-box">
      <li v-for='comment in rankCommentList.slice(0, -1)' :key='comment.id'>
        {{ comment.content }}
      </li>
    </div>
    <div class="comment-flex">
      <input type="text" v-model="inputContent" @keyup.enter="createComment" maxlength="15">
      <div class="myButton" @click="createComment">작성!</div>
    </div>
  </div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
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
      // console.log('댓글왜안댐')
      if (!this.inputContent.trim()) {
        this.inputContent = ''
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/worlds/create_rankcomment/`,
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

<style scoped>
input {
  width: 150px;
  border-radius: 5px;
}


.comment-flex {
  display: flex;
  align-items: center;
  justify-content: center;
} 

.comment-title {
  font-size: 35px;
}
.scroll-box {
  text-align: start;
  overflow-y: scroll;
  height: 80%;
  padding-left: 15px;
  padding-top: 5px;
}
.myButton {
	box-shadow:inset 0px 1px 0px 0px #efdcfb;
	background-color:#dfbdfa;
	border-radius:6px;
	border: 2px solid #c584f3;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size: 14px;
	font-weight:bold;
  margin-left: 2px;
	padding:2px 8px;
	text-decoration:none;
	text-shadow:0px 0.5px 0px #9752cc;
}
.myButton:hover {
	background-color:#bc80ea;
}
.myButton:active {
	position:relative;
	top: 1px;
}

</style>