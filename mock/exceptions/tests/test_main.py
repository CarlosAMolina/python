from unittest import TestCase
from unittest.mock import patch

from src.exceptions import CustomError
from src.main import _RunRaiseException
from src.main import CustomError as CustomError_main
from src.main import run_catch_exception


class CustomError_test(ZeroDivisionError):
    pass


class TestIsinstance(TestCase):
    def test_isinstance_for_all_classes(self):
        assert isinstance(CustomError(), CustomError)
        assert isinstance(CustomError_main(), CustomError)
        assert not isinstance(CustomError_test(), CustomError)


class Test_run_catch_exceptions(TestCase):
    def test_exception_is_catched(self):
        self.assertEqual("Catched FileExistsError!", run_catch_exception())

    @patch("src.main._RunRaiseException.raise_file_exists_error")
    def test_exception_is_catched_if_mocked(self, mock_raise_exception):
        mock_raise_exception.side_effect = ValueError
        self.assertEqual("Catched ValueError!", run_catch_exception())

    @patch("src.main._RunRaiseException.raise_file_exists_error")
    def test_exception_is_catched_if_mocked_with_custom_error(self, mock_raise_exception):
        mock_raise_exception.side_effect = CustomError
        self.assertEqual("Catched CustomError!", run_catch_exception())


class Test_RunRaiseException(TestCase):
    def test_catch_method_exception(self):
        is_catched = False
        try:
            _RunRaiseException().raise_file_exists_error()
        except FileExistsError:
            is_catched = True
        self.assertTrue(is_catched)

    @patch("src.main._RunRaiseException.raise_file_exists_error")
    def test_catch_mocked_exception(self, mock_raise_exception):
        is_catched = False
        mock_raise_exception.side_effect = ValueError
        try:
            _RunRaiseException().raise_file_exists_error()
        except ValueError:
            is_catched = True
        self.assertTrue(is_catched)

    def test_catch_custom_exception(self):
        is_catched = False
        try:
            _RunRaiseException().raise_custom_error()
        except CustomError:
            is_catched = True
        self.assertTrue(is_catched)

    @patch("src.main._RunRaiseException.raise_file_exists_error")
    def test_catch_mocked_custom_exception(self, mock_raise_exception):
        is_catched = False
        mock_raise_exception.side_effect = CustomError
        try:
            _RunRaiseException().raise_file_exists_error()
        except CustomError:
            is_catched = True
        self.assertTrue(is_catched)
