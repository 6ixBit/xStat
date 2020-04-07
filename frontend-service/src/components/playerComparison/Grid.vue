<template>
    <b-container class="bv-example-row">

      <br> <!-- INFO ABOUT PAGE -->
      <b-row align-h="center" align-v="center">
        <b-col cols="12" md="8" >  
          The player comparison matrix allows you to select your favourite players and
          plot them against each other. Once selected you can compare their data and draw your
          own conclusions from there!
        </b-col>
      </b-row>

      <br> <!-- SEARCH FOR PLAYER -->
      <b-row align-h="center" align-v="center">
        <b-col cols="6" md="4" > 

          <search-bar/>
          <radar-chart/>
          
        </b-col>
      </b-row>

      <br> <!-- CHARTS -->
      <b-row>
        <b-col md="6">
          It has survived not only five centuries,
           but also the leap into electronic typesetting, 
           remaining essentially unchanged. It was popularised in the 
           1960s with the release of Letraset sheets containing Lorem Ipsum passages.
        </b-col>

        <br>
        <b-col md="6"> <br>
         It has survived not only five centuries,
           but also the leap into electronic typesetting, 
           remaining essentially unchanged. It was popularised in the 
           1960s with the release of Letraset sheets containing Lorem Ipsum passages.
        </b-col>
      </b-row>

    </b-container>
</template>

<script>
import SearchBar from './SearchBar'
import RadarChart from './RadarChart'


export default {
    components: {
        "search-bar": SearchBar,
        "radar-chart": RadarChart
    } 
}
</script>