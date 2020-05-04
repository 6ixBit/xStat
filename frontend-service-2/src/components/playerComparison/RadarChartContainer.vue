<template>
  <div>
    <div class="radarContainer">
      <radar-chart :key="componentKey" v-if="loaded" :chart-data="formatOffensivePlayerData" :options="options"/>
      </div>
    {{ formatOffensivePlayerData }}
    key: {{ componentKey }}
  </div>
</template>

<script>
import Radar from "../Charts/RadChart";

export default {
  data() {
    return {
      loaded: false,
      chartdata: null,
      options: {}
    };
  },
  components: {
    "radar-chart": Radar
  },
  computed: {
    selectedPlayers() {
      return this.$store.state.selectedPlayers;
    },
    playerInfo() {
      return this.$store.state.playerInfo;
    },
    formatOffensivePlayerData() {
      return this.$store.getters.formatOffensivePlayerData
    }
  },
  methods: {
    clearRadarChart() {
      this.chartdata = {};
      this.options = [];
    },
    updateRadarChart() {
      this.loaded = false;
      this.chartdata = this.formatOffensivePlayerData      

      try {
        this.options = {
          tooltips: {
            mode: 'label'
          },
          responsive: true,
          maintainAspectRatio: false
        }
        this.loaded = true;
      } catch (error) {
        console.log(error);
      }
    }
  },
  watch: {
    selectedPlayers() {
      this.$store.commit("clearPlayerInfo");
      this.$store.commit("getPlayers");

      // Then Update Chart with Player Info Data.
      this.updateRadarChart();
    }
  },
  mounted() { // RENDERS CHART WHEN PAGE IS REFRESHED
    this.updateRadarChart()
  }
};
</script>

<style scoped>
 .radarContainer{
   display: flex;
   justify-content: center;
 }
</style>