<template>
	<div>
		WorldShopView
		<PublicIconList />
		<WorldShopCube />
    <button @click="getCards">카드 뽑기</button>
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
      abilitylist: ['공격력+03%', '공격력+06%', '방어력+03%', '방어력+06%', '체력+03%', '체력+06%']
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
          Authorization: 'Token 1bda32d8178c9c2f668d1facb42781b74fca2217'
        }
      })
      .then(() => {
        console.log('생성')
      })
    }
    ,
    getCards() {
      this.getCard(2)
      this.getCard(3)
      this.getCard(4)
      this.getCard(5)
    }
  }
};
</script>

<style></style>
