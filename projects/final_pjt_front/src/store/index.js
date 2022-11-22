import Vue from 'vue'
import Vuex from 'vuex'
import VueCarousel from 'vue-carousel';
import axios from 'axios';
import createPersistedState from 'vuex-persistedstate'
 
Vue.use(Vuex);
Vue.use(VueCarousel);

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  
  state: {
    token: null,
    userObject: null,
    detailBoxShadowStyle: 'none',
    detailMovie: null,
    searchList: null,
    playList: null,
    detailUsercard: null,
  },
  getters: {
  },
  mutations: {
    OFF_DETAIL(state) {
      //detailBosShadowStyle => flex or none
      state.detailBoxShadowStyle = 'none'
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
      state.playlist = play_list;
    },
    SHOW_USERCARD_DETAIL(state, usercard) {
      state.detailUsercard = usercard;
    }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;

      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/signup`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          context.commit('SIGN_UP', res.data.key);
        })
        .catch((err) => {
          console.log(err);
        })
    },
    userData(context) {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/user_detail/`,
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
    }
  },
  modules: {
  }
})
