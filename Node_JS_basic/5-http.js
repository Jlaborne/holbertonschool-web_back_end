const http = require('http');
const fs = require('fs');
const { parse } = require('csv-parse');

// Function to count and list students from the CSV file
function countStudents(database) {
  return new Promise((resolve, reject) => {
    const students = {};
    let totalStudents = 0;

    fs.readFile(database, (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const parser = parse(data, { delimiter: ',', from_line: 2 });
      parser.on('data', (row) => {
        if (row.length > 1 && row[0].trim()) {
          const field = row[3];
          if (!students[field]) {
            students[field] = [];
          }
          students[field].push(row[0]);
          totalStudents++;
        }
      });

      parser.on('end', () => {
        let output = `Number of students: ${totalStudents}\n`;
        for (const [field, names] of Object.entries(students)) {
          output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
        }
        resolve(output.trim());
      });

      parser.on('error', (error) => reject(error));
    });
  });
}

// Create the HTTP server
const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.writeHead(200);
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const database = process.argv[2];
    countStudents(database)
      .then((output) => {
        res.writeHead(200);
        res.end(`This is the list of our students\n${output}`);
      })
      .catch((err) => {
        res.writeHead(500);
        res.end(err.message);
      });
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

// Listen on port 1245
app.listen(1245);

// Export the app variable
module.exports = app;
