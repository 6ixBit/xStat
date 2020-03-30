// Third party imports
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

// Init Vuex
Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        radarChartSeries: [], // HOLDS ACTUAL CHART DATA
        radarChartOptions: {}, // HOLDS CHART OPTIONS
        selectedPlayers: [], // PLAYER NAMES OF THOSE SELECTED
        playerInfo: [] // HOLDS ALL RELEVANT JSON FOR CURRENT SELECTED PLAYERS 
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
            state.playerInfo = [];
        },
        clearRadarChart(state) {
            state.radarChartSeries = []
            state.radarChartOptions = {}
        },
        updateRadarChart(state) {
            // Check if current player is empty
             //if( state.playerInfo === [] ) { return [] }

            // Loop players and add data to series
            state.playerInfo.forEach( (player) => {
                console.log(player)

                let series = {
                    name: `${player.player_name} - ${player.season}`,
                    data: [player.dribbleSuccess_per90, player.goals_per90, 
                            player.keyPasses_per90, player.shots_on_target_p90,
                            player.assists_per90]
                }
                state.radarChartSeries.push(series)
            })
        }
    },
    actions: {
        async getPlayers(context) {
            // Clear player Info to avoid duplicates
            // context.commit('clearPlayerInfo') GIVES ISSUES
           try {
               for (var player of context.state.selectedPlayers) {
                   const info = await axios.get(`http://localhost:8082/api/v1/players/${player}`)

                   this.state.playerInfo.push(info.data[0])
               }
           }  catch (error) {
               console.log(error)
           }
        }
    }
}) 