// Import HTTP module
const http = require('http');

// Define port number
const PORT = 3000; 

// Create HTTP server
const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('Hello World! This is a Node.js HTTP Server');
    res.end();
});

// Start server
server.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
