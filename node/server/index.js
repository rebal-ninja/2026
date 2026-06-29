const http = require("http");
const fs = require("fs");

const myserver = http.createServer((req, res) => {
    const log = `${Date.now()}: New Request Received\n`;

    fs.appendFile("log.txt", log, (err) => {
        if (err) {
            console.log(err);
        }
    });

    res.end("Hello from server");
});

myserver.listen(2001, () => {
    console.log("Server started");
});