<template>
	<div>
		<h1>WorldFight</h1>
    <div id='game' style="border: solid black 1px">
      <button id='randommatch' @click='getEnermy'>랜덤 매칭</button>
      <button id='1round' style="display: none" @click='startFirstRound'>1라운드 시작</button>
      <button id='2round' style="display: none" @click='startSecondRound'>2라운드 시작</button>
      <button id='3round' style="display: none" @click='startThirdRound'>3라운드 시작</button>
      <p>{{ round_num }}</p>
      <p>게임 진행 상황</p>
      <p>{{ my_win_point }} : {{ enermy_win_point }}</p>
      <p v-for='(st, index) in gamestatus_content' :key='index'>{{ st }}</p>
      <div id='ask' style="display:none">
        <p>{{ ask }}</p>
        <span style="margin-right: 3px" @click='openThirdButton'>예</span>
        <span style="margin-left: 3px" @click='sendResult'>대전 종료</span>
      </div>
      <p>{{ battle_result }}</p>
      <button id='endgame' style="display: none" @click='sendResult'>대전 종료</button>
    </div>
		<WorldDeckCard/>
	</div>
</template>

<script>
import WorldDeckCard from '@/components/world/profile/WorldDeckCard'
import _ from 'lodash'
import axios from 'axios'

export default {
	name: "WorldFightView",
	components: {
		WorldDeckCard,
	},
  data() {
    return {
      enermy_exist: false,
      roundnum: '대전 시작 전',
      gamestatus: [],
      my_nickname: null,
      my_card1: null,
      my_card2: null,
      my_card3: null,
      enermy_nickname: null,
      enermy_id: null,
      enermy_card1: null,
      enermy_card2: null,
      enermy_card3: null,
      my_win_num: 0,
      enermy_win_num: 0,
      endgame: false,
      win_user: null,
      battle_result: null,
      ask: null,
      final_result: null,
    }
  },
  methods: {
    sleep(ms) {
      const wakeUpTime = Date.now() + ms;
      while (Date.now() < wakeUpTime) {
        console.log()
      }
    },
    FirstAttack() {
      const m_a = _.random(this.my_card1.final_attack - 20, this.my_card1.final_attack + 20)
      const m_a_l = _.round(m_a - m_a * this.enermy_card1.final_defense / 100)
      let my_critical = false
      if (_.random(1, 10) === 3 || _.random(1, 10) === 5 || _.random(1, 10) === 7) {
        my_critical = true
      }

      let status = ''
      if (my_critical) {
        if (m_a_l * 2 < this.enermy_card1.final_life) {
          this.enermy_card1.final_life -= m_a_l * 2
          status += `크리티컬 적중!.상대방의 카드가 ${m_a_l * 2}만큼의 데미지를 입었습니다.남은 체력은 ${this.enermy_card1.final_life}입니다.`
        } else {
          this.win_user = 'me'
          this.endgame = true
          status += `크리티컬 적중!.상대방의 카드가 ${m_a_l * 2}만큼의 데미지를 입었습니다.상대방의 카드에 남은 체력이 없습니다.당신의 승리입니다.`
          return status
        }
      } else {
        if (m_a_l < this.enermy_card1.final_life) {
          this.enermy_card1.final_life -= m_a_l
          status += `상대방의 카드가 ${m_a_l}만큼의 데미지를 입었습니다.남은 체력은 ${this.enermy_card1.final_life}입니다.`
        } else {
          this.win_user = 'me'
          this.endgame = true
          status += `상대방의 카드가 ${m_a_l}만큼의 데미지를 입었습니다.상대방의 카드에 남은 체력이 없습니다.당신의 승리입니다.`
          return status
        }
      }

      const e_a = _.random(this.enermy_card1.final_attack - 20, this.enermy_card1.final_attack + 20)
      const e_a_l = _.round(e_a - e_a * this.my_card1.final_defense / 100)
      let enermy_critical = false
      if (_.random(1, 10) === 3 || _.random(1, 10) === 5 || _.random(1, 10) === 7) {
        enermy_critical = true
      }

      if (enermy_critical) {
        if (e_a_l * 2 < this.my_card1.final_life) {
          this.my_card1.final_life -= e_a_l * 2
          status += `크리티컬 적중!.나의 카드가 ${e_a_l * 2}만큼의 데미지를 입었습니다.남은 체력은 ${this.my_card1.final_life}입니다.`
          return status
        } else {
          this.win_user = 'enermy'
          this.endgame = true
          status += `크리티컬 적중!.나의 카드가 ${e_a_l*2}만큼의 데미지를 입었습니다.나의 카드에 남은 체력이 없습니다.상대방의 승리입니다.`
          return status
        }
      } else {
        if (e_a_l < this.my_card1.final_life) {
          this.my_card1.final_life -= e_a_l
          status += `나의 카드가 ${e_a_l}만큼의 데미지를 입었습니다.남은 체력은 ${this.my_card1.final_life}입니다.`
          return status
        } else {
          this.win_user = 'enermy'
          this.endgame = true
          status += `나의 카드가 ${e_a_l}만큼의 데미지를 입었습니다.나의 카드에 남은 체력이 없습니다.상대방의 승리입니다.`
          return status
        }
      }
    },
    SecondAttack() {
      const m_a = _.random(this.my_card2.final_attack - 20, this.my_card2.final_attack + 20)
      const m_a_l = _.round(m_a - m_a * this.enermy_card2.final_defense / 100)
      let my_critical = false
      if (_.random(1, 10) === 3 || _.random(1, 10) === 5 || _.random(1, 10) === 7) {
        my_critical = true
      }

      let status = ''
      if (my_critical) {
        if (m_a_l * 2 < this.enermy_card2.final_life) {
          this.enermy_card2.final_life -= m_a_l * 2
          status += `크리티컬 적중!.상대방의 카드가 ${m_a_l * 2}만큼의 데미지를 입었습니다.남은 체력은 ${this.enermy_card2.final_life}입니다.`
        } else {
          this.win_user = 'me'
          this.endgame = true
          status += `크리티컬 적중!.상대방의 카드가 ${m_a_l * 2}만큼의 데미지를 입었습니다.상대방의 카드에 남은 체력이 없습니다.당신의 승리입니다.`
          return status
        }
      } else {
        if (m_a_l < this.enermy_card2.final_life) {
          this.enermy_card2.final_life -= m_a_l
          status += `상대방의 카드가 ${m_a_l}만큼의 데미지를 입었습니다.남은 체력은 ${this.enermy_card2.final_life}입니다.`
        } else {
          this.win_user = 'me'
          this.endgame = true
          status += `상대방의 카드가 ${m_a_l}만큼의 데미지를 입었습니다.상대방의 카드에 남은 체력이 없습니다.당신의 승리입니다.`
          return status
        }
      }

      const e_a = _.random(this.enermy_card2.final_attack - 20, this.enermy_card2.final_attack + 20)
      const e_a_l = _.round(e_a - e_a * this.my_card2.final_defense / 100)
      let enermy_critical = false
      if (_.random(1, 10) === 3 || _.random(1, 10) === 5 || _.random(1, 10) === 7) {
        enermy_critical = true
      }

      if (enermy_critical) {
        if (e_a_l * 2 < this.my_card2.final_life) {
          this.my_card2.final_life -= e_a_l * 2
          status += `크리티컬 적중!.나의 카드가 ${e_a_l * 2}만큼의 데미지를 입었습니다.남은 체력은 ${this.my_card2.final_life}입니다.`
          return status
        } else {
          this.win_user = 'enermy'
          this.endgame = true
          status += `크리티컬 적중!.나의 카드가 ${e_a_l*2}만큼의 데미지를 입었습니다.나의 카드에 남은 체력이 없습니다.상대방의 승리입니다.`
          return status
        }
      } else {
        if (e_a_l < this.my_card2.final_life) {
          this.my_card2.final_life -= e_a_l
          status += `나의 카드가 ${e_a_l}만큼의 데미지를 입었습니다.남은 체력은 ${this.my_card2.final_life}입니다.`
          return status
        } else {
          this.win_user = 'enermy'
          this.endgame = true
          status += `나의 카드가 ${e_a_l}만큼의 데미지를 입었습니다.나의 카드에 남은 체력이 없습니다.상대방의 승리입니다.`
          return status
        }
      }
    },
    ThirdAttack() {
      const m_a = _.random(this.my_card3.final_attack - 20, this.my_card3.final_attack + 20)
      const m_a_l = _.round(m_a - m_a * this.enermy_card3.final_defense / 100)
      let my_critical = false
      if (_.random(1, 10) === 3 || _.random(1, 10) === 5 || _.random(1, 10) === 7) {
        my_critical = true
      }

      let status = ''
      if (my_critical) {
        if (m_a_l * 2 < this.enermy_card3.final_life) {
          this.enermy_card3.final_life -= m_a_l * 2
          status += `크리티컬 적중!.상대방의 카드가 ${m_a_l * 2}만큼의 데미지를 입었습니다.남은 체력은 ${this.enermy_card3.final_life}입니다.`
        } else {
          this.win_user = 'me'
          this.endgame = true
          status += `크리티컬 적중!.상대방의 카드가 ${m_a_l * 2}만큼의 데미지를 입었습니다.상대방의 카드에 남은 체력이 없습니다.당신의 승리입니다.`
          return status
        }
      } else {
        if (m_a_l < this.enermy_card3.final_life) {
          this.enermy_card3.final_life -= m_a_l
          status += `상대방의 카드가 ${m_a_l}만큼의 데미지를 입었습니다.남은 체력은 ${this.enermy_card3.final_life}입니다.`
        } else {
          this.win_user = 'me'
          this.endgame = true
          status += `상대방의 카드가 ${m_a_l}만큼의 데미지를 입었습니다.상대방의 카드에 남은 체력이 없습니다.당신의 승리입니다.`
          return status
        }
      }

      const e_a = _.random(this.enermy_card3.final_attack - 20, this.enermy_card3.final_attack + 20)
      const e_a_l = _.round(e_a - e_a * this.my_card3.final_defense / 100)
      let enermy_critical = false
      if (_.random(1, 10) === 3 || _.random(1, 10) === 5 || _.random(1, 10) === 7) {
        enermy_critical = true
      }

      if (enermy_critical) {
        if (e_a_l * 2 < this.my_card3.final_life) {
          this.my_card3.final_life -= e_a_l * 2
          status += `크리티컬 적중!.나의 카드가 ${e_a_l * 2}만큼의 데미지를 입었습니다.남은 체력은 ${this.my_card3.final_life}입니다.`
          return status
        } else {
          this.win_user = 'enermy'
          this.endgame = true
          status += `크리티컬 적중!.나의 카드가 ${e_a_l*2}만큼의 데미지를 입었습니다.나의 카드에 남은 체력이 없습니다.상대방의 승리입니다.`
          return status
        }
      } else {
        if (e_a_l < this.my_card3.final_life) {
          this.my_card3.final_life -= e_a_l
          status += `나의 카드가 ${e_a_l}만큼의 데미지를 입었습니다.남은 체력은 ${this.my_card3.final_life}입니다.`
          return status
        } else {
          this.win_user = 'enermy'
          this.endgame = true
          status += `나의 카드가 ${e_a_l}만큼의 데미지를 입었습니다.나의 카드에 남은 체력이 없습니다.상대방의 승리입니다.`
          return status
        }
      }
    },
    startFirstRound() {
      const but = document.getElementById('1round')
      but.style.display = 'none'
      this.roundnum = '1 라운드'
      this.loading = setInterval(this.FirstRound, 1500)
    },
    async FirstRound() {
      let tt = await this.FirstAttack()
      this.gamestatus = tt
      if (this.endgame) {
        if (this.win_user === 'me') {
          this.my_win_num += 1
        } else {
          this.enermy_win_num += 1
        }
        this.win_user = null
        this.endgame = false
        const but2 = document.getElementById('2round')
        but2.style.display = 'inline'
        clearInterval(this.loading)
      }
    },
    startSecondRound() {
      const but2 = document.getElementById('2round')
      but2.style.display = 'none'
      this.roundnum = '2 라운드'
      this.loading = setInterval(this.SecondRound, 1500)
    },
    async SecondRound() {
      let tt = await this.SecondAttack()
      this.gamestatus = tt
      if (this.endgame) {
        if (this.win_user === 'me') {
          this.my_win_num += 1
        } else {
          this.enermy_win_num += 1
        }
        this.win_user = null
        this.endgame = false
        if (this.my_win_num === 2) {
          this.ask = '2판의 승리로 당신이 최종 승리했습니다. 3라운드도 진행하시겠습니까?'
          const divAsk = document.getElementById('ask')
          this.final_result = '승'
          divAsk.style.display = 'block'
        } else if (this.enermy_win_num === 2) {
          this.ask = '2판의 패배로 당신이 최종 패배했습니다. 3라운드도 진행하시겠습니까?'
          const divAsk = document.getElementById('ask')
          this.final_result = '패'
          divAsk.style.display = 'block'
        } else {
          const but3 = document.getElementById('3round')
          but3.style.display = 'inline'
        }
        clearInterval(this.loading)
      }
    },
    startThirdRound() {
      const but3 = document.getElementById('3round')
      but3.style.display = 'none'
      this.roundnum = '3 라운드'
      this.loading = setInterval(this.ThirdRound, 1500)
    },
    async ThirdRound() {
      let tt = await this.ThirdAttack()
      this.gamestatus = tt
      if (this.endgame) {
        if (this.win_user === 'me') {
          this.my_win_num += 1
        } else {
          this.enermy_win_num += 1
        }
        this.win_user = null
        this.endgame = false
        clearInterval(this.loading)
        if (this.my_win_num >= 2) {
          this.battle_result = `${this.my_win_num} : ${this.enermy_win_num} 으로 당신의 최종 승리입니다!`
          this.final_result = '승'
        } else {
          this.battle_result = `${this.my_win_num} : ${this.enermy_win_num} 으로 당신의 최종 패배입니다!`
          this.final_result = '패'
        }
        const endbutton = document.getElementById('endgame')
        endbutton.style.display = 'inline'
      }
    },
    openThirdButton() {
      const but3 = document.getElementById('3round')
      but3.style.display = 'inline'
      const divAsk = document.getElementById('ask')
      divAsk.style.display = 'none'
    },
    sendResult() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/worlds/make_battlelog/',
        data: {
          'enermy_id': this.enermy_id,
          'log': this.final_result
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$router.go()
      })
    },
    getEnermy() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/worlds/get_enermy_status/',
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        this.enermy_nickname = res.data.enermy_nickname
        this.enermy_card1 = res.data.card1
        this.enermy_card2 = res.data.card2
        this.enermy_card3 = res.data.card3
        this.enermy_id = res.data.enermy_id
        
        const button = document.getElementById('randommatch')
        button.style.display = 'none'
        this.gamestatus = '대전을 시작합니다. 버튼을 눌러 라운드를 실행하세요.'
        const but = document.getElementById('1round')
        but.style.display = 'inline'
      })
    }
  },
  created() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/worlds/get_my_status/',
      headers: {
        Authorization: `Token ${this.$store.state.token}`
      }
    })
    .then((res) => {
      this.my_nickname = res.data.my_nickname
      this.my_card1 = res.data.card1
      this.my_card2 = res.data.card2
      this.my_card3 = res.data.card3
    })
  },
  computed: {
    gamestatus_content() {
      return _.split(this.gamestatus, '.')
    },
    my_win_point() {
      return this.my_win_num
    },
    enermy_win_point() {
      return this.enermy_win_num
    },
    round_num () {
      return this.roundnum
    },
    user_tier () {
      return this.$store.state.userObject.tier
    }
  },
  watch: {
    user_tier: function(val, oldval) {
      alert(`티어가 ${oldval}에서 ${val}로 바뀌었습니다!`)
    }
  }
};
</script>

<style></style>
