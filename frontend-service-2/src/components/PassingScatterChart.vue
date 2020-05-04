<template>
  <div class="container">
      <scatter v-if="loaded" :chart-data="chartdata" :options="options" height="180"
       />
  </div>
</template>

<script>
import axios from "axios"
import Scatter from "./Charts/ScattChart"

export default {
  name: "PassingChartContainer",
  props : ['league'],
  components: {
    "scatter": Scatter
  },
  data: () => ({
    loaded: false,
    chartdata: null,
    options: {}
  }),
  methods: {
    async loadChart() {
      this.loaded = false

      try {
        const res = await axios.get(`http://localhost:8081/api/v1/stats/passes/${this.league}`)

        let playerData = [] // HOLDS PLAYER DATA TO BE PLOTTED.

        let labels = [] // HOLDS PLAYER NAMES
        
        // Extract data from response 
        res.data.forEach(player => {
          let temp_player_data = {}
          
          // Append specific player info to array
          temp_player_data.x = player.key_passes
          temp_player_data.y = player.minutes_played
          
          // Append player name to labels
          labels.push(player.player_name)

          playerData.push(temp_player_data)
        })

        this.chartdata = {
          datasets: [{
            label: `${res.data[0].competition} (${res.data[0].season})`,
            data: playerData,
            pointBackgroundColor: "#ffc40d",
            backgroundColor: "#ffc40d"
          }]
        }

        this.options = {
          scales: {
            yAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Minutes Played',
                fontSize: 14,
                fontStyle: "italic"
              }
            }],
            xAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Key Passes',
                fontSize: 14, 
                fontStyle: "italic"
              }
            }]
          },
          tooltips: {
          callbacks: {
              label: function(tooltipItem) {
                  var label = labels[tooltipItem.index];
                  
                  return `${label}: Key Passes: ${tooltipItem.xLabel} Minutes: ${tooltipItem.yLabel}`
              }
            }
          },
          title: {
            display: true,
            text: 'Key Passes 🎯',
            fontSize: 14
          },
          legend: {
            display: true,
            labels: {
                fontColor: '#666'
            },
            position: "bottom"
          },
          responsive: true
        }

        // Data has finished loading so render component.
        this.loaded = true
      } catch (e) {
        console.error(e)
      }
    },
    clearChart() {
      this.options = {}
      this.chartdata = null
    },
    async updateChart(newLeague) {
        try {
        const res = await axios.get(`http://localhost:8081/api/v1/stats/passes/${newLeague}`)

        let playerData = [] // HOLDS PLAYER DATA TO BE PLOTTED.

        let labels = [] // HOLDS PLAYER NAMES
        
        res.data.forEach(player => {
          let temp_player_data = {}
          
          // Append specific player info to array
          temp_player_data.x = player.key_passes
          temp_player_data.y = player.minutes_played
          
          // Append player name to labels
          labels.push(player.player_name)

          playerData.push(temp_player_data)
        })

        await this.clearChart()

        this.chartdata = {
          datasets: [{
            label: `${res.data[0].competition} (${res.data[0].season})`,
            data: playerData,
            pointBackgroundColor: "#ffc40d",
            backgroundColor: "#ffc40d"
          }]
        }

        this.options = {
          scales: {
            yAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Minutes Played',
                fontSize: 14,
                fontStyle: "italic"
              }
            }],
            xAxes: [{
              scaleLabel: {
                display: true,
                labelString: 'Key Passes',
                fontSize: 14, 
                fontStyle: "italic"
              }
            }]
          },
          tooltips: {
          callbacks: {
              label: function(tooltipItem) {
                  var label = labels[tooltipItem.index];
                  
                  return `${label}: Tackles: ${tooltipItem.xLabel} Minutes: ${tooltipItem.yLabel}`
              }
            }
          },
          title: {
            display: true,
            text: 'Key Passes 🎯',
            fontSize: 14
          },
          legend: {
            display: true,
            labels: {
                fontColor: '#666'
            },
            position: "bottom"
          },
          responsive: true
        }
      } catch (e) {
        console.error(e)
      }
    }
  }, 
  async mounted () {
    this.loadChart()
  },
  watch: {
    league: async function (newValue) {
        this.updateChart(newValue)
    }
  }
}
</script>

<style scoped>
 .container{
   margin: 5px 25px;
 }
</style>