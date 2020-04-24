<template>
    <div class="navBar">
       <b-navbar toggleable="lg" type="dark" variant="dark">
     <router-link to='/'> <b-navbar-brand to='/'>xStat</b-navbar-brand> </router-link>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item to="/playercomparison">Player Comparison</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

      </b-navbar-nav>
    </b-collapse>
  </b-navbar> 
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
.navbar {
    margin-bottom: 8px;
}

</style>