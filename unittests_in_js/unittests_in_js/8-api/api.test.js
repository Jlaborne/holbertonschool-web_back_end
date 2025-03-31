const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
  const url = 'http://localhost:7865';

  it('should return status 200', function (done) {
    request.get(url, (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      done();
    });
  });

  it('should return correct message', function (done) {
    request.get(url, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});