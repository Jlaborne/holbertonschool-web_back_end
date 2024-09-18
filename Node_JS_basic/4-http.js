const http = require('http');

// Create the HTTP server
const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain'); // Set content type as plain text
  res.statusCode = 200; // Set the status code to 200 OK
  res.end('Hello Holberton School!'); // Response body
});

// Make the server listen on port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Export the app variable
module.exports = app;
