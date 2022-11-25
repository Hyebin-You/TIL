<template>
  <transition name="fade-detail" mode="out-in">
    <div
      v-if="Card"
      id="dropshadow"
      :style="{ display: detailCardBoxShadowStyle }"
      @click="detailCardOff"
      class="dropshadow">
      <div class="detailbox">
        <h1>CardDetail</h1>
        <div class="detail-flex">
          <div>
            <img class="actor-img" :src="require(`@/assets/${Card?.img_url}`)" alt="없넹..."
              :class=" Card.isnormal? 'isSilver': 'isGold' "
              >
            <div class="actor-bottom-profile">
              <div>
                <p style="font-size: 40px; font-weight: bold;">{{ Card?.cardname }}</p>
              </div>
              <div style="font-size: 20px; text-align: start;">
                <p>공격력 : {{ Card?.attack }}</p>
                <p>방어율 : {{ Card?.defense }}%</p>
                <p>체력 : {{ Card?.life }}</p>
              </div>
            </div>
          </div>
          <div class="right-side">
            <div class="cube-box">
              <div @click='useBlack' class="cube" >
                <img :src="require(`@/assets/blackcube.png`)" alt="blackcube">
                <div>{{ User.blackcube }}</div>
              </div>
              <div @click='useRed' class="cube" >
                <img :src="require(`@/assets/redcube.png`)" alt="blackcube">
                <div>{{ User.redcube }}</div>
              </div>
            </div>
            <p>잠재능력 등급 : {{ ability_grade }}</p>
            <p>{{ ability1 }}</p>
            <p>{{ ability2 }}</p>
            <p>{{ ability3 }}</p>
            <hr>
            <p>잠재능력 등급 : {{ changedAbilityGrade }}</p>
            <p>{{ changedAbility1 }}</p>
            <p>{{ changedAbility2 }}</p>
            <p>{{ changedAbility3 }}</p>
            <button @click='sendResult'>해당 결과를 적용하시겠습니까?</button>
          </div>
        </div>

      </div>
    </div>
  </transition>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import _ from 'lodash'
import axios from 'axios'

export default {
  name: 'WorldCardDetail',
  data() {
    return {
      changedAbilityGrade: null,
      changedAbility1: null,
      changedAbility2: null,
      changedAbility3: null,
      epicAbility: ['공격력+03%', '공격력+06%', '방어력+03%', '방어력+06%', '체력+03%', '체력+06%'],
      uniqueAbility: ['공격력+06%', '공격력+09%', '방어력+06%', '방어력+09%', '체력+06%', '체력+09%'],
      legendAbility: ['공격력+09%', '공격력+12%', '방어력+09%', '방어력+12%', '체력+09%', '체력+12%'],
    }
  },
  methods: {
    sleep(ms) {
      const wakeUpTime = Date.now() + ms;
      while (Date.now() < wakeUpTime) {
        console.log()
      }
    },
    randomAbility(grade) {
      let abilityList
      if (grade === '에픽') {
        abilityList = this.epicAbility
      } else if (grade === '유니크') {
        abilityList = this.uniqueAbility
      } else {
        abilityList = this.legendAbility
      }

      if (_.random(1, 100) <= 15) {
        return abilityList[0]
      } else if (_.random(1, 100) > 15 && _.random(1, 100) <= 20) {
        return abilityList[1]
      } else if (_.random(1, 100) > 20 && _.random(1, 100) <= 50) {
        return abilityList[2]
      } else if (_.random(1, 100) > 50 && _.random(1, 100) <= 60) {
        return abilityList[3]
      } else if (_.random(1, 100) > 60 && _.random(1, 100) <= 90) {
        return abilityList[4]
      } else {
        return abilityList[5]
      }
    },
    useBlack() {
      if (this.User.blackcube === 0) {
        this.$swal('큐브가 없습니다!!','큐브 구매해주세요!','warning');
        return
      }

      if (this.ability_grade === '에픽') {
        if (_.random(1, 100) <= 8) {
          this.changedAbilityGrade = '유니크'
        } else {
          this.changedAbilityGrade = '에픽'
        }
      } else if (this.ability_grade === '유니크') {
        if (_.random(1, 100) <= 4) {
          this.changedAbilityGrade = '레전드리'
        } else {
          this.changedAbilityGrade = '유니크'
        }
      } else {
        this.changedAbilityGrade = '레전드리'
      }

      this.sleep(500)
      this.changedAbility1 = this.randomAbility(this.changedAbilityGrade)
      this.changedAbility2 = this.randomAbility(this.changedAbilityGrade)
      this.changedAbility3 = this.randomAbility(this.changedAbilityGrade)
      
      axios({
        method: 'POST',
        url: `${API_URL}/accounts/use_cube/`,
        data: {
          'cubename': 'black'
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.$store.dispatch('userData')
      })
      .catch((err) =>{
        console.log('블큡 사용함수 에러', err)
      })
    },
    useRed() {
      if (this.User.redcube === 0) {
        this.$swal('큐브가 없습니다!!','큐브 구매해주세요!','warning');
        return
      }

      if (this.ability_grade === '에픽') {
        if (_.random(1, 100) <= 6) {
          this.changedAbilityGrade = '유니크'
        } else {
          this.changedAbilityGrade = '에픽'
        }
      } else if (this.ability_grade === '유니크') {
        if (_.random(1, 100) <= 2) {
          this.changedAbilityGrade = '레전드리'
        } else {
          this.changedAbilityGrade = '유니크'
        }
      } else {
        this.changedAbilityGrade = '레전드리'
      }

      this.sleep(500)
      this.changedAbility1 = this.randomAbility(this.changedAbilityGrade)
      this.changedAbility2 = this.randomAbility(this.changedAbilityGrade)
      this.changedAbility3 = this.randomAbility(this.changedAbilityGrade)

      axios({
        method: 'POST',
        url: `${API_URL}/accounts/use_cube/`,
        data: {
          'cubename': 'red'
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.$store.dispatch('userData')
      })
      .catch((err) =>{
        console.log('레큡 사용함수 에러', err)
      })
    },
    sendResult() {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/modify_card/`,
        data: {
          'card_pk': this.Card.id,
          'ability_grade': this.changedAbilityGrade,
          'ability1': this.changedAbility1,
          'ability2': this.changedAbility2,
          'ability3': this.changedAbility3
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.changedAbilityGrade = null
        this.changedAbility1 = null
        this.changedAbility2 = null
        this.changedAbility3 = null
        this.$store.dispatch('userData')
        this.$store.commit('Change_USERCARD', res.data)
      })
      .catch((err) =>{
        console.log('결과반영 사용함수 에러', err)
      })
    },
    detailCardOff(event) {
      if (event.target.id === "dropshadow") {
        const bodyScroll = document.querySelector("body");
				bodyScroll.style.overflowY = "scroll";
				this.$store.commit('OFF_CARDDETAIL')
      }
    }
  },
  computed: {
    Card() {
      return this.$store.state.detailUsercard;
    },
    ability_grade() {
      return this.$store.state.detailUsercard?.ability_grade
    },
    ability1() {
      return this.$store.state.detailUsercard?.ability1
    },
    ability2() {
      return this.$store.state.detailUsercard?.ability2
    },
    ability3() {
      return this.$store.state.detailUsercard?.ability3
    },
    User() {
      return this.$store.state.userObject
    },
    detailCardBoxShadowStyle() {
      return this.$store.state.detailCardBoxShadowStyle
    }
  }
}
</script>

<style scoped>
.right-side {
  margin: 120px 0 auto;
}
.actor-bottom-profile {
  display: flex;
  justify-content: space-evenly;
}



.cube {
  width: 30px; 
  height: 30px;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}

.cube > div {
  margin-left: 5pxc;
}

.cube:hover {
  cursor: pointer;
  transform: scale(1.2);
  transition: all 0.5s;
}
.cube:active > img {
  transform: rotate(360deg);
  transition: all 0.5s;
}

.cube-box {
    display: flex;
    justify-content: space-evenly;
}


.hide {
	display: none;
}
.detail-flex {
	display: flex;
	justify-content: space-evenly;
}

.dropshadow {
	width: 100vw;
	height: 200%;
	background-color: rgba(0, 0, 0, 0.8);
	display: flex;
	justify-content: center;
	align-items: center;
	position: absolute;
	top: -100px;
	z-index: 10;
}

.detailbox {
	position: fixed;
	top: 20px;
	background-color: #161515;
	border-radius: 5px;
	width: 1200px;
	height: 900px;
}
.fade-detail-enter-active {
	transition: all 0.5s ease-out;
}
/* .fade-detail-leave-active {
	transition: all 0.1s ease-out;
} */

.fade-detail-enter {
	opacity: 0;
}

.fade-detail-leave-to {
	opacity: 0;
}

.actor-img {
  height: 500px;
}

.isGold {
  border: solid gold 3px;
}

.isSilver {
	border: solid rgb(130, 130, 130) 3px;
}
</style>