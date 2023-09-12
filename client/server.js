// const express = require('express');

// const serveStatic = require('serve-static');

// const path = require('path');



// app = express();

// app.use(serveStatic(path.join(__dirname, 'dist')));

// app.use('/robots.txt', express.static(path.join(__dirname, 'dist/public/robots.txt')));

// app.use('/sitemap.xml', express.static(path.join(__dirname, 'dist/public/sitemap.xml')));

// const port = process.env.PORT || 80;

// app.listen(port);

const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http, {
    cors: {
        origins: []
    }
});

app.get('/', (req, res) => {
    res.send('<h1>Hey Socket.io</h1>');
});

// io.on('connection', (socket) => {
//     console.log('a user connected');
//     socket.on('disconnect', () => {
//         console.log('user disconnected');
//     });
// });
io.on('connection', (socket) => {
    console.log('a user connected');
});

io.on('chat', (socket) => {
    console.log('a user connected');
});

// io.on('connection', (socket) => {
//     socket.on('my message', (msg) => {
//         io.emit('my broadcast', `server: ${msg}`);
//     });
// });

io.on('connected', () => {
    console.log('a user connected');
});

http.listen(3000, () => {
    console.log('listening on *:3000');
});