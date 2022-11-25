<template>
  <div>
    <h1>꼬기먹은 PinkBean 찾기</h1>
    <hr>
    <div class="myButton" @click="eatingMeat">시작!!</div>
    <p>{{`( 500 Point 필요 )` }}</p>
    <transition-group name="shuffle" tag="div">
      <!-- <div v-for="bean in beans" :key="bean">{{ bean }}</div> -->
      <img @click="selectAnswer" class="pinkbean" v-for="bean in beans" :id="`pink${bean}`" :key="bean" src="@/assets/pink.png" alt="pinkbean">
    </transition-group>
    
    <transition name="eating">
      <img 
        v-if="show"
        class="meat" 
        src="@/assets/meat.png" 
        alt="meat"
        >
    </transition>
  </div>
</template>


<script>
const API_URL = 'http://3.112.52.213'
import _ from "lodash"
import axios from 'axios'

export default {
  name: 'PinkBeanView',
  data() {
    return {
      show: true,
      answer: false,
      beans: [1, 2, 3],     
    }
  },
  computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		},    
    userObject() {
      return this.$store.state.userObject;
    }
  },
	created() { {
			if (!this.isLogin) {
				this.$router.push({ name: 'login'});
			}
		}
	},  
  methods: {
    shuffleAll() {
      const repeatCount = _.random(13, 20);
      let count = 0;
      // const bean1 = document.querySelector('#pink1');

      // const scales = ['150px', '50px', '100px'];
      let randomTime = _.random(350, 450);
      const interval = setInterval(() => {
        this.beans = _.shuffle(this.beans);
        // const scale1 = _.sample(scales);
        // bean1.style.width = `${scale1}`
        // bean1.classList.add('scale');
        count++;
        if (count >= repeatCount) {
          clearInterval(interval);
        }
      }, randomTime);
      setTimeout(() => {
        this.$swal('꼬기먹은 핑크빈 선택해주세염!');
        this.answer = true;
      }, randomTime * repeatCount + 300);
    },
    selectAnswer(event) {
      if (this.answer === false) {
        return
      } else if (this.answer === true && event.target.id === 'pink2') {
        axios({
          method: "post",
          url: `${API_URL}/accounts/change_point/`,
          data: {
            'status': 'add',
            'point': 2000,
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then(res => {
            this.$store.dispatch("userData");
            this.$swal('정답!!!', '2000Point 지급!!', 'success');
          })
          .catch(err => {
            console.log("error", err);
          });

      } else {
        axios({
          method: "post",
          url: `${API_URL}/accounts/change_point/`,
          data: {
            'status': 'delete',
            'point': 500,
          },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
          .then(res => {
            this.$store.dispatch("userData");
            this.$swal('응 걔 아냐!!', '', 'error');
          })
          .catch(err => {
            console.log("error", err);
          });        
      }
      this.answer = false;
      this.show = !this.show
      this.beans = [1, 2, 3];
    },
    eatingMeat() {
      if (this.userObject.point >= 500) {
        this.show = !this.show
        setTimeout(() => {
        this.shuffleAll()
      }, 2000);
      } else {
        this.$swal('보유하신 포인트가 부족합니다!', '한상현 국민은행 731102-.... 입급 바랍니다..', 'warning');
      }

    }
  },

}

</script>

<style scoped>
/* .start {
  cursor: pointer;
  font-family: 'maplestory';
  font-size: 1.5rem;
  border-radius: 3px;
  margin-top: 50px
} */
p {
  margin-top: 0;
  margin-bottom: 70px;
}

/* .start:hover {
  cursor: pointer;
  font-family: 'maplestory';
  color: rgb(255, 6, 89);
  transition: all 0.5s;
} */

.shuffle-move {
  transition: all 0.5s;
  transform: translateX(0px) rotate(360deg);
}

.pinkbean {
  margin: 0 20px;
  width: 120px;
  height: 120px;
}

.pinkbean-over {
  position: absolute;
  z-index: 2;
  margin: 0 20px;
  width: 120px;
  height: 120px;
}


.pinkbean:hover {
  
  cursor: pointer;
  width: 130px;
  height: 130px;
  transition: all 0.5s;
}

.meat {
  margin-top: 50px;
  width: 150px;
}

.eating-enter-active, .eating-leave-active {
  transition: all 1s;
}
.eating-leave-to {
  transform: translateY(-150px) rotate(360deg);
  opacity: 0;
}


/* .scale {
  animation: scale 0.5s;
}

@keyframes scale {
  100%{
    transform: rotateY(360deg);
  }
  } */

.bounce-enter-active, .bounce-leave-active {
  transition: all .5s;
}
.bounce-enter {
  transform: translateX(30px);
  opacity: 0;
}
.bounce-enter-to {
  transform: translateX(0px);
  opacity: 1;
}
/* .bounce-leave {
  transform: translateX(0px);
  opacity: 0;
} */
.bounce-leave-to {
  transform: translateX(30px) scale(1.5);
  opacity: 0;
}
.myButton {
	box-shadow:inset 0px 1px 0px 0px #f2d3e9;
	background-color:#ebb7d3;
	border-radius:6px;
	border:1px solid #f073d1;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:20px;
	font-weight:bold;
	padding:6px 24px;
	text-decoration:none;
	text-shadow:0px 1px 0px #f745a4;
  margin-top: 30px;
}
.myButton:hover {
	background-color:#eb5eac;
}
.myButton:active {
	position:relative;
	top:1px;
}




</style>