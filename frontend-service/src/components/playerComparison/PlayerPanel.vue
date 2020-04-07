<template>
  <div>
    <b-container class="bv-example-row">
    
        <b-card no-body style="max-width: 20rem;" 
        v-for="player in Players" :key="player.id">

          <template v-slot:header>
            <h4 class="mb-0"> {{player.player_name}}, {{ player.age }} </h4>
          </template>

          <b-list-group flush>
            <b-list-group-item>{{player.team_name}}</b-list-group-item>
            <b-list-group-item>Goals: {{ player.goals }}</b-list-group-item>
            <b-list-group-item>Assists: {{player.assists}}</b-list-group-item>
            <b-list-group-item>Pass Accuracy: {{player.pass_accuracy}}%</b-list-group-item>
            <b-list-group-item>Minutes Played: {{ player.minutes_played }}</b-list-group-item>
          </b-list-group>

          <b-card-body>
            <a href="#" class="card-link">View Profile</a>
          </b-card-body>
        </b-card>

    </b-container>
  </div>
  
</template>

<script>
export default {
  props: ['Players'] // Player Info From Radar Component
}
</script>
