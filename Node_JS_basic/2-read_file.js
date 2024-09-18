const fs = require('fs')

function countStudents (path) {
  try {
    const data = fs.readFileSync(path, 'utf8')

    // Split the file content by lines
    const lines = data.trim().split('\n')

    if (lines.length <= 1) {
      throw new Error('Cannot load the database')
    }

    const students = lines.slice(1).map((line) => line.split(',')).filter((fields) => fields.length === 4)

    const studentCount = students.length
    console.log(`Number of students: ${studentCount}`)

    const fields = {}

    students.forEach((student) => {
      const field = student[3]
      const firstName = student[0]

      if (!fields[field]) {
        fields[field] = []
      }
      fields[field].push(firstName)
    })
    for (const field in fields) {
      const list = fields[field]
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`)
    }
  } catch (err) {
    throw new Error('Cannot load the database')
  }
}

module.exports = countStudents
