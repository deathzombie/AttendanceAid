const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const db = require('./config/db');
const apiRoutes = require('./routes/api');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/thankyou', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'thankyou.html'));
});

app.use('/api', apiRoutes);

// Store data locally
app.post('/store', (req, res) => {
    const { name, rollNumber } = req.body;

    // Create a data object
    const data = {
        name,
        rollNumber,
        lmsId,
        lmsPassword,
        branch,
        subgroup
        // Add more fields as needed
    };

    // Convert data to JSON
    const jsonData = JSON.stringify(data);

    // Define the file path to store the data
    const filePath = path.join(__dirname, 'data.json');

    // Write data to the file
    fs.writeFile(filePath, jsonData, (err) => {
        if (err) {
            console.error(err);
            res.status(500).json({ error: 'An error occurred' });
        } else {
            res.redirect('/thankyou');
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
