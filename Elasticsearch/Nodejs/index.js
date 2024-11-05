const elasticsearch = require("elasticsearch");
const client = new elasticsearch.Client({
  host: "localhost:9200",
});

client.ping(
  {
    requestTimeout: 3000,
  },
  (err, res, sta) => {
    if (err) {
      return console.error(`Error connect:::`, err);
    }
    console.log(`isOkay::: connect`);
  }
);

// client.indices.create(
//   {
//     index: "player-index",
//   },
//   (err, res, sta) => {
//     console.log(`err, res, sta:::`, err, res, sta);
//   }
// );

// client.index(
//   {
//     index: "player-index",
//     id: 1,
//     type: "player-list",
//     body: {
//       name: "ronaldo",
//       age: 35,
//       club: "MU",
//     },
//   },
//   (err, res, sta) => {
//     console.log(`err, res, sta:::`, err, res, sta);
//   }
// );

// client.search(
//   {
//     index: "player-index",
//     type: "player-list",
//     body: {
//       query: {
//         match: {
//           name: "ronaldo",
//         },
//       },
//     },
//   },
//   (err, res, sta) => {
//     // console.log(`err, res, sta:::`, err, res, sta);
//     console.log(res.hits.hits);
//   }
// );

let bulk = [];

cities.forEach((city) => {
  bulk.push({
    index: {
      _index: "city_index01", // index
      _type: "city_list01", // type
    },
  });
  bulk.push(city);
});

client.bulk(
  {
    body: bulk,
  },
  (err, res, sta) => {
    console.log(`err, res, sta::`, cities.length);
  }
);
