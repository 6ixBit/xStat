<template>
    <b-container class="bv-example-row">

      <b-row align-h="center" align-v="center"> <!-- GENERSL INFO -->
        <b-col cols="12" md="8"> It has survived not only five centuries,
           but also the leap into electronic typesetting, 
           remaining essentially unchanged. It was popularised in the 
           1960s with the release of Letraset sheets containing Lorem Ipsum passages.
        </b-col>
      </b-row>

      <br> <!-- SELECT A LEAGUE -->
      <b-row align-h="center" align-v="center">
        <b-col cols="6" md="4" >  
          <select-league :childValue="TestValues"/>
        </b-col>
      </b-row>

      <br> <!-- CHARTS -->
      <b-row>
        <b-col md="6">
          <scatter :chartData="series"/>
        </b-col>

        <b-col md="6">
          <scatter :chartData="series"/>
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
      series: [{ // For chart data
            name: "SAMPLE A",
            data: [
            [16.4, 5.4], [21.7, 2], [25.4, 3], [19, 2], [10.9, 1], [13.6, 3.2], [10.9, 7.4], [10.9, 0], [10.9, 8.2], [16.4, 0], [16.4, 1.8], [13.6, 0.3], [13.6, 0], [29.9, 0], [27.1, 2.3], [16.4, 0], [13.6, 3.7], [10.9, 5.2], [16.4, 6.5], [10.9, 0], [24.5, 7.1], [10.9, 0], [8.1, 4.7], [19, 0], [21.7, 1.8], [27.1, 0], [24.5, 0], [27.1, 0], [29.9, 1.5], [27.1, 0.8], [22.1, 2]]
          },{
            name: "SAMPLE B",
            data: [
            [36.4, 13.4], [1.7, 11], [5.4, 8], [9, 17], [1.9, 4], [3.6, 12.2], [1.9, 14.4], [1.9, 9], [1.9, 13.2], [1.4, 7], [6.4, 8.8], [3.6, 4.3], [1.6, 10], [9.9, 2], [7.1, 15], [1.4, 0], [3.6, 13.7], [1.9, 15.2], [6.4, 16.5], [0.9, 10], [4.5, 17.1], [10.9, 10], [0.1, 14.7], [9, 10], [12.7, 11.8], [2.1, 10], [2.5, 10], [27.1, 10], [2.9, 11.5], [7.1, 10.8], [2.1, 12]]
          }],
       TestValues: [ // For Select drop down component
            { value: 'a', text: 'Premier League' },
            { value: 'b', text: 'Serie A' },
            { value: 'c', text: 'La Liga' },
            { value: 'd', text: 'Ligue 1' },
            { value: 'f', text: 'Bundesliga'}
        ]
      }
    }
}
</script>