<template>
  <div>
    <AutoComplete
        v-model="text"
        :data="players"
        @on-search="OnChange"
        placeholder="Search for a player"
        style="width:200px"></AutoComplete>

      <div> <!-- SELECTED PLAYER -->
      <b-badge pill variant="primary" v-for="selected in selectedPlayers" :key="selected.id" @click="removePlayer(selected)"> {{selected}} </b-badge> 
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
                this.players.push(`${player.player_name} - ${player.competition}`)
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