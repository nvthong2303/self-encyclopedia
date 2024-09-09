import pg from 'pg'
const { Pool } = pg 

const pool = new Pool({
    user: 'postgres',
    host: '127.0.0.1',
    database: 'connect_pool',
    password: 'changeme',
    port: 5432,
    max: 20, // số lượng kết nối tối đa trong pool 
    idleTimeoutMillis: 30000, // thời gian một máy khách được phép ở trạng thái nhàn rỗi trước khi bị đóng 
    connectionTimeoutMillis: 2000, // thời gian chờ để thiết lập kết nối
})

const result = await pool.query('SELECT * FROM users WHERE id = $1', [1])
console.log(result.rows[0].name)