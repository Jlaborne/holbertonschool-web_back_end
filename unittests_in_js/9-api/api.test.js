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
  const baseUrl = "http://localhost:7865";

  it("should return 200 and correct message when id is a number", function (done) {
    request.get(`${baseUrl}/cart/12`, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal("Payment methods for cart 12");
      done();
    });
  });

  it("should return 404 when id is NOT a number", function (done) {
    request.get(`${baseUrl}/cart/hello`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it("should return 404 when id is missing", function (done) {
    request.get(`${baseUrl}/cart/`, (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
});
