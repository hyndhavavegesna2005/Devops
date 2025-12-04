import unittest
from main import Calculator

# assertEqual / NotEqual
# assertTrue / False
# assertIn / assertNotIn
# assertRaises
# assertGreater / Less
# assertGreaterThan / LessThan
# assertIsIn / NotIn

class TestCalc(unittest.TestCase):
    def setUp(self):
        print("Set up an instance before each test")
        self.calc = Calculator()

    def test_add(self):
        result = self.calc.add(1,2)
        self.assertEqual(result, 3)

    def test_sub(self):
        result = self.calc.sub(1,2)
        self.assertEqual(result, -1)

    def test_mul(self):
        result = self.calc.mul(1,2)
        self.assertEqual(result, 2)

    def test_div(self):
        result = self.calc.div(1,2)
        self.assertEqual(result, 0.5)

    def test_div_zero(self):
        with self.assertRaises( ValueError):
            self.calc.div(1,0)

    def tearDown(self):
        "Tear down an instance after each test"
        pass

if __name__ == '__main__':
    unittest.main()
