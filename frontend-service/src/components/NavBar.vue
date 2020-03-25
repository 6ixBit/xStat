<template>
    <div>
       <nav class="navbar navbar-expand-lg navbar-light bg-dark">
         <router-link to='/'><a class="navbar-brand" href="#" id="menu-item0">xStat</a></router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">  
                    <li class="nav-item active">
                        <router-link to='/'><a class="nav-link" href="#" id="menu-item1">Home <span class="sr-only">(current)</span></a></router-link>
                    </li>

                    <li class="nav-item">
                        <router-link to="/playercomparison"><a class="nav-link" href='/playercomparison' to='/playercomparison' id="menu-item2">Player comparison</a></router-link>
                    </li>
                </ul>

                <form class="form-inline my-2 my-lg-0">
                    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                </form>

            </div>
        </nav>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
 #menu-item0, #menu-item1, #menu-item2, #menu-item3  {
     color: #FFFFFF;
 }
</style>