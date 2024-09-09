const Pool = require("pg-pool")

const pool = new Pool({
    user: 'postgres',
    host: '127.0.0.1',
    database: 'connect_pool',
    password: 'changeme',
    port: 5432,
    max: 20, // số lượng kết nối tối đa trong pool 
    idleTimeoutMillis: 30000, // thời gian một máy khách được phép ở trạng thái nhàn rỗi trước khi bị đóng 
    connectionTimeoutMillis: 2000, // thời gian chờ để thiết lập kết nối
});

pool.query('SELECT * FROM users WHERE id = $1', [1],
    (err, res) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log("==>", res.rows[0]);
    });
