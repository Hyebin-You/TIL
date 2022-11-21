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
    userObject: {
      "username": "test",
      "nickname": "하늘 수정",
      "point": 8600,
      "tier": "Bronze",
      "win_point": 150,
      "blackcube": 10,
      "redcube": 2,
      "like_genres": [
          {
              "name": "모험"
          }
      ],
      "playlist_set": [],
      "attacklist_set": [
          {
              "id": 1,
              "card1": {
                  "id": 3,
                  "cardname": "한가인",
                  "isnormal": true,
                  "attack": 100,
                  "defense": 10,
                  "life": 600,
                  "img_url": "card_img/kwak.jpg",
                  "ability1": "체력+06%",
                  "ability2": "방어력+03%",
                  "ability3": "방어력+03%",
                  "ability_grade": "epic",
                  "user": 1
              },
              "card2": {
                  "id": 5,
                  "cardname": "콜린퍼스",
                  "isnormal": true,
                  "attack": 100,
                  "defense": 10,
                  "life": 600,
                  "img_url": "card_img/콜린퍼스.jpg",
                  "ability1": "공격력+06%",
                  "ability2": "방어력+03%",
                  "ability3": "방어력+06%",
                  "ability_grade": "epic",
                  "user": 1
              },
              "card3": {
                  "id": 8,
                  "cardname": "공유",
                  "isnormal": true,
                  "attack": 100,
                  "defense": 10,
                  "life": 600,
                  "img_url": "card_img/공유.jpg",
                  "ability1": "체력+03%",
                  "ability2": "공격력+03%",
                  "ability3": "공격력+06%",
                  "ability_grade": "epic",
                  "user": 1
              },
              "user": 1
          }
      ],
      "defenselist_set": [
          {
              "id": 1,
              "card1": {
                  "id": 3,
                  "cardname": "한가인",
                  "isnormal": true,
                  "attack": 100,
                  "defense": 10,
                  "life": 600,
                  "img_url": "card_img/kwak.jpg",
                  "ability1": "체력+06%",
                  "ability2": "방어력+03%",
                  "ability3": "방어력+03%",
                  "ability_grade": "epic",
                  "user": 1
              },
              "card2": {
                  "id": 5,
                  "cardname": "콜린퍼스",
                  "isnormal": true,
                  "attack": 100,
                  "defense": 10,
                  "life": 600,
                  "img_url": "card_img/콜린퍼스.jpg",
                  "ability1": "공격력+06%",
                  "ability2": "방어력+03%",
                  "ability3": "방어력+06%",
                  "ability_grade": "epic",
                  "user": 1
              },
              "card3": {
                  "id": 8,
                  "cardname": "공유",
                  "isnormal": true,
                  "attack": 100,
                  "defense": 10,
                  "life": 600,
                  "img_url": "card_img/공유.jpg",
                  "ability1": "체력+03%",
                  "ability2": "공격력+03%",
                  "ability3": "공격력+06%",
                  "ability_grade": "epic",
                  "user": 1
              },
              "user": 1
          }
      ],
      "battlelog_set": [
          {
              "id": 1,
              "log": "패배",
              "enermy_nickname": "별",
              "user": 1
          },
          {
              "id": 2,
              "log": "승리",
              "enermy_nickname": "달",
              "user": 1
          },
          {
              "id": 3,
              "log": "승리",
              "enermy_nickname": "산",
              "user": 1
          },
          {
              "id": 4,
              "log": "패배",
              "enermy_nickname": "산",
              "user": 1
          }
      ],
      "usercard_set": [
          {
              "id": 1,
              "cardname": "다니엘래드클리프",
              "isnormal": true,
              "attack": 100,
              "defense": 10,
              "life": 600,
              "img_url": "card_img/다니엘래드클리프.jpg",
              "ability1": "체력+03%",
              "ability2": "공격력+06%",
              "ability3": "방어력+03%",
              "ability_grade": "epic",
              "user": 1
          },
          {
              "id": 2,
              "cardname": "김대명",
              "isnormal": true,
              "attack": 100,
              "defense": 10,
              "life": 600,
              "img_url": "card_img/김대명.jpg",
              "ability1": "방어력+03%",
              "ability2": "체력+06%",
              "ability3": "방어력+06%",
              "ability_grade": "epic",
              "user": 1
          },
          {
              "id": 3,
              "cardname": "한가인",
              "isnormal": true,
              "attack": 100,
              "defense": 10,
              "life": 600,
              "img_url": "card_img/kwak.jpg",
              "ability1": "체력+06%",
              "ability2": "방어력+03%",
              "ability3": "방어력+03%",
              "ability_grade": "epic",
              "user": 1
          },
          {
              "id": 4,
              "cardname": "콜린퍼스",
              "isnormal": true,
              "attack": 100,
              "defense": 10,
              "life": 600,
              "img_url": "card_img/콜린퍼스.jpg",
              "ability1": "체력+03%",
              "ability2": "체력+03%",
              "ability3": "방어력+03%",
              "ability_grade": "epic",
              "user": 1
          },
          {
              "id": 5,
              "cardname": "콜린퍼스",
              "isnormal": true,
              "attack": 100,
              "defense": 10,
              "life": 600,
              "img_url": "card_img/콜린퍼스.jpg",
              "ability1": "공격력+06%",
              "ability2": "방어력+03%",
              "ability3": "방어력+06%",
              "ability_grade": "epic",
              "user": 1
          },
          {
              "id": 6,
              "cardname": "채수빈",
              "isnormal": true,
              "attack": 100,
              "defense": 10,
              "life": 600,
              "img_url": "card_img/채수빈.jpg",
              "ability1": "방어력+03%",
              "ability2": "공격력+03%",
              "ability3": "공격력+03%",
              "ability_grade": "epic",
              "user": 1
          },
          {
              "id": 7,
              "cardname": "채수빈",
              "isnormal": true,
              "attack": 100,
              "defense": 10,
              "life": 600,
              "img_url": "card_img/채수빈.jpg",
              "ability1": "방어력+03%",
              "ability2": "방어력+03%",
              "ability3": "방어력+06%",
              "ability_grade": "epic",
              "user": 1
          },
          {
              "id": 8,
              "cardname": "공유",
              "isnormal": true,
              "attack": 100,
              "defense": 10,
              "life": 600,
              "img_url": "card_img/공유.jpg",
              "ability1": "체력+03%",
              "ability2": "공격력+03%",
              "ability3": "공격력+06%",
              "ability_grade": "epic",
              "user": 1
          },
          {
              "id": 9,
              "cardname": "원빈",
              "isnormal": true,
              "attack": 100,
              "defense": 10,
              "life": 600,
              "img_url": "card_img/원빈.jpg",
              "ability1": "공격력+03%",
              "ability2": "공격력+06%",
              "ability3": "공격력+06%",
              "ability_grade": "epic",
              "user": 1
          },
          {
              "id": 50,
              "cardname": "이동욱",
              "isnormal": true,
              "attack": 100,
              "defense": 100,
              "life": 100,
              "img_url": "card_img/이동욱.jpg",
              "ability1": "체력+06%",
              "ability2": "방어력+03%",
              "ability3": "공격력+06%",
              "ability_grade": "epic",
              "user": 1
          }
      ],
      "like_movies": []
  },
    detailBoxShadowStyle: 'none',
    detailMovie: null,
    searchList: null,
    detailUsercard: {
      "id": 50,
      "cardname": "이동욱",
      "isnormal": true,
      "attack": 100,
      "defense": 100,
      "life": 100,
      "img_url": "card_img/이동욱.jpg",
      "ability1": "체력+06%",
      "ability2": "방어력+03%",
      "ability3": "공격력+06%",
      "ability_grade": "epic",
      "user": 1
  },
  },
  getters: {
  },
  mutations: {
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