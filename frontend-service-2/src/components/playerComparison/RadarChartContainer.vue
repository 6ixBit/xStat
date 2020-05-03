<template>
  <div>
    <radar-chart></radar-chart>
    {{playerInfo}}
  </div>
</template>

<script>
import Radar from "../Charts/RadChart"

export default {
  data() {
    return {
      loaded: false,
      chartdata: null,
      options: {}
    };
  },
  components: {
    'radar-chart' : Radar,
  },
  computed: {
    selectedPlayers() {
      return this.$store.state.selectedPlayers;
    },
    playerInfo() {
      return this.$store.state.playerInfo;
    }
  },
  methods: {
    clearRadarChart() {
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
      this.$store.commit("clearPlayerInfo")
      this.$store.commit("getPlayers")

      // Fetch searched players then update chart
      // this.getPlayers(newData).then(() => {
      //   this.updateRadarChart(this.playerInfo);
      // });
    }
  }
};
</script>
