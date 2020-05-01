<template>
    <b-container class="bv-example-row">

      <b-row align-h="center" align-v="center"> <!-- GENERAL INFO -->
        <b-col cols="12" md="8">
          <h1>Frontend Service 1</h1>
          <p class="homeText"> View the statistics from Europe's Top football leagues by selecting a 
          league of choice from the drop down menu.
           </p>
        </b-col>
      </b-row>

      <br> <!-- SELECT A LEAGUE -->
      <b-row align-h="center" align-v="center">
        <b-col cols="6" md="4" >  
          <select-league v-on:leagueModified="updateCharts($event)"/>
        </b-col>
      </b-row>

      <br> <!-- CHARTS -->
      <b-row>
        <b-col md="6">
          <scatter :league="currentLeague"/>
        </b-col>

        <b-col md="6">
         <passes-scatter :league="currentLeague"/>
        </b-col>
      </b-row>

    </b-container>
</template>

<script>
import GoalsScatterChart from "./GoalsScatterChart"
import DribbleScatterChart from "./DribbleScatterChart"
import SelectMenu from './SelectLeague'

export default {
    components : {
      "scatter" : GoalsScatterChart,
      "passes-scatter": DribbleScatterChart,
      "select-league" : SelectMenu
    },
    data(){
      return {
        currentLeague : "Premier League"
      }
    },
    methods : {
      updateCharts(leagueName){
        // Assign value from select option event to a data variable so children charts can update
        this.currentLeague = leagueName
      }
    }
}
</script>

<style scoped>
  .homeText{
    text-align: center;
    margin-top: 5px;
  }
</style>