const app = require('./app');
const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

/*

app.get('/', (req, res) => {
    res.send('Hello, Football Stats SaaS!');
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

app.get('/api/match-data', (req, res) => {
    // Logic to fetch data from sports API
    res.json({ message: 'Match data endpoint' });
});
*/