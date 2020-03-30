<template>
    <div> 
        {{ radarChartSeries }}
        Here: {{ playerInfo }}
    </div>
</template>

<script>
// Third party imports
// import VueApexCharts from 'vue-apexcharts'

export default {
    computed: {
        radarChartSeries(){
            return this.$store.state.radarChartSeries;
        },
        selectedPlayers(){
            return this.$store.state.selectedPlayers;
        },
        playerInfo(){
            return this.$store.state.playerInfo;
        }
    },
    watch: {
        radarChartSeries(newData) { // IF Chart data changes then render chart.
            console.log(newData)
        },
        selectedPlayers() {  
            // REQUEST current players and add them to playersInfo global
            this.$store.dispatch('getPlayers')          
        }
    }
}
</script>