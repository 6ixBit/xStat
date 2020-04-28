<template>
   <div>

     <b-row align-h="center" align-v="center">
        <b-col cols="12" md="8" >  
            <div class="header">
                <h1>Monitor</h1>
                <p>{{ setTableData }}</p>
                <b-table striped hover :items="setTableData"></b-table>
            </div> 
        </b-col>
      </b-row>

   </div> 
</template>
 
<script>
import axios from "axios"

export default {
    async created() {
       try {
           await pingServices()
       } catch (err) {
           console.log(err)
       }
    },
    data() {
        return {
            serviceStatus: {}
        }
    },
    methods: {
        async pingServices() {
            try {
                const result = await axios.get("http://localhost:8083/monitor")
                this.serviceStatus = result        
            } catch (err) {
                console.log(err)
            }
       } 
    },
    computed: {
        setTableData() { 
            let formattedServices = []

            for (let service in this.serviceStatus) {
                formattedServices.push({
                    "Service": service,
                    "Status" : this.serviceStatus[service] 
                })
            }
            return formattedServices 
        }
    }
}
</script>

<style scoped>
    .header{
        display: flex;
        justify-content: center;
    }
</style>





