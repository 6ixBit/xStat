<template>
    <b-container class="bv-example-row">

      <b-row align-h="center" align-v="center"> <!-- GENERAL INFO -->
        <b-col cols="12" md="8"> It has survived not only five centuries,
           but also the leap into electronic typesetting, 
           remaining essentially unchanged. It was popularised in the 
           1960s with the release of Letraset sheets containing Lorem Ipsum passages.
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
         <!-- <scatter :chartData="series"/> -->
        </b-col>
      </b-row>

    </b-container>
</template>

<script>
import ScatterChart from "./ScatterChart"
import SelectMenu from './SelectLeague'

export default {
    components : {
      "scatter" : ScatterChart,
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