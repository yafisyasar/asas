const http = require('http');

const PORT = 3000; 

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello World! This is a Node.js HTTP Server');
    res.end();
});

server.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
