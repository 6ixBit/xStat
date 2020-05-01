import express from "express"
import axios from "axios"
import cors from "cors"

const app = express()
app.use(express.json())
app.use(cors())

// Available services
const services = {
    "frontend-service": "http://frontend:8080/",
    "general-service": "http://general-service:8081/api/v1/stats/leagues/",
    "player-comparison-service": "http://player-comparison-service:8082/api/v1/players/J. Milner/"
}

// @desc Endpoints for server
app.get("/monitor", cors(), async (req, res) => {

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
            return "Up"
        } else {
            return "Down" 
        }  
    } catch (err) {
        console.log(err)
        return "Down"
    }
 }

app.listen(5000, () => {console.log(`Listening on port: 5000`)})