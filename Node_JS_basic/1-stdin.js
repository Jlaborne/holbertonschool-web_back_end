// Display the welcome message
console.log('Welcome to Holberton School, what is your name?');

// Read from stdin
process.stdin.on('data', (input) => {
  const name = input.toString().trim(); // Get the input and remove any extra spaces/newlines

  // Output the user's name
  console.log(`Your name is: ${name}`);

  // Check if the input is coming from echo (piped input) or interactive terminal
  if (process.stdin.isTTY) {
    process.exit(); // Exit for interactive mode
  } else {
    console.log('This important software is now closing');
    process.exit(); // Exit for piped input
  }
});
