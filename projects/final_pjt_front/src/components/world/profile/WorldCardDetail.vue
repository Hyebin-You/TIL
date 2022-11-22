<template>
<div>
  <h1>CardDetail</h1>
    <img :src="require(`@/assets/${Card?.img_url}`)" alt="없넹...">
    <p>{{ Card?.cardname }}</p>
    <p>기본 공격력 : {{ Card?.attack }}</p>
    <p>기본 방어력 : {{ Card?.defense }}</p>
    <p>기본 체력 : {{ Card?.life }}</p>
    <p>보유 블랙 큐브 : {{ User.blackcube }}개</p>
    <p>보유 레드 큐브 : {{ User.redcube }}개</p>
    <button @click='useBlack'>블랙 큐브 사용하기</button>
    <button @click='useRed'>레드 큐브 사용하기</button>
    <p>잠재능력 등급 : {{ ability_grade }}</p>
    <p>ability1 : {{ ability1 }}</p>
    <p>ability2 : {{ ability2 }}</p>
    <p>ability3 : {{ ability3 }}</p>
    <hr>
    <p>큐브를 돌린 결과</p>
    <p>잠재능력 등급 : {{ changedAbilityGrade }}</p>
    <p>ability1 : {{ changedAbility1 }}</p>
    <p>ability2 : {{ changedAbility2 }}</p>
    <p>ability3 : {{ changedAbility3 }}</p>
    <button @click='sendResult'>해당 결과를 적용하시겠습니까?</button>
  </div>
</template>

<script>
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
        alert('큐브가 없습니다!!')
        return
      }

      if (this.ability_grade === 'epic') {
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
        url: 'http://127.0.0.1:8000/accounts/use_cube/',
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
        alert('큐브가 없습니다!!')
        return
      }

      if (this.ability_grade === 'epic') {
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
        url: 'http://127.0.0.1:8000/accounts/use_cube/',
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
        url: 'http://127.0.0.1:8000/accounts/modify_card/',
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
        this.$store.dispatch('userData')
      })
      .catch((err) =>{
        console.log('결과반영 사용함수 에러', err)
      })
    },
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
  }
}
</script>

<style scoped>

</style>