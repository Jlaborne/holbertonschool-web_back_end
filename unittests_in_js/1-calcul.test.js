const assert = require("assert");
const calculateNumber = require("./1-calcul");

describe("calculateNumber", function () {
  describe("type SUM", function () {
    it("should return 4 when a = 1 and b = 3", function () {
      assert.strictEqual(calculateNumber("SUM", 1, 3), 4);
    });

    it("should return 5 when a = 1.4 and b = 3.6", function () {
      assert.strictEqual(calculateNumber("SUM", 1.4, 3.6), 5);
    });

    it("should return 6 when a = 1.5 and b = 3.6", function () {
      assert.strictEqual(calculateNumber("SUM", 1.5, 3.6), 6);
    });
  });

  describe("type SUBTRACT", function () {
    it("should return -2 when a = 1 and b = 3", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 1, 3), -2);
    });

    it("should return -2 when a = 1.4 and b = 3.6", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 3.6), -3);
    });

    it("should return -3 when a = 1.4 and b = 3.7", function () {
      assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 3.7), -3);
    });
  });

  describe("type DIVIDE", function () {
    it("should return 0.25 when a = 1 and b = 3.6", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 1, 3.6), 0.25);
    });

    it("should return 0.5 when a = 1 and b = 1.4", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 1, 1.4), 1);
    });

    it("should return Error when a = 1 and b = 0.3 (rounded to 0)", function () {
      assert.strictEqual(calculateNumber("DIVIDE", 1, 0.3), "Error");
    });
  });

  describe("Unsuported type", function () {
    it("should throw an error", function () {
      assert.throws(() => calculateNumber("MULTIPLY", 1, 2), "Unsuported type");
    });
  });
});
