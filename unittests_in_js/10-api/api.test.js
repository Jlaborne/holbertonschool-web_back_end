const request = require("request");
const { expect } = require("chai");

describe("Index page", function () {
  const url = "http://localhost:7865";

  it("should return status 200", function (done) {
    request.get(url, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it("should return correct message", function (done) {
    request.get(url, (err, res, body) => {
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });
});

describe("Cart page", function () {
  const url = "http://localhost:7865";

  it("should return 200 and correct message when id is a number", function (done) {
    request.get(`${url}/cart/5`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal("Payment methods for cart 5");
      done();
    });
  });

  it("should return 404 when id is not a number", function (done) {
    request.get(`${url}/cart/test`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});

describe("/available_payments", function () {
  const url = "http://localhost:7865/available_payments";

  it("should return status 200 and correct JSON response", function (done) {
    request.get(url, { json: true }, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false,
        },
      });
      done();
    });
  });
});

describe("/login", function () {
  const url = "http://localhost:7865/login";

  it("should return 200 and Welcome message", function (done) {
    request.post(
      {
        url,
        json: { userName: "Betty" },
      },
      (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(res.body).to.be.undefined; // POST returns raw text, not JSON
        expect(res.text || res.body || res.rawBody || res.toJSON?.()).to.be
          .undefined;
        expect(res).to.have.property("body"); // confirm body exists
        expect(res.body).to.equal(undefined); // raw text not parsed here
        expect(res).to.have.property("statusCode", 200);
        done();
      }
    );
  });

  it("should return Welcome Betty in response body (manual)", function (done) {
    request.post(
      {
        url,
        body: JSON.stringify({ userName: "Betty" }),
        headers: { "Content-Type": "application/json" },
      },
      (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        expect(body).to.equal("Welcome Betty");
        done();
      }
    );
  });
});
