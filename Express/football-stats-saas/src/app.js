const express = require('express');
const cors = require('cors');
const app = express();
const matchDataRoute = require('./routes/matchData');
const playerDataRoute = require('./routes/playerData');
app.use(cors());  // Enable CORS
app.use('/api', matchDataRoute);
app.use('/api', playerDataRoute); // Add the new route
module.exports = app;



