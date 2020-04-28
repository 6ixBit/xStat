import express from "express"
import axios from "axios"
import fetch from "node-fetch"

const app = express()
app.use(express.json())

// Available services
const services = {
    "frontend-service": "http://localhost:8080/",
    "general-service": "http://localhost:8081/api/v1/stats/leagues",
    "player-comparison-service": "http://localhost:8082/api/v1/players/J. Milner"
}

// @desc Endpoints for server
app.get("/monitor", async (req, res) => {

    var monitoredServices = {} 
    try {
        for (let serviceName in services) {
            let serviceURL = services[serviceName]

            const result = await pingService(serviceURL)
            monitoredServices[serviceName] = result
        }
        res.status(200).json(monitoredServices)
    } catch(err) {
        console.log(err)
    }
})

// @desc Ping other services.
async function pingService (url) {

    try {
        const response = await axios.get(url)
    
        if(response.status == 200) {
            return "up"
        } else {
            return "down" 
        }  
    } catch (err) {
        console.log(err)
        return "down"
    }
 }

app.listen(5001, () => {console.log(`Listening on port: 5000`)})