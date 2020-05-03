<template>
  <div>
    <radar-chart type="radar" height="350" :options="chartOptions" :series="chartSeries"/>
    <br>
    <player-panel :Players="playerInfo"/>
  </div>
</template>

<script>
import axios from "axios";
import VueApexCharts from 'vue-apexcharts';
import PlayerPanel from './PlayerPanel';

export default {
  data() {
    return {
      chartSeries: [],
      chartOptions: {},
      playerInfo: []
    };
  },
  components: {
    'radar-chart' : VueApexCharts,
    'player-panel': PlayerPanel
  },
  computed: {
    selectedPlayers() {
      return this.$store.state.selectedPlayers;
    }
  },
  methods: {
    async getPlayers(players) {
      // Clear playerInfo to remove duplicates
      this.clearPlayerInfo();

      try {
        for (var player of players) {
          const info = await axios.get(
            `http://localhost:8082/api/v1/players/${player}`
          );

          this.playerInfo.push(info.data[0]);
        }
      } catch (error) {
        console.log(`Failed: ${error}`);
      }
    },
    async clearPlayerInfo() {
      this.playerInfo = [];
    },
    async clearRadarChart() {
      this.chartOptions = {};
      this.chartSeries = [];
    },
    updateRadarChart(players) {
      // Clear Radar Chart Data
      this.clearRadarChart();

      for (var player of players) {
        let newSeries = {
          name: `${player.player_name} - ${player.season}`,
          data: [
            player.dribbleSuccess_per90,
            player.goals_per90,
            player.keyPasses_per90,
            player.shots_on_target_p90,
            player.assists_per90
          ]
        };
        this.chartSeries.push(newSeries);
      }

      // Set Chart Options
      this.chartOptions = {
        chart: {
          height: 350,
          type: "radar",
          dropShadow: {
            enabled: true,
            blur: 1,
            left: 1,
            top: 1
          }
        },
        title: {
          text: `xStat Comparison Matrix`
        },
        stroke: {
          width: 0
        },
        fill: {
          opacity: 0.4
        },
        markers: {
          size: 0
        },
        xaxis: {
          categories: ["Dribbles", "Goals", "Key Passes", "Shots On Target", "Assists"]
        }
      };
    }
  },
  watch: {
    selectedPlayers(newData) {
      // Fetch searched players then update chart
      this.getPlayers(newData).then(() => {
        this.updateRadarChart(this.playerInfo);
      });
    }
  }
};
</script>
