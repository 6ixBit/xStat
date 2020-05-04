<template>
    <div class="listContainer">
      
        <List :header="player.player_name" 
            border size="large" 
            class="listItem" 
            v-for="player in getPlayers"
            :key="player.id"
            >
                <ListItem>
                   <p style="color:#1e272e">{{player.team_name}}</p>
                </ListItem>

                <ListItem>
                   <p style="color:#1e272e">{{player.competition}} ({{player.season}})</p>
                </ListItem>

                <ListItem>
                    Goals
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.goals}}</p>
                        </li>
                    </template>
                </ListItem> 

                <ListItem>
                    Assists
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.assists}}</p>
                        </li>
                    </template>
                </ListItem> 

                <ListItem>
                    Minutes
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.minutes_played}}</p>
                        </li>
                    </template>
                </ListItem> 

                <ListItem>
                    Key Passes
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.key_passes}}</p>
                        </li>
                    </template>
                </ListItem> 

                <ListItem>
                    Pass Accuracy
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.pass_accuracy}}%</p>
                        </li>
                    </template>
                </ListItem> 

                <ListItem>
                    Passes
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.total_passes}}</p>
                        </li>
                    </template>
                </ListItem> 

                <ListItem>
                    Dribbles
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.dribble_success}}</p>
                        </li>
                    </template>
                </ListItem> 

               <ListItem>
                    Interceptions
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.interceptions}}</p>
                        </li>
                    </template>
                </ListItem>  

                <ListItem>
                    Tackles
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.completed_tackles}}</p>
                        </li>
                    </template>
                </ListItem>

                <ListItem>
                    Fouls Drawn
                    <template slot="action">
                        <li>
                            <p style="color:#1e272e">{{player.fouls_drawn}}</p>
                        </li>
                    </template>
                </ListItem> 
        </List>

    </div>
</template>

<script>

export default {
    name: "TableView",
    data() {
        return {
            split: true
        }
    },
    computed: {
        getPlayers() {
            return this.$store.state.playerInfo
        },
        organisePlayerName(playerName, playerAge) {
            return `${playerName} - ${playerAge}`
        }
    }
}
</script>

<style scoped>
 .listContainer{
     display: flex;
 }

 .listItem {
     margin: 3px 10px;
     margin-top: 2px;
     margin-bottom: 4px;
 }

</style>