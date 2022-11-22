<template>
	<div class="profile-whole">
		PublicProfile
		<div class="profile-info">
			<div class="profile-img">
				<img src="@/assets/people.png" alt="" />
			</div>
			<div class="info-list">
				<div>여기는 아이디</div>
				<div>여기는 티어</div>
				<div>여기는 포인트</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "PublicProfile",
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
</style>
