<template>
    <div>
        <nav-bar/>
        <grid/>
    </div>
</template>

<script>
import NavBar from "./NavBar"
import Grid from "./Grid"

export default {
    name: 'Home',
    components: {
        "nav-bar" : NavBar,
        "grid" : Grid
  }
}
</script>