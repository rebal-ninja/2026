const http = require("http");

const server = http.createServer((req,res)=>{
    if (req.url === "/"){
        res.write("welcome to the home page");
    }
    else if (req.url === "/about"){
        res.write("about page")
    }
    else{
        res.write("404 page not found -_-");
    }
    res.end();
})


server.listen(3000)