<template>
  <div>
    <!-- INFO ABOUT PAGE -->
    <div class="infoWrapper">
    <Row type="flex" justify="center">   
        <i-col span="24">
            <p> The player comparison matrix allows you to select your favourite players and
          plot them against each other. Once selected you can compare their data and draw your
          own conclusions from there! Once selected you can compare their data and draw your
          own conclusions from there!  </p>
        </i-col>
    </Row>
    </div>
    
   <div class="searchBarWrapper"> 
    <Row type="flex" justify="center">
        <i-col span="24">
          <search-bar/>
        </i-col>
    </Row>
    </div>

    <div class="chartWrapper">

    <Row type="flex" justify="center">
        <i-col span="24">
           <radar-chart></radar-chart>
        </i-col>
    </Row>
    
    </div>

  </div>

</template>

<script>
import SearchBar from './SearchBar'
import RadarChart from './RadarChartContainer' // SWAP OUT TEST CHART AFTER.

export default {
    components: {
        "search-bar": SearchBar,
        "radar-chart": RadarChart
    } 
}
</script>

<style scoped>

 .chartWrapper {
   margin: 20px 10px;
   display: flex;
   justify-content: center;
 }

.searchBarWrapper {
  margin: 20px 10px;
  display: flex;
  justify-content: center;
}

.infoWrapper {
  margin: 10px 10px;
}

.infoWrapper p {
  text-align: center;
  font-size: 14px;
  padding: 10px 20px;
}
</style>