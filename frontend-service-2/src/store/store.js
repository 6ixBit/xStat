// Third party imports
import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

// Init Vuex
Vue.use(Vuex)

let dynamicColors = function(numberOfColors) {
    var r = Math.floor(Math.random() * 255);
    var g = Math.floor(Math.random() * 255);
    var b = Math.floor(Math.random() * 255);

    let Colors = []

    for(let i=0; i < numberOfColors; i++) {
        let rgb = "rgb(" + r + "," + g + "," + b + ")"; 
        Colors.push(rgb)
    }
    return Colors
}

export const store = new Vuex.Store({
    state: {
        selectedPlayers: [], // PLAYER NAMES OF THOSE SELECTED
        playerInfo: [] // PLAYER INFO FETCHED 
    },
    getters: {
        formatOffensivePlayerData: (state) => {
            let players = []

           state.playerInfo.map( player => {
                let {dribbleSuccess_per90, 
                    goals_per90, 
                    keyPasses_per90, 
                    shots_on_target_p90, 
                    assists_per90,
                    tacklesCompleted_per90
                } = player

                players.push({
                    label: `${player.player_name} (${player.season})`, 
                    data: [dribbleSuccess_per90, 
                            goals_per90, 
                            keyPasses_per90, 
                            shots_on_target_p90, 
                            assists_per90,
                            tacklesCompleted_per90
                        ],
                    borderColor: dynamicColors(1)
                })
           })

           return {
            labels: ["Dribbles", "Goals", "Key Passes","Shots On Target", "Assists", "Tackles"],
            datasets: players 
           }
        }
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







