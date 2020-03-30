// Third party imports
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

// Init Vuex
Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        radarChartSeries: [1,2,3,4,5], // HOLDS ACTUAL CHART DATA
        selectedPlayers: [],
        playerInfo: [] // HOLDS ALL JSON FOR SELECTED PLAYERS 
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
        },
        clearPlayerInfo(state) {
            // @desc Clear playerInfo object
            state.playerInfo = []
        }
    },
    actions: {
        async getPlayers(context) {
            // Clear player Info to avoid duplicates
            context.commit('clearPlayerInfo')

           try {
               for (var player of context.state.selectedPlayers) {
                   const info = await axios.get(`http://localhost:8082/api/v1/players/${player}`)

                   // Add new player to Player info
                   context.state.playerInfo.push(info)
               }
           }  catch (error) {
               console.log(error)
           }
        }
    }
}) 