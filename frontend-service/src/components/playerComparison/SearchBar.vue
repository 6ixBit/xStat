<template>
  <div>
       <b-form-input @input="OnChange"  v-model="text" placeholder="Enter player name" id="search_player"></b-form-input>
    <div class="mt-2">Value: {{ text }}</div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        text: ''
      }
    },
    methods: {
        OnChange(){
            //@desc Make AJAX call to backend for search potential results
            console.log(this.text)
        }
    }
  }
</script>
