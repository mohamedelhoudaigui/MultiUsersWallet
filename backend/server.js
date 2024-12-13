const express =  require('express');
const { init } = require('./eth.js');

init()

const app = express();

app.get('/api', (req, res) => {
  res.json({ message: 'Hello, world!' });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});


