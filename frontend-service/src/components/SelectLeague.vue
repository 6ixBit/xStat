<template>

    <div>
        <p>Choose a league: {{ selected }}</p>
        <b-form-select v-model="selected" :options="leagueData">
            <template v-slot:first>
               <b-form-select-option :value="null" disabled>-- Select a league --</b-form-select-option>
                <!-- <b-form-select-option v-for="league of leagueData" v-bind:key="league.id"> </b-form-select-option> -->
            </template>
        </b-form-select>
  </div>

</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            selected: "",
            leagueData: []
        }
    },
    async created(){
        try {
            // Make request to general micro service.
            const res = await axios.get("http://localhost:8081/api/v1/stats/leagues")
            console.log(res)

            this.leagueData = res // Set league data to list of leagues array.
        } catch (e) {
            console.log(e)
        }
    }
}
</script>