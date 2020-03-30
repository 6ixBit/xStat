<template>
    <div> 
        1st Position: {{ playerInfo[0].position }} <br>
        2nd Position: {{ playerInfo[1].position }}
        <!-- Res: {{ playerInfo }} -->
        <!-- <radar-chart/> -->
    </div>
</template>

<script>
// Third party imports
// import VueApexCharts from 'vue-apexcharts'

export default {
    data() {
        return {
            series: [],
            chartOptions: {}
        }
    },
    components: {
        // 'radarChart' : VueApexCharts
    },
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
        radarChartSeries(newData, oldData) { // IF Chart data changes then render chart.
            console.log(`Radar Chart ${newData} - ${oldData}`)
        },
        selectedPlayers(newData) { 
            console.log(newData)
            
            // REQUEST current players and add them to playersInfo global
            this.$store.dispatch('getPlayers')   
            
            // Update Radar Chart on Selected players changed
            this.$store.commit('clearRadarChart')
            this.$store.commit('updateRadarChart')
        }
    }
}
</script>

