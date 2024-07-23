export default function updateStudentGradeByCity(students, city, newGrades) {
  // Filter students by the specified city
  const studentsInCity = students.filter((student) => student.location === city);

  // Map over the filtered students to update their grades
  const updatedStudents = studentsInCity.map((student) => {
    // Find the grade for the current student
    const studentGrade = newGrades.find((grade) => grade.studentId === student.id);

    // If a grade is found, use it; otherwise, assign 'N/A'
    const grade = studentGrade ? studentGrade.grade : 'N/A';

    // Return a new student object with the updated grade
    return {
      ...student,
      grade,
    };
  });

  // Return the array of updated students
  return updatedStudents;
}
