<template>
  <div>
    <div>
      Players: {{ selectedPlayers }}
      <div class="autocomplete"> <!-- SEARCH PLAYERS -->
          <b-form-input @input="OnChange"  v-model="text" placeholder="Enter player name" id="search_player"></b-form-input>
      </div>

      <div> <!-- SELECTED PLAYERS -->
      <b-badge pill variant="primary" v-for="selected in selectedPlayers" :key="selected.id" @click="removePlayer(selected)"> {{selected}} </b-badge> 
      </div>

        Results: {{ numbOfResults }}

       <ul> <!-- MATCHED PLAYER NAMES -->
         <li v-for="player in players" :key="player.id" @click="addPlayer(player)"> {{player.player_name}} - {{player.competition}} </li>
       </ul>
    </div>

  
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    data() {
      return {
        text: '',
        players: [],
        numbOfResults: 0,
        selectedPlayers: []
      }
    },
    methods: {
      async OnChange() {
          this.players = []

          //@desc Make AJAX call to backend for search potential results
        try {
            const matched_players = await axios.get(`http://localhost:8082/api/v1/players/search/${this.text}`)

            // Set Number of potential results
            this.numbOfResults = matched_players.data.results

            // Append matched results to component data
            for (var player of matched_players.data.players) {
                this.players.push(player)
            }
  
            } catch (error) {
            // When request fails set returned results to 0
            console.log(error)
            this.numbOfResults = 0
          }
      },
      addPlayer(player) {
        //@desc A selected player is added to list of select players
        // Check size of players selected, if more than 2 then prevent user from adding a new player.
        if (this.selectedPlayers.length >= 2) {
          alert("You can not add more than 2 players")
        } else {
          this.selectedPlayers.push(player.player_name)
        }
      },
      removePlayer(playerName){
        // @desc Remove player from selected list
        this.selectedPlayers = this.selectedPlayers.filter(el => el !== playerName)
      }

    }
  }
</script>

<style scoped>
* {
  box-sizing: border-box;
}

body {
  font: 16px Arial;  
}

/*the container must be positioned relative:*/
.autocomplete {
  position: relative;
  display: inline-block;
}

input {
  border: 1px solid transparent;
  background-color: #f1f1f1;
  padding: 10px;
  font-size: 16px;
}

input[type=text] {
  background-color: #f1f1f1;
  width: 100%;
}

input[type=submit] {
  background-color: DodgerBlue;
  color: #fff;
  cursor: pointer;
}

.autocomplete-items {
  position: absolute;
  border: 1px solid #d4d4d4;
  border-bottom: none;
  border-top: none;
  z-index: 99;
  /*position the autocomplete items to be the same width as the container:*/
  top: 100%;
  left: 0;
  right: 0;
}

.autocomplete-items div {
  padding: 10px;
  cursor: pointer;
  background-color: #fff; 
  border-bottom: 1px solid #d4d4d4; 
}

/*when hovering an item:*/
.autocomplete-items div:hover {
  background-color: #e9e9e9; 
}

/*when navigating through the items using the arrow keys:*/
.autocomplete-active {
  background-color: DodgerBlue !important; 
  color: #ffffff; 
}
</style>