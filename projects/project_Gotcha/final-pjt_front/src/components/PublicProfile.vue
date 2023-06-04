<template>
	<div class="profile-whole">
		<div class="profile-info">
			<div class="profile-img">
				<img :src="require(`@/assets/${userObject.user_icon}`)" alt="" />
			</div>
			<div class="info-list">
				<div>닉네임&nbsp;: &nbsp;{{ userObject.nickname }}</div>
				<div>티어&nbsp;: &nbsp;{{ userObject.tier }}</div>
				<div>포인트&nbsp;: &nbsp;{{ userObject.point }}</div>
				<div>승점&nbsp;: &nbsp;{{ userObject.win_point }}</div>
			</div>
			<div class="info-deck">
				<WorldDeck
					deck-name='Attack List'
					:deck-list='userObject.attacklist_set[0]'
				/>
				<WorldDeck
					deck-name='Defense List'
					:deck-list='userObject.defenselist_set[0]'
				/>
			</div>
		</div>
	</div>
</template>

<script>
import WorldDeck from '@/components/world/profile/WorldDeck'


export default {
	name: "PublicProfile",
	components: {
		WorldDeck,
	},
	computed: {
		userObject() {
			return this.$store.state.userObject;
		}
	}
};
</script>

<style scoped>
.profile-whole {
	margin: auto;
	width: 80%;
	height: 100%;
}
.profile-img {
  width: 150px;
	height: 150px;
}
.profile-img > img {
  width: 100%;
  height: 100%;
}

.profile-info {
	width: 100%;
	height: 100%;
	display: flex;
	align-items: center;
}
.info-list {
	font-size: 22px;
	display: flex;
	flex-direction: column;
  justify-content: space-evenly;
	align-items: flex-start;
	padding-left: 20px;
  width: 200px;
}
.info-deck {
	display: flex;

}

</style>
