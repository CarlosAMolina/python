from unittest import TestCase
from unittest.mock import patch

from classes import RunRaiseException

class TestMockException(TestCase):
    def test_catch_method_exception(self):
        is_catched = False
        try:
            RunRaiseException().raise_file_exists_error()
        except FileExistsError:
            is_catched = True
        self.assertTrue(is_catched)

    @patch("classes.RunRaiseException.raise_file_exists_error")
    def test_catch_mocked_exception(self, mock_raise_exception):
        is_catched = False
        mock_raise_exception.side_effect = ValueError
        try:
            RunRaiseException().raise_file_exists_error()
        except ValueError:
            is_catched = True
        self.assertTrue(is_catched)
