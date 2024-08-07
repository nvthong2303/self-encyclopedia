const http = require("http");

let requestCount = 0;

const server = http.createServer((req, res) => {
    if (++requestCount > 3) {
        res.writeHead(500); // set status code 500
        res.end("Application v3 have some internal error has occurred!\n");
        return;
    }

    res.end("Hello application v3\n");
});

server.listen(3000, () => {
    console.log("Server listen on port 3000")
})

