from unittest import TestCase
from .functions import divide, multiply

"""
To run it from VSCode: 
```python -B -m unittest src.v2.testing.test_functions```
"""


class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        # self.assertEqual(divide(dividend, divisor), expected_result)
        self.assertAlmostEqual(
            divide(dividend, divisor), expected_result
        )  # in case .999999999....

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        expected_result = 0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_error_by_zero(self):
        # both are equivalent:
        # alt.1
        with self.assertRaises(ValueError):
            divide(25, 0)
        # alt.2 (lambda because it has arguments)
        self.assertRaises(ValueError, lambda: divide(25, 0))
        # alt.3 (if function doesn't have args)
        # self.assertRaises(ValueError, lambda: divide)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected = 8
        self.assertEqual(multiply(expected), expected)

    def test_multiply_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)

    def test_multiply_result(self):
        inputs = (3, 5, 1)
        expected = 15
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_result_with_zero(self):
        inputs = (3, 5, 0)
        expected = 0
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_negative(self):
        inputs = (3, -5, 2)
        expected = -30
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_floats(self):
        inputs = (3.0, 2)
        expected = 6.0
        self.assertEqual(multiply(*inputs), expected)
