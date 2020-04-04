<template>
    <div> 
        <!-- Res: {{ playerInfo }} -->
        <!-- <radar-chart/> -->
        Length of Player Info: {{ this.playerInfo.length }}
    </div>
</template>

<script>
import axios from 'axios'
// import VueApexCharts from 'vue-apexcharts'

export default {
    data() {
        return {
            series: [],
            chartOptions: {},
            playerInfo: []
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
        }
    },
    methods: {
        async getPlayers(players){
            this.clearPlayerInfo()

            try {
               for (var player of players) {
                   const info = await axios.get(`http://localhost:8082/api/v1/players/${player}`)

                   this.playerInfo.push(info.data[0])
               }
           }  catch (error) {
               console.log(`Failed: ${error}`)
           }
        },
        async clearPlayerInfo() {
            this.playerInfo = []
        }
    },
    watch: {
        radarChartSeries(newData, oldData) { // IF Chart data changes then render chart.
            console.log(`Radar Chart ${newData} - ${oldData}`)
        },
        selectedPlayers(newData) { 

            // Add players to central repo
            this.getPlayers(newData);
            console.log(this.playerInfo.length)

            // STORE FUNCTIONALITY HERE
            //this.$store.dispatch('getPlayers')   
            // Update Radar Chart on Selected players changed
            //this.$store.commit('clearRadarChart')
            //this.$store.commit('updateRadarChart')
        }
    }
}
</script>

