<template>
  <div>
    <div class="autocompleteWrapper">
    <AutoComplete
        v-model="text"
        @on-search="OnChange"
        @on-select="addPlayer"
        placeholder="Search for a player..."
        style="width:200px">
  
        <Option v-for="player in players" :value="player.player_name" :key="player.id" >{{player.player_name}} - {{player.competition}}</Option>
        </AutoComplete>
      </div>

      <div class="playerTags"> <!-- Remove players when done. -->
        <Tag closable @on-close="removePlayer(selected)" v-for="selected in selectedPlayers" :key="selected.id">{{selected}}</Tag>
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
 .playerTags {
   margin: 5px 5px;
 }
</style>