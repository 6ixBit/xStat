<template>
  <div>
    <!-- INFO ABOUT PAGE -->
    <div class="infoWrapper">
      <Row type="flex" justify="center">   
          <i-col :span="getGridSpan">
              <p class="infoText"> The player comparison matrix allows you to select your favourite players and
            plot them against each other. Once selected you can compare their data on the chart
            on a per90 basis or view their whole numbers side by side in the list below.  </p>
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
            <radar-chart/>
          </i-col>
      </Row>
    </div>

    <div class="tableWrapper">
      <Row type="flex" justify="center">
          <i-col span="24">
            <table-view/>
          </i-col>
      </Row>
    </div>

  </div>

</template>

<script>
import SearchBar from './SearchBar'
import RadarChart from './RadarChartContainer' 
import TableView from './TableView'

export default {
    components: {
        "search-bar": SearchBar,
        "radar-chart": RadarChart,
        "table-view": TableView
    },
    computed: {
      getGridSpan(){
        if(this.$mq === "mobile"){ // Responsive Grid
          return "24"
        } else {
          return "12"
        }
      }
    }
}
</script>

<style scoped>

 .chartWrapper {
   margin: 20px 10px;
   display: flex;
   justify-content: center;
 }

 .tableWrapper{
   display:flex;
   justify-content: center;
 }

.searchBarWrapper {
  margin: 20px 10px;
  display: flex;
  justify-content: center;
}

.infoWrapper {
  margin: 10px 10px;
  width: 100%;
}

.infoWrapper p {
  text-align: center;
  font-size: 14px;
  padding: 10px 20px;  
}

@media only screen and (min-width: 400px) {
  .infoText{
    display: flex;
    justify-content: center;
    align-items: center;
 }
}
</style>