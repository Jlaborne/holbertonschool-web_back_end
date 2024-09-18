// Display the initial message
console.log('Welcome to Holberton School, what is your name?');

// Event listener for when the user inputs their name
process.stdin.on('data', (input) => {
  const name = input.toString().trim();
  console.log(`Your name is: ${name}`);

  // Close the input stream to allow the program to finish
  process.stdin.end();
});

// Event listener for when the input stream is closed (when the user ends the program)
process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
