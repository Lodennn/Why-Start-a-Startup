const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = '/Users/khalednasser/Documents/Lodenn/how-to-start-a-startup/book/site-ar';
const PORT = 8744;

const MIME = { '.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript', '.png': 'image/png', '.pdf': 'application/pdf' };

http.createServer((req, res) => {
  let filePath = path.join(ROOT, req.url === '/' ? '/index.html' : req.url);
  fs.readFile(filePath, (err, data) => {
    if (err) { res.writeHead(404); res.end('Not found'); return; }
    const ext = path.extname(filePath);
    res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
    res.end(data);
  });
}).listen(PORT, () => console.log(`Serving ${ROOT} on :${PORT}`));
