from unittest import TestCase
from unittest.mock import patch

from src.main import RunRaiseException
from src.main import CustomError


class TestMockException(TestCase):
    def test_catch_method_exception(self):
        is_catched = False
        try:
            RunRaiseException().raise_file_exists_error()
        except FileExistsError:
            is_catched = True
        self.assertTrue(is_catched)

    @patch("src.main.RunRaiseException.raise_file_exists_error")
    def test_catch_mocked_exception(self, mock_raise_exception):
        is_catched = False
        mock_raise_exception.side_effect = ValueError
        try:
            RunRaiseException().raise_file_exists_error()
        except ValueError:
            is_catched = True
        self.assertTrue(is_catched)

    def test_catch_custom_exception(self):
        is_catched = False
        try:
            RunRaiseException().raise_custom_error()
        except CustomError:
            is_catched = True
        self.assertTrue(is_catched)

    @patch("src.main.RunRaiseException.raise_file_exists_error")
    def test_catch_mocked_custom_exception(self, mock_raise_exception):
        is_catched = False
        mock_raise_exception.side_effect = CustomError
        try:
            RunRaiseException().raise_file_exists_error()
        except CustomError:
            is_catched = True
        self.assertTrue(is_catched)
