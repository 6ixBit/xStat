<template>
    <i-menu mode="horizontal" :theme="light" active-name="1">
        <MenuItem name="1" to="/">
            <Icon type="ios-stats" />
            xStat
        </MenuItem>

        <MenuItem name="2" to="/playercomparison">
            <Icon type="ios-people" />
            Player Comparison
        </MenuItem>

        <!-- <MenuItem name="3">
          <Icon type="ios-paper" />
              About 
        </MenuItem> -->

    </i-menu>
 
</template>

<script>
    export default {
        data () {
            return {
                theme1: 'light'
            }
        },
        mounted() {
            console.log(this.$router.currentRoute.fullPath) // Match active-name with route to get active item.
        }
    }
</script>