const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', function () {
  it('should return resolved promise with correct data when success is true', function (done) {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch(done); // en cas d'erreur, on passe l'erreur à Mocha
  });
});