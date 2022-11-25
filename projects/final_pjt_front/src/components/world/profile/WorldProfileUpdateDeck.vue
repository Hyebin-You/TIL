<template>
	<transition name="fade-detail" mode="out-in">
		<div
			id="dropshadow3"
			:style="{ display: detailDeckBoxShadowStyle }"
			@click="detailOff3"
			class="dropshadow3">
			<div class="detailbox3">
        <h2>{{ deckNameHangle }} 덱 구성하기</h2>
        <button @click="sendResult">구성 완료</button>
        <!-- 요안에 넣으면 댐!! -->
        <div style="display: flex; justify-content: space-evenly">
          <div style="height:300px; width:200px; position: relative">
            <p>card1</p>
            <img
              v-if="card1"
              style="right: 0px; top: 33px"
              @click='removeCard1'
              class="x-delete"
              src="@/assets/x.png"
              alt="x" />
            <img v-if="card1" :src="require(`@/assets/${card1.img_url}`)">
          </div>
          <div style="height:300px; width:200px; position: relative">
            <p>card2</p>
            <img
              v-if='card2'
              style="right: 0px; top: 33px"
              @click='removeCard2'
              class="x-delete"
              src="@/assets/x.png"
              alt="x" />
            <img v-if="card2" :src="require(`@/assets/${card2.img_url}`)">
          </div>
          <div style="height:300px; width:200px; position: relative">
            <p>card3</p>
            <img
              v-if='card3'
              style="right: 0px; top: 33px"
              @click='removeCard3'
              class="x-delete"
              src="@/assets/x.png"
              alt="x" />
            <img v-if="card3" :src="require(`@/assets/${card3.img_url}`)">
          </div>
        </div>
        <br>
        <hr>
        <div style="display:flex; flex-wrap: wrap;">
          <div v-for="card in cardList" :key="card.name" style="margin: auto">
            <div class="eventhover" @click='insertCard(card)'>
              <img :src="require(`@/assets/${card.img_url}`)" :class="{'isGold' : !card?.isnormal}" alt="card img">
              <div class="text-hidden">
                <p style="font-size: 18px">{{ card?.cardname }}</p>
                <br>
                <div :class="{ 'border-purple': card.ability_grade === '에픽',
                  'border-yellow': card.ability_grade === '유니크',
                  'border-green': card.ability_grade === '레전드리'}">
                  <span>{{ card.ability_grade }}</span>
                  <span>{{ card?.ability1 }}</span>
                  <span>{{ card?.ability2 }}</span>
                  <span>{{ card?.ability3 }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
			</div>
		</div>
	</transition>
</template>

<script>
const API_URL = 'http://3.112.52.213'
import axios from 'axios'

export default {
	name: "WorldProfileUpdateDeck",
	components: {
	},
	data() {
		return {
      card1: null,
      card2: null,
      card3: null
    };
	},
	computed: {
		detailDeckBoxShadowStyle() {
			return this.$store.state.detailDeckBoxShadowStyle;
		},
    cardList() {
      return this.$store.state.userObject.usercard_set;
    },
		deckName() {
			return this.$store.state.deckName
		},
		deckNameHangle() {
			if (this.$store.state.deckName === 'attack') {
				return '공격'
			} else {
				return '방어'
			}
		}
	},
	methods: {
		detailOff3(event) {
			if (event.target.id === "dropshadow3") {
				const bodyScroll = document.querySelector("body");
				bodyScroll.style.overflowY = "scroll";
				this.$store.commit('OFF_DECKDETAIL')
			}
		},
    insertCard(card) {
      if (this.card1 === null) {
        if (this.card2 === null || this.card2.id !== card.id) {
          if (this.card3 === null || this.card3.id !== card.id ) {
            this.card1 = card
          }
        }
      } else if (this.card2 === null) {
        if (this.card1.id !== card.id) {
          if (this.card3 === null || this.card3.id !== card.id) {
            this.card2 = card
          }
        }
      } else if (this.card3 === null) {
        if (this.card1.id !== card.id && this.card2.id !== card.id) {
          this.card3 = card
        }
      }
    },
    removeCard1() {
      this.card1 = null
    },
    removeCard2() {
      this.card2 = null
    },
    removeCard3() {
      this.card3 = null
    },
    sendResult() {
      if (this.card1 !== null && this.card2 !== null && this.card3 !== null) {
        axios({
          method: 'post',
          url: `${API_URL}/accounts/make_${this.deckName}list/`,
          data: {
            'card1': this.card1.id,
            'card2': this.card2.id,
            'card3': this.card3.id
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then(() => {
          this.$swal(`${this.deckNameHangle} 덱이 저장되었습니다!`,'', 'success')
          this.$store.dispatch('userData')
        })
      } else {
        this.$swal('카드 3장을 모두 채워야 합니다!', '', 'warning')
      }
    }
	},
};
</script>

<style scoped>
.hide {
	display: none;
}
.detail-flex3 {
	display: flex;
	justify-content: space-evenly;
}

.dropshadow3 {
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

.detailbox3 {
	position: fixed;
	top: 20px;
	background-color: #161515;
	border-radius: 5px;
	width: 1200px;
	height: 900px;
  overflow-y: scroll;
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

.eventhover {
	width: 200px;
  height: 300px;
	transform: scale(0.9);
}
.flex-box {
	display: flex;
	justify-content: center;
	align-items: center;
}

.container {
	width: 1350px;
	max-height: 350px;

}
.likelist-title {
  font-size: 25px;
} 

.marginbox {
	margin-left: 200px;
}

.eventhover:hover {
	cursor: pointer;
	transform: scale(1);
	transition: all 1s;
}

.text-hidden {
	display: flex;
  flex-direction: column;
	align-items: center;
	justify-content: center;
	width: 100%;
	height: 100%;
	opacity: 0;
	background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.9) 100%);
	/* background-color: rgba(0, 0, 0, 0.7); */
	cursor: pointer;
	position: absolute;
	top: 0%;
	left: 0%;
}

.text-hidden:hover {
	opacity: 1;
	color: white;
	transition: all 1s;
	/* background-image: brightness(0.5); */
}

.text-hidden > p {
	max-width: 150px;
	font-size: 13px;
	font-weight: 500;
	margin: 0;
	/* padding-top: 150px; */
	/* padding-top: 200px; */
	/* text-align: left; */
	word-break: break-all;
}

.text-hidden > div {
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	/* border: 4px solid purple; */
	padding: 3px 15px;
	border-radius: 5px;
}

img {
	width: 100%;
	height: 90%;
	border-radius: 5px;
}

.isGold {
  border: solid gold 3px;
}

.border-purple {
  border: solid purple 4px;
}
.border-yellow {
  border: solid yellow 4px;
}
.border-green {
  border: solid green 4px;
}
.x-delete {
	max-width: 20px;
	height: 20px;
	position: absolute;
	z-index: 100;
}
.x-delete:hover {
	cursor: pointer;
	transform: scale(1.2);
}
</style>
