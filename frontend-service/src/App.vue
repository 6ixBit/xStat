<template>
  <div id="app">
    <nav-bar/>
  
    <grid/>
  </div>
</template>

<script>
import NavBar from "./components/NavBar"
import Grid from "./components/Grid"

export default {
  name: 'App',
  components: {
    "nav-bar" : NavBar,
    "grid" : Grid
  },
  data(){
    return {
    }
  }
}
</script>

