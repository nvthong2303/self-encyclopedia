const grpc = require("@grpc/grpc-js");
const PROTO_PATH = "./news.proto";
var protoLoader = require("@grpc/proto-loader");

const options = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
};

var packageDefinition = protoLoader.loadSync(PROTO_PATH, options);
const newsProto = grpc.loadPackageDefinition(packageDefinition);

const server = new grpc.Server();
let news = [
  { id: "1", title: "Note 1", body: "Content 1", postImage: "Post image 1" },
  { id: "2", title: "Note 2", body: "Content 2", postImage: "Post image 2" },
  { id: "3", title: "Note 3", body: "Content 3", postImage: "Post image 3" },
  { id: "4", title: "Note 4", body: "Content 4", postImage: "Post image 4" },
];

server.addService(newsProto.NewsService.service, {
  getAllNews: (_, callback) => {
    callback(null, { news: news });
  },
  getNewsById: (call, callback) => {
    const request = call.request;
    const foundNews = news.find((n) => n.id === request.id);
    if (foundNews) {
      callback(null, { news: foundNews });
    } else {
      callback({
        code: grpc.status.NOT_FOUND,
        details: "Not found",
      });
    }
  },
  addNews: (call, callback) => {
    const newNews = {
      id: (news.length + 1).toString(),
      ...call.request.news,
    };
    news.push(newNews);
    callback(null, { news: newNews });
  },
  editNews: (call, callback) => {
    const request = call.request;
    const foundIndex = news.findIndex((n) => n.id === request.news.id);
    if (foundIndex !== -1) {
      news[foundIndex] = request.news;
      callback(null, { news: request.news });
    } else {
      callback({
        code: grpc.status.NOT_FOUND,
        details: "Not found",
      });
    }
  },
  deleteNews: (call, callback) => {
    const request = call.request;
    const foundIndex = news.findIndex((n) => n.id === request.id);
    if (foundIndex !== -1) {
      news = news.filter((n) => n.id !== request.id);
      callback(null, {});
    } else {
      callback({
        code: grpc.status.NOT_FOUND,
        details: "Not found",
      });
    }
  },
});

server.bindAsync(
  "127.0.0.1:50051",
  grpc.ServerCredentials.createInsecure(),
  (error, port) => {
    console.log("Server running at http://127.0.0.1:50051");
    server.start();
  }
);
