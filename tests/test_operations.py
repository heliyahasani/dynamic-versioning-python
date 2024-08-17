import unittest
from trial.calculator.operations import sum, sub, mul, div


class TestOperations(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-1, -1), -2)

    def test_sub(self):
        self.assertEqual(sub(2, 1), 1)
        self.assertEqual(sub(2, 2), 0)
        self.assertEqual(sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(-1, -1), 1)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-10, -2), 5)
        self.assertEqual(div(-10, 2), -5)
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)


if __name__ == "__main__":
    unittest.main()
