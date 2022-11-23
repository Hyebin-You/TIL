<template>
	<div>
		<h1>MovieShop</h1>
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
};
</script>


<style scoped>
.icon-shop {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.icon-shop > div {
  font-size: 20px;
  font-weight: bold;
}

</style>
