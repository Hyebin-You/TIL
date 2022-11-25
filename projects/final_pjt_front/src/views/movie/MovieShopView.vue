<template>
	<div>
		<div class="icon-shop">
			<div>IconShop</div>
			<PublicIconList />
		</div>
	</div>
</template>

<script>
import PublicIconList from "@/components/PublicIconList";

export default {
	name: "MovieShop",
	components: {
		PublicIconList,
	},
	computed: {
		isLogin() {
			return this.$store.getters.isLogin;
		},
	},
	created() { {
			if (!this.isLogin) {
				this.$router.push({ name: 'login'});
			}
		}
	},	
};
</script>


<style scoped>
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

</style>
