from unittest import mock
import unittest

import classes


class TestCalculator(unittest.TestCase):

    def test_sum_3_to_number(self):
        calculator = classes.Calculator()
        self.assertEqual(calculator.sum_3_to_number(3), 6, "Should be 6")

    @mock.patch('classes.Calculator._get_number_3')
    def test_mocked_sum_3_to_number(self, _get_number_3):
        _get_number_3.return_value = 4
        calculator = classes.Calculator()
        self.assertEqual(calculator.sum_3_to_number(3), 7, "Should be 7")


if __name__ == '__main__':
    unittest.main()

