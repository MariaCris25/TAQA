import unittest
from Calculator import Calculator

class testSumFromNumbers(unittest.TestCase):
    def test_isCorect(self):
        calc = Calculator()
        result = calc.sumFromNumbers(2,3)
        expected = 5
        self.assertEqual(result,expected)


    def test_isNegative(self):
        calc = Calculator()
        result = calc.sumFromNumbers(-4,1)
        expected = 0
        self.assertLess(result,expected)


    def test_isGreater(self):
        calc = Calculator()
        result = calc.sumFromNumbers(2,3)
        expected = 5
        self.assertGreaterEqual(result,expected)

def suite():
    # gather all tests in a test suite

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(testSumFromNumbers))

    return test_suite

mySuite=suite()

#define Runner

runner=unittest.TextTestRunner()
runner.run(mySuite)
