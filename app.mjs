// import {age,name} from "./new.mjs"

// console.log(age)
// console.log(name)

const http = require("http")

const server = http.createServer((req,res)=>{
    res.writeHead(200,{"content-type":"text/html"})
})