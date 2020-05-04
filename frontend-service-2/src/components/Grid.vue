<template>
 
  <div>
    <Row type="flex" justify="center">
        <i-col span="24">
            <h1 class="homeText">- Frontend Service 2 -</h1>
            <p class="homeText"> View the statistics from Europe's Top football leagues by selecting a 
            league of choice from the drop down menu.
            </p>
        </i-col>
    </Row>

    <div class="row-select">
      <Row type="flex" justify="end">
          <i-col span="24">
            <select-league v-on:leagueModified="updateCharts($event)"/>
          </i-col>
      </Row>
    </div>


     <Row type="flex" justify="center" class="firstRowCharts">
        <i-col :span="getGridSpan">
          <goals-scatter :league="currentLeague"/>
        </i-col>

        <i-col :span="getGridSpan">
          <dribbles-scatter :league="currentLeague"/>
        </i-col>
    </Row>

    <Row type="flex" justify="center" class="secondRowCharts">
        <i-col :span="getGridSpan">
          <tackles-scatter :league="currentLeague"/>
        </i-col>

        <i-col :span="getGridSpan">
          <passes-scatter :league="currentLeague"/>
        </i-col>
    </Row>

  </div>

</template>

<script>
import GoalsScatterChart from "./GoalsScatterChart"
import DribbleScatterChart from "./DribbleScatterChart"
import TacklesScatterChart from "./TacklesScatterChart"
import PassesScatterChart from "./PassingScatterChart"
import SelectMenu from './SelectLeague'

export default {
    components : {
      "goals-scatter" : GoalsScatterChart,
      "dribbles-scatter": DribbleScatterChart,
      "tackles-scatter": TacklesScatterChart,
      "passes-scatter": PassesScatterChart,
      "select-league" : SelectMenu
    },
    data(){
      return {
        currentLeague : "Premier League"
      }
    },
    computed: {
      getGridSpan() {
        if(this.$mq === "mobile") {
          return "24"
        } else {
          return "12"
        }
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
  .homeText {
    text-align: center;
    word-wrap: break-word;
    margin-top: 5px;
    margin-bottom: 3px;
  }

  .row-select {
    display: flex;
    justify-content: center;
    margin: 15px 10px;
  }


  @media only screen 
  and (min-device-width: 320px) 
  and (max-device-width: 480px)
  and (-webkit-min-device-pixel-ratio: 2) {
    .firstRowCharts{
      display: flex;
      justify-content: center;
      flex-direction: column
    }

     .secondRowCharts{
      display: flex;
      justify-content: center;
      flex-direction: column;
    }
}
</style>