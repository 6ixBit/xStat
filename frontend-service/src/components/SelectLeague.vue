<template>

    <div>
        <p>Choose a league: {{ selected }}</p>
        <b-form-select v-model="selected" @change="selectedLeague">
            <template v-slot:first>
                <b-form-select-option v-for="league in leagueData" v-bind:key="league.id" :value="league.value"> {{league.text}} </b-form-select-option> 
            </template>
        </b-form-select>
  </div>

</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            selected: "Premier League",
            leagueData: []
        }
    },
    async created(){
        try {
            // Make request to general micro service.
            const res = await axios.get("http://localhost:8081/api/v1/stats/leagues")
            
            // Set league data to list of leagues array.
            this.leagueData = res.data
        } catch (e) {
            console.log(e)
        }
    },
    methods: {
        selectedLeague(){
            // Send an event to the parent when the select option has changed
            this.$emit("leagueModified", this.selected)
        }
    }
}
</script>