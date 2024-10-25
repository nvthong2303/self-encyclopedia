const grpc = require("@grpc/grpc-js")
const PROTO_PATH = "./news.proto"
const protoLoader = require("@grpc/proto-loader")

const options = {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
}

var packageDefinition = protoLoader.loadSync(PROTO_PATH, options)
const newService = grpc.loadPackageDefinition(packageDefinition).NewsService;

const client = new newService(
    "localhost:50051",
    grpc.credentials.createInsecure()
)

client.getAllNews({}, (err, news) => {
    if (!err) {
        console.log("get all news: ", news)
    } else {
        console.error("errrrrrrr : ", err)
    }
})

client.getNewsById({ id: "1" }, (err, news) => {
    if (!err) {
        console.log("get news id = 1 :", news)
    } else {
        console.error("errrrrrrr : ", err)
    }
})
