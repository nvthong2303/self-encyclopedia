const http = require("http");

const server = http.createServer((req, res) => {
    console.log("Hello env\n")
});

server.listen(process.env.PORT, () => {
    console.log("Server listen on port ", process.env.PORT)
})
