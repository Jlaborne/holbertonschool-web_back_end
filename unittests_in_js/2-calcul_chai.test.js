const { expect } = require("chai");
const calculateNumber = require("./2-calcul_chai");

describe("calculateNumber", function () {
  describe("type SUM", function () {
    it("should return 4 when a = 1 and b = 3", function () {
      expect(calculateNumber("SUM", 1, 3)).to.equal(4);
    });

    it("should return 5 when a = 1.4 and b = 3.6", function () {
      expect(calculateNumber("SUM", 1.4, 3.6)).to.equal(5);
    });

    it("should return 6 when a = 1.5 and b = 3.6", function () {
      expect(calculateNumber("SUM", 1.5, 3.6)).to.equal(6);
    });
  });

  describe("type SUBTRACT", function () {
    it("should return -2 when a = 1 and b = 3", function () {
      expect(calculateNumber("SUBTRACT", 1, 3)).to.equal(-2);
    });

    it("should return -3 when a = 1.4 and b = 3.6", function () {
      expect(calculateNumber("SUBTRACT", 1.4, 3.6)).to.equal(-3);
    });

    it("should return -3 when a = 1.4 and b = 3.7", function () {
      expect(calculateNumber("SUBTRACT", 1.4, 3.7)).to.equal(-3);
    });
  });

  describe("type DIVIDE", function () {
    it("should return 0.25 when a = 1 and b = 3.6", function () {
      expect(calculateNumber("DIVIDE", 1, 3.6)).to.equal(0.25);
    });

    it("should return 1 when a = 1 and b = 1.4", function () {
      expect(calculateNumber("DIVIDE", 1, 1.4)).to.equal(1);
    });

    it("should return 'Error' when a = 1 and b = 0.3 (rounded to 0)", function () {
      expect(calculateNumber("DIVIDE", 1, 0.3)).to.equal("Error");
    });
  });

  describe("unsupported type", function () {
    it("should throw an error", function () {
      expect(() => calculateNumber("MULTIPLY", 1, 2)).to.throw("Unsupported type");
    });
  });
});
