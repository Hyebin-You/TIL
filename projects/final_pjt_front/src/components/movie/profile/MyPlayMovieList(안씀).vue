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