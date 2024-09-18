const http = require('http');
const { readFile } = require('fs').promises;
const { argv } = process;

const countStudents = async (path) => {
  try {
    const data = await readFile(path, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    const students = lines.slice(1);
    
    const fields = {};
    students.forEach(student => {
      const [firstName, , , field] = student.split(',');
      if (!fields[field]) fields[field] = [];
      fields[field].push(firstName);
    });

    let output = `Number of students: ${students.length}\n`;
    for (const [field, names] of Object.entries(fields)) {
      output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }
    return output.trim();
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const databasePath = argv[2];
      const studentsInfo = await countStudents(databasePath);
      res.end(`This is the list of our students\n${studentsInfo}`);
    } catch (error) {
      res.end(`This is the list of our students\n${error.message}`);
    }
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server running on port 1245');
});

module.exports = app;