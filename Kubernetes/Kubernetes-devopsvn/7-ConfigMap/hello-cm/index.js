const http = require("http");
const { Client } = require("pg");

const { DB_HOST, POSTGRES_USER, POSTGRES_DB, POSTGRES_PASSWORD } = process.env;

const client = new Client({
    host: DB_HOST,
    user: POSTGRES_USER,
    database: POSTGRES_DB,
    password: POSTGRES_PASSWORD,
    port: 5432,
});
client.connect().then(() => {
    console.log("connect db successfully");
})

const server = http.createServer((req, res) => {
    console.log("Hello env\n")
});

server.listen(process.env.PORT, () => {
    console.log("Server listen on port ", process.env.PORT)
})
