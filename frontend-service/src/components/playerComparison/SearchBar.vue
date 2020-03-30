<template>
  <div>
    <div>
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
        numbOfResults: 0
      }
    },
    computed: {
      selectedPlayers(){
        return this.$store.state.selectedPlayers
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
              console.log(error)
              this.numbOfResults = 0
          }
      },
      addPlayer(player) {
        // Mutate state to add player in store 
        this.$store.commit('addPlayer', player)
      },
      removePlayer(playerName){
        // Mutate state to remove player in store 
        this.$store.commit('removePlayer', playerName)
      }
    }
  }
</script>

<style scoped>
* {
  box-sizing: border-box;
}

/*the container must be positioned relative:*/
.autocomplete {
  position: relative;
  display: inline-block;
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