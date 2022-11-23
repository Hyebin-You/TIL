<template>
	<div>
		WorldShopView
		<PublicIconList />
		<WorldShopCube />
    <button @click="getCards">카드 뽑기</button>
      <div class="item-size-box">
        <WorldDeckCard
          v-for="card in cardList"
          :key='card.id'
          :card='card'
          class='eventhover'
        />
      </div>
    <br>
    <!-- <img v-for="(card, index) in cardList" :key='index' :src="require(`@/assets/actors/${card.img_url}`)"> -->
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
import WorldDeckCard from "@/components/world/profile/WorldDeckCard"
import _ from 'lodash'
import axios from 'axios'

export default {
	name: "WorldShopView",
	components: {
		PublicIconList,
		WorldShopCube,
    WorldDeckCard
	},
  data() {
    return {
      // 30%(20% 10%)  35%(20% 15%)  35%(20% 15%)
      abilitylist: ['공격력+03%', '공격력+06%', '방어력+03%', '방어력+06%', '체력+03%', '체력+06%'],
      buy_black: null,
      buy_red: null,
      cardList: [],
      goldList: [1, 2, 3, 4, 5, 6, 7, 8]
    }
  },
  methods: {
		enter(el) {
			el.style.transitionDelay = 200 + "ms";
		},
		afterEnter(el) {
			el.style.transitionDelay = "";
		},
    sleep(ms) {
      const wakeUpTime = Date.now() + ms;
      while (Date.now() < wakeUpTime) {
        console.log()
      }
    },
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
    getCard() {
      const ability1 = this.getability()
      const ability2 = this.getability()
      const ability3 = this.getability()
      let card_pk
      if (_.random(1, 100) <= 10) {
        const a = _.random(1, 100)
        if (a >= 3 && a < 13) {
          card_pk = 9
        } else {
          card_pk = _.sample(this.goldList)
        }
      } else {
        card_pk = _.random(10, 54)
      }

      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/make_usercards/',
        data: {'card_pk': card_pk, 'ability1': ability1, 'ability2': ability2, 'ability3': ability3},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.cardList.push(res.data)
      })
    }
    ,
    getCards() {
      const result = confirm(`카드 5장을 뽑으시겠습니까? 2000포인트가 소모됩니다.
      보유 포인트 : ${this.user.point}`)
      if (result) {
        if (this.user.point < 2000) {
          alert('포인트가 모자랍니다!!!')
          return
        }
      } else {
        return
      }
      this.cardList = []
      this.getCard()
      this.sleep(100)
      this.getCard()
      this.sleep(100)
      this.getCard()
      this.sleep(100)
      this.getCard()
      this.sleep(100)
      this.getCard()
      this.sleep(500)
      this.$store.dispatch('userData')
    },
    buyBlackCube() {
      const result = confirm(`블랙큐브를 ${this.buy_black}개 구매하시겠습니까?
      총 가격 : ${this.buy_black * 100}
      보유 포인트 : ${this.user.point}`)
      if (result) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/worlds/buy_cube/',
          data: {
            'num': this.buy_black,
            'cubename': 'black'
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          this.$swal(`블랙큐브 ${this.buy_black}개`,'구매에 성공했습니다!', 'success');
          this.buy_black = null
          this.$store.dispatch('userData')
          })
        .catch(() => {
          this.$swal('구매 실패!!', '보유 포인트를 확인하고 구매해주세요', 'warning');
          this.buy_black = null
        })
      } else {
        this.buy_black = null
      }
    },
    buyRedCube() {
      const result = confirm(`레드큐브를 ${this.buy_red}개 구매하시겠습니까?
      총 가격 : ${this.buy_red * 50}
      보유 포인트 : ${this.user.point}`)
      if (result) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/worlds/buy_cube/',
          data: {
            'num': this.buy_red,
            'cubename': 'red'
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          alert(`레드큐브 ${this.buy_red}개 구매에 성공했습니다!`);
          this.buy_red = null
          this.$store.dispatch('userData')
          })
        .catch(() => {
          alert('가지고 있는 포인트가 부족하여 구매에 실패했습니다. 보유 포인트를 확인하고 구매해주세요!')
          this.buy_red = null
          
        })
      } else {
        this.buy_red = null
      }
    }
  },
  computed: {
    user() {
      return this.$store.state.userObject
    }
  }
};
</script>

<style scoped>
.img-sizing {
  height: 300px;
}
.item-size-box {
  width: 100%;
  display: flex;
  justify-content: center;
  position: relative;

}
.eventhover {
	width: 140px;
	transform: scale(0.9);
}

.eventhover:hover {
	cursor: pointer;
	transform: scale(1.05);
	transition: all 1s;
  z-index: 100;
}
.icons {
	display: flex;
	width: 900px;
	flex-wrap: wrap;
	align-items: center;

}
.iconlist-flex {
  display: flex;
  justify-content: center;
}

.fade-move-enter-active {
	transition: all 0.5s ease-out;
}
.fade-move-enter {
	transform: translateX(50px);
	opacity: 0;
}
.fade-move-leave {
	opacity: 0;
}

</style>