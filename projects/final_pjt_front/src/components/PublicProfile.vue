<template>
	<div class="profile-whole">
		PublicProfile
		<div class="profile-info">
			<div class="profile-img">
				<img src="@/assets/pink.png" alt="" />
			</div>
			<div class="info-list">
				<div>닉네임 : {{ userObject.nickname }}</div>
				<div>티어 :{{ userObject.tier }}</div>
				<div>포인트 : {{ userObject.point }}</div>
				<div>승점 : {{ userObject.win_point }}</div>
			</div>
			<div class="info-deck">
				<div>{{ userObject.attacklist_set[0] }}</div>
				<div>{{ userObject.defenselist_set[0] }}</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "PublicProfile",
	computed: {
		userObject() {
			return this.$store.state.userObject;
		}
	}
};
</script>

<style scoped>
.profile-whole {
	border: 1px solid skyblue;
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
	height: 150px;
	display: flex;
}
.info-list {
	display: flex;
	flex-direction: column;
  justify-content: space-evenly;
  width: 200px;
}
.info-deck {
	display: flex;

}

</style>
