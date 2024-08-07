const http = require("http");

const server = http.createServer((req, res) => {
    res.end("Hello application v2\n") // change v1 to v2
});

server.listen(3000, () => {
    console.log("Server listen on port 3000")
})
