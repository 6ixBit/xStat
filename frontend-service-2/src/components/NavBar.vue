<template>
    <i-menu mode="horizontal" :theme="light" :active-name='activeMenuItem'>
        <MenuItem name="1" to="/">
            <Icon type="ios-stats" />
            xStat
        </MenuItem>

        <MenuItem name="2" to="/playercomparison">
            <Icon type="ios-people" />
            Player Comparison
        </MenuItem>

    </i-menu>
 
</template>

<script>
    export default {
        data () {
            return {
                currentRoute: this.$router.currentRoute.fullPath,
                activeMenuItem: "1"
            }
        },
        mounted() {
            if(this.currentRoute === "/playercomparison") {
                this.activeMenuItem = "2"
            }

        }
    }
</script>