const http = require("http");

const server = http.createServer((req, res) => {
    res.write("server created");
    res.end();
});

server.listen(3000, () => {
    console.log("Server running at http://");
});