const express = require('express');

const serveStatic = require('serve-static');

const path = require('path');



app = express();

app.use(serveStatic(path.join(__dirname, 'dist')));

app.use('/robots.txt', express.static(path.join(__dirname, 'dist/public/robots.txt')));

app.use('/sitemap.xml', express.static(path.join(__dirname, 'dist/public/sitemap.xml')));

const port = process.env.PORT || 80;

app.listen(port);