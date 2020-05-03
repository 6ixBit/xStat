<template>
    <div>
        <nav-bar/>
        <grid/>
    </div>
</template>


<script>
import NavBar from '../components/NavBar'
import Grid from '../components/playerComparison/Grid'

export default {
    components: {
        'nav-bar' : NavBar,
        'grid': Grid
    }
}
</script>