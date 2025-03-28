// 0-calcul.test.js
const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
  it("should return 4 when a = 1 and b = 3", function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });

  it("should return 5 when a = 1 and b = 3.7", function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });

  it("should return 5 when a = 1.2 and b = 3.7", function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });

  it("should return 6 when a = 1.5 and b = 3.7", function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });

  it("should return 0 when a = 0.1 and b = 0.3", function () {
    assert.strictEqual(calculateNumber(0.1, 0.3), 0);
  });

  it("should return -4 when a = -1.4 and b = -2.6", function () {
    assert.strictEqual(calculateNumber(-1.4, -2.6), -4);
  });

  it("should return 1 when a = 0.5 and b = 0.4", function () {
    assert.strictEqual(calculateNumber(0.5, 0.4), 1);
  });

  it("should return 2 when a = 0.5 and b = 0.5", function () {
    assert.strictEqual(calculateNumber(0.5, 0.5), 2);
  });
});
