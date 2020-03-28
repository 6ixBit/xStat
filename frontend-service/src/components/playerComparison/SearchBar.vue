<template>
  <div>
       <b-form-input @input="OnChange"  v-model="text" placeholder="Enter player name" id="search_player"></b-form-input>
    <div class="mt-2">Value: {{ text }} </div>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    data() {
      return {
        text: '',
        player_names: []
      }
    },
    methods: {
        async OnChange(){
            //@desc Make AJAX call to backend for search potential results
            const matched_players = await axios.get(`http://localhost:8082/api/v1/players/search/${this.text}`)

            // Set response from AJAX request to component state data
            // https://alligator.io/vuejs/vue-autocomplete-component/
            console.log(matched_players)
        }
    }
  }
</script>
