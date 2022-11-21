<template>
	<div>
		WorldShopView
		<PublicIconList />
		<WorldShopCube />
    <button @click="getCards">카드 뽑기</button>
    <br>
    <img v-for="(card, index) in cardList" :key='index' :src="`/assets/actors/${card.img_url}`">
    <br>
    <p>블랙 큐브를 몇 개 구매하시겠습니까</p>
    <input type="number" @keyup.enter="buyBlackCube" v-model='buy_black' placeholder="개수를 입력 후 엔터치기">
    <br>
    <br>
    <p>레드 큐브를 몇 개 구매하시겠습니까</p>
    <input type="number" @keyup.enter="buyRedCube" v-model='buy_red' placeholder="개수를 입력 후 엔터치기">
	</div>
</template>

<script>
import PublicIconList from "@/components/PublicIconList";
import WorldShopCube from "@/components/world/shop/WorldShopCube";
import _ from 'lodash'
import axios from 'axios'

export default {
	name: "WorldShopView",
	components: {
		PublicIconList,
		WorldShopCube,
	},
  data() {
    return {
      // 30%(20% 10%)  35%(20% 15%)  35%(20% 15%)
      abilitylist: ['공격력+03%', '공격력+06%', '방어력+03%', '방어력+06%', '체력+03%', '체력+06%'],
      buy_black: null,
      buy_red: null,
      cardList: [],
    }
  },
  methods: {
    getability() {
      const num = _.random(1, 100)
      if (1 <= num && num < 21) {
        return this.abilitylist[0]
      } else if (21 <= num && num < 31) {
        return this.abilitylist[1]
      } else if (31 <= num && num < 51) {
        return this.abilitylist[2]
      } else if (51 <= num && num < 66) {
        return this.abilitylist[3]
      } else if (66 <= num && num < 87) {
        return this.abilitylist[4]
      } else {
        return this.abilitylist[5]
      }
    },
    getCard(card_pk) {
      const ability1 = this.getability()
      const ability2 = this.getability()
      const ability3 = this.getability()
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/make_usercards/',
        data: {'card_pk': card_pk, 'ability1': ability1, 'ability2': ability2, 'ability3': ability3},
        headers: {
          Authorization: 'Token ee6fb03fa4fe171dd3d989a63bb8561d1e3259c1'
        }
      })
      .then((res) => {
        console.log('생성')
        console.log(res.data)
        this.cardList.push(res.data)
      })
    }
    ,
    getCards() {
      this.getCard(3)
      // this.getCard(_.random(1, 25))
      // this.getCard(_.random(1, 25))
      // this.getCard(_.random(1, 25))
      // this.getCard(_.random(1, 25))
    },
    buyBlackCube() {
      const result = confirm(`블랙큐브를 ${this.buy_black}개 구매하시겠습니까?`)
      if (result) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/worlds/buy_cube/',
          data: {
            'num': this.buy_black,
            'cubename': 'black'
          },
          headers: {
            Authorization: 'Token 05bf7dab4d5be465453cc9807bb047ed9cc89953'
          }
        })
        .then(() => {
          alert(`블랙큐브 ${this.buy_black}개 구매에 성공했습니다!`);
          this.buy_black = null
          })
        .catch(() => {
          alert('가지고 있는 포인트가 부족하여 구매에 실패했습니다. 보유 포인트를 확인하고 구매해주세요!')
          this.buy_black = null
        })
      } else {
        this.buy_black = null
      }
    },
    buyRedCube() {
      const result = confirm(`레드큐브를 ${this.buy_red}개 구매하시겠습니까?`)
      if (result) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/worlds/buy_cube/',
          data: {
            'num': this.buy_red,
            'cubename': 'red'
          },
          headers: {
            Authorization: 'Token 05bf7dab4d5be465453cc9807bb047ed9cc89953'
          }
        })
        .then(() => {
          alert(`레드큐브 ${this.buy_red}개 구매에 성공했습니다!`);
          this.buy_red = null
          })
        .catch(() => {
          alert('가지고 있는 포인트가 부족하여 구매에 실패했습니다. 보유 포인트를 확인하고 구매해주세요!')
          this.buy_red = null
        })
      } else {
        this.buy_red = null
      }
    }
  }
};
</script>

<style></style>
