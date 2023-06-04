import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '@/views/account/SignUpView'
import LoginView from '@/views/account/LoginView'
import IndexView from '@/views/movie/IndexView'
import SearchView from '@/views/movie/SearchView'
import MovieShopView from '@/views/movie/MovieShopView'
import MovieProfileView from '@/views/movie/MovieProfileView'
import WorldIndexView from '@/views/world/WorldIndexView'
import WorldProfileView from '@/views/world/WorldProfileView'
import WorldFightView from '@/views/world/WorldFightView'
import WorldShopView from '@/views/world/WorldShopView'
import SignUpNickNameView from '@/views/account/SignUpNickNameView'
import SignUpLikeGenreListView from '@/views/account/SignUpLikeGenreListView'
import MoviePlayListDetailView from '@/views/movie/MoviePlayListDetailView'
import PinkBeanView from '@/views/world/PinkBeanView'

Vue.use(VueRouter)

const routes = [
  {
    path: '',
    redirect: { name: 'login' }
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/nickname',
    name: 'nickname',
    component: SignUpNickNameView
  },
  {
    path: '/likegenre',
    name: 'likegenre',
    component: SignUpLikeGenreListView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/index',
    name: 'index',
    component: IndexView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/movieshop',
    name: 'movieshop',
    component: MovieShopView
  },
  {
    path: '/movieprofile',
    name: 'movieprofile',
    component: MovieProfileView
  },
  {
    path: '/worldindex',
    name: 'worldindex',
    component: WorldIndexView
  },
  {
    path: '/worldprofile',
    name: 'worldprofile',
    component: WorldProfileView
  },
  {
    path: '/worldfight',
    name: 'worldfight',
    component: WorldFightView
  },
  {
    path: '/worldshop',
    name: 'worldshop',
    component: WorldShopView
  },
  {
    path: '/playlist',
    name: 'playlist',
    component: MoviePlayListDetailView
  },
  {
    path: '/pinkbean',
    name: 'pinkbean',
    component: PinkBeanView
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
