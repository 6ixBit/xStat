import express from "express"
import axios from "axios";
import fetch from "node-fetch"

const app = express()

// Available services
const services = {
    "frontend-service": "http://google.com",
    "general-service": "http://amazon.com",
    "player-comparison-service": "http://facebook.com"
}

// @desc Endpoints fr server
app.get("/monitor", (req, res) => {

    var monitoredServices = {} 

    for (let serviceName in services) {
        let serviceURL = services[serviceName]

        const result = pingService(serviceURL)
        monitoredServices[serviceName] = result || false // Undefined, for some reason?
    }

    res.status(200).json(monitoredServices)
})

// @desc Ping other services.
function pingService (url) {
    fetch(url)
    .then( (response) => {
        if(response.status == 200) {
            return { url: true }
        } else {
            return { url: false }
        } 
    })
    .catch( (err) => {console.log(err)})
 }

app.listen(5000, () => {console.log(`Listening on port: 5000`)})