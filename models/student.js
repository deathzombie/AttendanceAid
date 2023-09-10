// models/student.js
//This is where we create a schema in order show how we are going to store values of the data we are inputing.
// *using MongoDB for backend
const mongoose = require('mongoose');

const studentSchema = new mongoose.Schema({
    name: String,
    rollNumber: String,
    LMSID: String,
    LMSPassword: String,
    SubGroup: String

    // Add more fields as needed
});

module.exports = mongoose.model('Student', studentSchema);
