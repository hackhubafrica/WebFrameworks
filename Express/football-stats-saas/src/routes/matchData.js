const express = require('express');
const router = express.Router();
const axios = require('axios');

const API_ENDPOINT = 'https://sportapi7.p.rapidapi.com/api/v1/event/xdbsZdb/h2h/events';
const API_KEY = '99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699';

router.get('/match-data', async (req, res) => {
    try {
        const response = await axios.get(API_ENDPOINT, {
            headers: { 'x-rapidapi-key': API_KEY, 'x-rapidapi-host': 'sportapi7.p.rapidapi.com' }
        });
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching match data:', error.message);
        res.status(500).json({ error: 'Failed to fetch match data' });
    }
});





// Route to fetch odds providers
router.get('/odds/providers', async (req, res) => {
    try {
        const response = await axios.get('https://sportapi7.p.rapidapi.com/api/v1/odds/providers/DE/app', {
            headers: {
                'x-rapidapi-key': API_KEY,
                'x-rapidapi-host': API_HOST
            }
        });
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching odds providers:', error.message);
        res.status(500).json({ error: 'Failed to fetch odds providers' });
    }
});


// Route to fetch player data
router.get('/player/:playerId', async (req, res) => {
    const { playerId } = req.params; // Extract player ID from request parameters
    try {
        const response = await axios.get(`https://sportapi7.p.rapidapi.com/api/v1/player/${playerId}`, {
            headers: {
                'x-rapidapi-key': API_KEY,
                'x-rapidapi-host': API_HOST
            }
        });
        res.json(response.data);
    } catch (error) {
        console.error('Error fetching player data:', error.message);
        res.status(500).json({ error: 'Failed to fetch player data' });
    }
});

module.exports = router;