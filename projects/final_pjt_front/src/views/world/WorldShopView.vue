<template>
	<div>
    <WorldCardDetail />
		<div class="icon-shop">
			<div>IconShop</div>
			<PublicIconList />
		</div>
    <div class="myButton" @click="getCards">카드 뽑기</div>
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
    <div style="display: flex; justify-content: center;">
      <div>
        <div @click="buyBlackCube" class="black-cube">블랙 큐브 구매</div>
        <input type="number" @keyup.enter="buyBlackCube" v-model='buy_black' placeholder="개수 입력">
      </div>
      <div>
        <div @click="buyRedCube" class="red-cube">레드 큐브 구매</div>
        <input type="number" @keyup.enter="buyRedCube" v-model='buy_red' placeholder="개수 입력">
      </div>
    </div>
	</div>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import PublicIconList from "@/components/PublicIconList";
import WorldDeckCard from "@/components/world/profile/WorldDeckCard"
import WorldCardDetail from "@/components/world/profile/WorldCardDetail"
import _ from 'lodash'
import axios from 'axios'

export default {
	name: "WorldShopView",
	components: {
		PublicIconList,
    WorldDeckCard,
    WorldCardDetail
	},
  data() {
    return {
      // 30%(20% 10%)  35%(20% 15%)  35%(20% 15%)
      abilitylist: ['공격력+03%', '공격력+06%', '방어력+03%', '방어력+06%', '체력+03%', '체력+06%'],
      buy_black: 0,
      buy_red: 0,
      cardList: [],
      goldList: [1, 2, 3, 4, 5, 6, 7, 8]
    }
  },
	created() { {
			if (!this.isLogin) {
				this.$router.push({ name: 'login'});
			}
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
        url: `${API_URL}/accounts/make_usercards/`,
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
          this.$swal('포인트가 모자랍니다!!','','warning');
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
          url: `${API_URL}/worlds/buy_cube/`,
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
          url: `${API_URL}/worlds/buy_cube/`,
          data: {
            'num': this.buy_red,
            'cubename': 'red'
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          this.$swal(`레드큐브 ${this.buy_red}개 구매에 성공했습니다!`, '', 'success');
          this.buy_red = null
          this.$store.dispatch('userData')
          })
        .catch(() => {
          this.$swal('가지고 있는 포인트가 부족하여 구매에 실패했습니다.', '보유 포인트를 확인하고 구매해주세요!', 'success')
          this.buy_red = null
          
        })
      } else {
        this.buy_red = null
      }
    }
  },
  computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		},    
    user() {
      return this.$store.state.userObject
    }
  }
};
</script>

<style scoped>
input {
  width: 100px;
  border-radius: 5px;
}

.black-cube {
  background-image: url('@/assets/blackcube.png');
  background-repeat: no-repeat;
  background-size: contain;
  height: 30px;
  width: 170px;


}
.black-cube:hover {
  cursor: pointer;
  font-size: 17px;
  transition: all 0.3s;
  color:#000000;
  font-weight: bold;
}


.red-cube {
  background-image: url('@/assets/redcube.png');
  background-repeat: no-repeat;
  background-size: contain;
  height: 30px;
  width: 170px;
}
.red-cube:hover {
  cursor: pointer;
  font-size: 17px;
  transition: all 0.3s;
  color:#ff0189;
  font-weight: bold;
}


.icon-shop {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.icon-shop > div {
  font-size: 40px;
  font-weight: bold;
  margin-bottom: 20px;
}


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
  border-bottom: 3px white solid;
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
.myButton {
	box-shadow:inset 0px 1px 0px 0px #f2d3e9;
	background-color:#ebb7d3;
	border-radius:6px;
	border: 3px solid #f073d1;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:19px;
	font-weight:bold;
	padding:6px 24px;
	text-decoration:none;
	text-shadow:0px 0.5px 0px #ff5ab2;
}
.myButton:hover {
	background-color:#fc88c8;
}
.myButton:active {
	position:relative;
	top:1px;
}
</style>