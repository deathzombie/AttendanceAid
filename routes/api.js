// routes/api.js

const express = require('express');
const router = express.Router();
const Student = require('../models/student');

// POST request to save student data
router.post('/students', async(req, res) => {
    try {
        const { name, rollNumber } = req.body;

        const student = new Student({
            name,
            rollNumber,
        });

        await student.save();

        res.status(201).json(student);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'An error occurred' });
    }
});

module.exports = router;
