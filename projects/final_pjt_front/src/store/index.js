import Vue from 'vue'
import Vuex from 'vuex'
import VueCarousel from 'vue-carousel';
import createPersistedState from 'vuex-persistedstate'
 
Vue.use(Vuex);
Vue.use(VueCarousel);

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],

  state: {
    detailSwitch: false,
    detailMovie: null,
  },
  getters: {
  },
  mutations: {
    SHOW_DETAIL(state, movie) {
      console.log('@@', '오냐');
      state.detailSwitch = true;
      state.detailMovie = movie;
    }
  },
  actions: {
    show_detail(context, movie) {
      context.commit('SHOW_DETAIL', movie);
      
    }
  },
  modules: {
  }
})
