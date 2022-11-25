import Vue from 'vue'
import Vuex from 'vuex'
import VueCarousel from 'vue-carousel';
import axios from 'axios';
import createPersistedState from 'vuex-persistedstate'
import router from '@/router/index'
import swal from 'sweetalert';


Vue.use(Vuex);
Vue.use(VueCarousel);
const API_URL = 'http://3.112.52.213'
export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  
  state: {
    token: null,
    userObject: null,
    maple: false,
    detailBoxShadowStyle: 'none',
    detailCardBoxShadowStyle: 'none',
    detailDeckBoxShadowStyle: 'none',
    detailMovie: null,
    searchList: null,
    playList: null,
    detailUsercard: null,
    deckName: null,
    rankComment: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    OFF_DETAIL(state) {
      //detailBosShadowStyle => flex or none
      state.detailBoxShadowStyle = 'none';
    },
    OFF_CARDDETAIL(state) {
      state.detailCardBoxShadowStyle = 'none';
    },
    OFF_DECKDETAIL(state) {
      state.detailDeckBoxShadowStyle = 'none';
    },
    SHOW_DETAIL(state, movie) {
      //detailBosShadowStyle => flex or none
      state.detailBoxShadowStyle = '';
      state.detailMovie = movie;
    },
    SEARCH_LIST(state, movies) {
      state.searchList = movies;
    },
    SIGN_UP(state, token) {
      state.token = token
    },
    USER_DATA(state, user_data) {
      state.userObject = user_data;
    },
    SAVE_TOKEN(state, token) {
      state.token = token;
    },
    SAVE_PLAYLIST(state, play_list) {
      state.playList = play_list;
    },
    SHOW_USERCARD_DETAIL(state, usercard) {
      state.detailCardBoxShadowStyle = '';
      state.detailUsercard = usercard;
    },
    SHOW_DECKCARD_DETAIL(state, status) {
      state.detailDeckBoxShadowStyle = '';
      state.deckName = status
    },
    Change_USERCARD(state, usercard) {
      state.detailUsercard = usercard
    },
    USER_LOGOUT(state) {
      state.token = null;
      state.userObject = null;
      state.maple = false;
      state.detailBoxShadowStyle = 'none';
      state.detailCardBoxShadowStyle = 'none';
      state.detailDeckBoxShadowStyle = 'none';
      state.detailMovie = null;
      state.searchList = null;
      state.playList = null;
      state.detailUsercard = null;
      router.push({ name: 'login' });
    },
    RANKCOMMENTLIST(state, rcList) {
      state.rankComment = rcList
    },
    CHANGE_WORLD(state) {
      state.maple = !state.maple;
      const bodyColor = document.querySelector('body');
      if (state.maple) {
        bodyColor.style.backgroundColor = 'rgb(186 150 191)';
      } else {
        bodyColor.style.backgroundColor = 'black';
      }
  }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          context.commit('SIGN_UP', res.data.key);
          router.push({ name: 'nickname'});
        })
        .catch((err) => {
          console.log(err);
          swal('다시 입력해주세요', '아이디 중복이거나 패스워드가 너무 단순합니다.', 'warning');
        })
    },
    userData(context) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/user_detail/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('USER_DATA', res.data);
        })
        .catch((err) => {
          console.log(err);
        })
    },
    savePlayListDetail(context, list_id) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/playlist_detail/${list_id}/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          // console.log('!!', res.data);
          context.commit('SAVE_PLAYLIST', res.data);
        })
        .catch((err) => {
          console.log(err);
        })
    },
    getRankCommentList(context) {
      axios({
        method: 'get',
        url: `${API_URL}/worlds/rankcomment_list/`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
      .then((res) => {
        context.commit('RANKCOMMENTLIST', res.data)
      })
      .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
