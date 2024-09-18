const express = require('express');
const fs = require('fs');
const { parse } = require('csv-parse');

const app = express();
const PORT = 1245;

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
        if (row.length > 3 && row[0].trim() && row[3].trim()) {
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

// Middleware to set plain text response type
app.use((req, res, next) => {
  res.setHeader('Content-Type', 'text/plain');
  next();
});

// Route for '/'
app.get('/', (req, res) => {
  res.status(200).send('Hello Holberton School!');
});

// Route for '/students'
app.get('/students', (req, res) => {
  const database = process.argv[2];
  if (!database) {
    res.status(500).send('Database not provided');
    return;
  }

  countStudents(database)
    .then((output) => {
      res.status(200).send(`This is the list of our students\n${output}`);
    })
    .catch((err) => {
      res.status(500).send('Cannot load the database');
    });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

// Export the app variable
module.exports = app;
