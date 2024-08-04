const express = require('express');
const router = express.Router();
const axios = require('axios');

const API_KEY = '99752ab9cdmsh02e55e45c9b765bp1d045djsne4cb4cb79699';
const API_HOST = 'sportapi7.p.rapidapi.com';

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
