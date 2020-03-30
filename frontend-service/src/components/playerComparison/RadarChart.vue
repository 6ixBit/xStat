<template>
    <div> 
        {{ radarChartSeries }}
    </div>
</template>

<script>
// Third party imports
//import VueApexCharts from 'vue-apexcharts'

export default {
    computed: {
        radarChartSeries(){
            return this.$store.state.radarChartSeries;
        }
    }
}
</script>