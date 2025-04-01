const express = require("express");
const app = express();
const port = 7865;

// Middleware pour parser les body JSON
app.use(express.json());

app.get("/", (req, res) => {
  res.send("Welcome to the payment system");
});

app.get("/cart/:id(\\d+)", (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}`);
});

app.get("/available_payments", (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

app.post("/login", (req, res) => {
  const { userName } = req.body;

  if (userName) {
    res.send(`Welcome ${userName}`);
  } else {
    res.status(400).send("Missing userName");
  }
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
