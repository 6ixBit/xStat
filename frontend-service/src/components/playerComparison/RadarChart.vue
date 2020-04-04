<template>
    <div> 
        <!-- Res: {{ playerInfo }} -->
        <!-- <radar-chart type="radar" height="350" :options="chartOptions" :series="chartSeries"/> -->
        Length of Player Info: {{ this.playerInfo.length }} <br>
        Radar: {{ this.chartSeries }}

    </div>
</template>

<script>
import axios from 'axios'
// import VueApexCharts from 'vue-apexcharts'

export default {
    data() {
        return {
            chartSeries: [],
            chartOptions: {},
            playerInfo: []
        }
    },
    components: {
        // 'radarChart' : VueApexCharts
    },
    computed: {
        selectedPlayers(){
            return this.$store.state.selectedPlayers;
        }
    },
    methods: {
        async getPlayers(players){
            // Clear playerInfo to remove duplicates
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
        },
        async clearRadarChart() {
            this.chartOptions = {};
            this.chartSeries = [];
        },
        updateRadarChart() {
            // Clear Radar Chart Data
            this.clearRadarChart()

            for (var player of this.playerInfo) { // NOT WORKING 
                    let newSeries = {
                        name: `${player.player_name} - ${player.season}`,
                        data: [player.dribbleSuccess_per90, player.goals_per90, 
                                player.keyPasses_per90, player.shots_on_target_p90,
                                player.assists_per90]
                            }
                    this.chartSeries.push(newSeries)
            }
        }
    },
    watch: {
        selectedPlayers(newData) { 
            // Add players to central repo
            this.getPlayers(newData)
            .then( () => { this.updateRadarChart() }) // Update Charts.

        }
    }
}
</script>

