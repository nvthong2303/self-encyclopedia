const express = require('express');
const mongoose = require('mongoose');
const redis = require('redis');

mongoose.connect('mongodb://mongo-service:27017/myapp', { useNewUrlParser: true, useUnifiedTopology: true });

const client = redis.createClient(6379, 'redis-service');

const app = express();

app.get('/', (req, res) => {
    res.send('Hello World!');
});

app.get('/users', (req, res) => {
    res.json({ message: 'Get users from MongoDB' });
});

app.post('/cache', (req, res) => {
    res.json({ message: 'Data cached in Redis' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});