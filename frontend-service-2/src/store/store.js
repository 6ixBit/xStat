// Third party imports
import Vue from 'vue'
import Vuex from 'vuex'

// Init Vuex
Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        selectedPlayers: [] // PLAYER NAMES OF THOSE SELECTED
    },
    mutations: {
        removePlayer(state, playerName){
            // @desc Remove player from selected list
            state.selectedPlayers = state.selectedPlayers.filter(el => el !== playerName)
        },
        addPlayer(state, player) {
            // @desc A selected player is added to list of select 
 
            // Check for duplicates of players in list.
            for (var plyr in state.selectedPlayers){
                if (player === plyr) {
                    return []
                }
            }

            if (state.selectedPlayers.length >= 2) {
                alert("You can not add more than 2 players")
            } else {
                state.selectedPlayers.push(player)
            }
        }
    }
}) 







