const mongoose = require('mongoose');

const DB_URL = 'mongodb://localhost:27017/mydatabase'; // Replace with your DB URL

mongoose.connect(DB_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

module.exports = db;
