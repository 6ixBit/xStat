import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        radarChartSeries: [1,2,3,4,5],
        selectedPlayers: []
    },
    mutations: {
        removePlayer(state, playerName){
            // @desc Remove player from selected list
            state.selectedPlayers = state.selectedPlayers.filter(el => el !== playerName)
          },

        addPlayer(state, player) {
            // @desc A selected player is added to list of select players
            if (state.selectedPlayers.length >= 2) {
                alert("You can not add more than 2 players")
            } else {
                state.selectedPlayers.push(player.player_name)
            }
        }
    }
}) 