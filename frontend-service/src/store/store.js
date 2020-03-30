import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        radarChartSeries: [1,2,3,4,5]
    }
}) 