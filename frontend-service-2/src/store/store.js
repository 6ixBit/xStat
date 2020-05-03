// Third party imports
import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

// Init Vuex
Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        selectedPlayers: [], // PLAYER NAMES OF THOSE SELECTED
        playerInfo: [] // PLAYER INFO FETCHED 
    },
    mutations: {
        removePlayer(state, playerName) {
            // @desc Remove player from selected list
            state.selectedPlayers = state.selectedPlayers.filter(el => el !== playerName)
        },
        addPlayer(state, player) {
            // Check for duplicates of players in list.
            for (var plyr in state.selectedPlayers) {
                if (player === plyr) {
                    return []
                }
            }

            if (state.selectedPlayers.length >= 2) {
                alert("You can not add more than 2 players")
            } else {
                state.selectedPlayers.push(player)
            }
        },
        clearPlayerInfo(state) {
            state.playerInfo = [];
        },
        getPlayers(state) {
            try {
                for (var player of state.selectedPlayers) {
                    axios.get(
                        `http://localhost:8082/api/v1/players/${player}`
                    ).then( resp => {state.playerInfo.push(resp.data[0])})
                }
            } catch (error) {
                console.log(`Failed: ${error}`);
            }
        }
    }
})







