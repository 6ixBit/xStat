<template>
    <div id="chart">
        <scatter type="scatter" width="100%" height="350" :options="chartOptions" :series="series"/>
    </div>
</template>

<script>
// Third party imports
import VueApexCharts from 'vue-apexcharts'
import axios from 'axios'

export default {
    components: {
        "scatter": VueApexCharts
    },
    props : ['league'],
    data() {
        return {
            series: [],
            chartOptions: {}    
        }
    },
    async created(){
        try {
            // Make request to general micro service to fetch goals stats on load of page.
            const res = await axios.get(`http://localhost:8081/api/v1/stats/passes/${this.league}`)

            var playerData = [] 
            
            // REMOVE ONCE DONE, VALUE IS STATIC ON LOAD.
            var playerName = []

            // Extract data from response 
            res.data.forEach(player => {
              let temp_player_data = []
              
              // Add specific player info to array
              temp_player_data.push(player.assists)
              temp_player_data.push(player.minutes_played)
              playerName.push(player.player_name)

              playerData.push(temp_player_data)
            })

            this.series = [{
              name: `${res.data[0].competition} players`,
              data: playerData
            }]

            this.chartOptions = {
            chart: {
              height: 350,
              type: 'scatter',
              zoom: {
                enabled: true,
                type: 'xy'
              }
            },
            title: {
              text: `🎯 Assists vs Minutes Played: ${res.data[0].competition} (${res.data[0].season})`,
              align: 'left'
            },
            xaxis: {
              tickAmount: 10,
              title : {
                text: "🎯 Assists",
              },
              labels: {
                formatter: function(val) {
                  return parseInt(val).toFixed(1)
                }
              }
            },
            yaxis: {
              tickAmount: 7,
              title : {
                text: "Minutes played"
              }
            },
            tooltip: {
              x: {
                formatter: function(value) {
                  return "Goals:  " + playerName + '' + value;
                }
              }
            }
          }            
        } catch (e) {
            // TODO: On data failing to load display an error to user.
            console.log(e)
        }
    },
    watch: {
      league: async function (newVal) { // Watch for league prop being changed.
        const newResult = await axios.get(`http://localhost:8081/api/v1/stats/goals/${newVal}`)

        var finalPlayerData = []

        // Loop over result and add data to chart.
        newResult.data.forEach(player => {
          let playerData = []

          playerData.push(player.goals) // Push results to array
          playerData.push(player.minutes_played)

          finalPlayerData.push(playerData)
        });

        // Update chart when select option is changed.
        this.series = [{
          name: `${newResult.data[0].competition} players`,
          data: finalPlayerData
        }]

        this.chartOptions = {
            chart: {
              height: 350,
              type: 'scatter',
              zoom: {
                enabled: true,
                type: 'xy'
              }
            },
            title: { 
              text: `🎯 Assists vs Minutes Played: ${newResult.data[0].competition} (${newResult.data[0].season})`,
              align: 'left'
            },
            xaxis: {
              tickAmount: 10,
              title : {
                text: " 🎯 Assists"
              },
              labels: {
                formatter: function(val) {
                  return parseInt(val).toFixed(1)
                }
              }
            },
            yaxis: {
              tickAmount: 7,
              title : {
                text: "Minutes played"
              }
            }
          }

      }
    }

}
</script>