<template>
  <div>
    <div>
      <div class="autocomplete"> <!-- SEARCH PLAYERS -->
          <b-form-input @input="OnChange"  v-model="text" placeholder="Enter player name" id="search_player"></b-form-input>
      </div>

      <div> <!-- SELECTED PLAYERS -->
      <b-badge pill variant="primary" v-for="selected in selectedPlayers" :key="selected.id" @click="removePlayer(selected)"> {{selected}} </b-badge> 
      </div>

       <b-list-group class="Listed">
         <b-list-group-item class="searchList" v-for="player in players" :key="player.id" @click="addPlayer(player)">{{player.player_name}} - {{player.competition}} </b-list-group-item>
       </b-list-group>

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
  .searchList {
    cursor: pointer;
  }

  .Listed {
    position: absolute;
    z-index: 5;
  }

  .searchList:hover {
    background-color: #0080ff
  }
</style>