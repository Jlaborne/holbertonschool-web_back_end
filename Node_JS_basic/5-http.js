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
        if (row.length > 1 && row[0].trim() && row[3].trim()) {
          const field = row[3].trim();
          if (!students[field]) {
            students[field] = [];
          }
          students[field].push(row[0].trim());
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
      const responseText = 'Hello Holberton School!';
      res.setHeader('Content-Length', responseText.length);
      res.writeHead(200);
      res.end(responseText);
    } else if (req.url === '/students') {
      const database = process.argv[2];
      if (!database) {
        res.writeHead(500);
        res.end('Database not provided');
        return;
      }
      countStudents(database)
        .then((output) => {
          const responseText = `This is the list of our students\n${output}`;
          res.setHeader('Content-Length', responseText.length);
          res.writeHead(200);
          res.end(responseText);
        })
        .catch((err) => {
          res.writeHead(500);
          res.end('Cannot load the database');
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
