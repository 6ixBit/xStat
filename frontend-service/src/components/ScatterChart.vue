<template>
    <div id="chart">
        <apexchart type="scatter" width="100%" height="350" :options="chartOptions" :series="series"></apexchart>
        <p>{{this.league}}</p>
    </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import axios from 'axios'

export default {
    props : ['league'],
    components : {
        apexchart : VueApexCharts
    },
    data() {
        return {
            series: [{ // For chart data
              name: "SAMPLE A",
              data: [
              [16.4, 5.4], [21.7, 2], [25.4, 3], [19, 2], [10.9, 1], [13.6, 3.2], [10.9, 7.4], [10.9, 0], [10.9, 8.2], [16.4, 0], [16.4, 1.8], [13.6, 0.3], [13.6, 0], [29.9, 0], [27.1, 2.3], [16.4, 0], [13.6, 3.7], [10.9, 5.2], [16.4, 6.5], [10.9, 0], [24.5, 7.1], [10.9, 0], [8.1, 4.7], [19, 0], [21.7, 1.8], [27.1, 0], [24.5, 0], [27.1, 0], [29.9, 1.5], [27.1, 0.8], [22.1, 2]]
            },{
              name: "SAMPLE B",
              data: [
              [36.4, 13.4], [1.7, 11], [5.4, 8], [9, 17], [1.9, 4], [3.6, 12.2], [1.9, 14.4], [1.9, 9], [1.9, 13.2], [1.4, 7], [6.4, 8.8], [3.6, 4.3], [1.6, 10], [9.9, 2], [7.1, 15], [1.4, 0], [3.6, 13.7], [1.9, 15.2], [6.4, 16.5], [0.9, 10], [4.5, 17.1], [10.9, 10], [0.1, 14.7], [9, 10], [12.7, 11.8], [2.1, 10], [2.5, 10], [27.1, 10], [2.9, 11.5], [7.1, 10.8], [2.1, 12]]
            }],
            chartOptions: {
            chart: {
              height: 350,
              type: 'scatter',
              zoom: {
                enabled: true,
                type: 'xy'
              }
            },
            title: {
              text: "Premier League 2019-2020",
              align: 'left'
            },
            xaxis: {
              tickAmount: 10,
              title : {
                text: "Minutes"
              },
              labels: {
                formatter: function(val) {
                  return parseFloat(val).toFixed(1)
                }
              }
            },
            yaxis: {
              tickAmount: 7,
              title : {
                text: "Goals"
              }
            }
          }    
        }
    },
    async created(){
        try {
            // Make request to general micro service to fetch goals stats
            const res = await axios.get(`http://localhost:8081/api/v1/stats/goals/${this.league}`)

            // Test print data to screen
            console.log(res.data)
        } catch (e) {
            console.log(e)
        }
    },
    watch: {
      league: async function (newVal) { // Watch for league prop being updated.
        const newResult = await axios.get(`http://localhost:8081/api/v1/stats/goals/${newVal}`)

        // Update chart data on prop change.
        this.chartOptions.title.text = newResult.data[0].competition

        console.log(newResult.data[0].season)

        // TESTING updating chart data! WORKS with dummy data.
        this.series = [{
          name: 'series-1',
          data: [[16.4, 5.4], [21.7, 2], [25.4, 3], [19, 2], [10.9, 1]]
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
              text: `${newResult.data[0].competition} - ${newResult.data[0].season}`,
              align: 'left'
            },
            xaxis: {
              tickAmount: 10,
              title : {
                text: "Minutes"
              },
              labels: {
                formatter: function(val) {
                  return parseFloat(val).toFixed(1)
                }
              }
            },
            yaxis: {
              tickAmount: 7,
              title : {
                text: "Goals"
              }
            }
          }

      }
    }
}
</script>
