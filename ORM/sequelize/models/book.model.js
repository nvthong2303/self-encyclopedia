const { Sequelize, DataTypes } = require("sequelize");

const sequelize = new Sequelize("test", "root", "thong2303", {
  host: "127.0.0.1",
  dialect: "mysql",
});

const Book = sequelize.define("books", {
  title: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  author: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  release_date: {
    type: DataTypes.DATEONLY,
  },
  subject: {
    type: DataTypes.INTEGER,
  },
});

// sequelize
//   .sync()
//   .then(() => {
//     console.log("Book table created successfully!");

//     Book.create({
//       title: "Clean code",
//       author: "Robert C. Martin",
//       release_date: "2008-08-11",
//       subject: 1,
//     })
//       .then((res) => {
//         console.log("Book created successfully!", res);
//       })
//       .catch((err) => {
//         console.log("Error: ", err);
//       });
//   })
//   .catch((error) => {
//     console.error("Unable to create table : ", error);
//   });

sequelize
  .sync()
  .then(() => {
    Book.findOne({
      where: {
        id: "1",
      },
    })
      .then((res) => {
        console.log(res);
      })
      .catch((error) => {
        console.error("Failed to retrieve data : ", error);
      });
  })
  .catch((error) => {
    console.error("Unable to create table : ", error);
  });
