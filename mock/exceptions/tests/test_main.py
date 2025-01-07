from unittest import TestCase
from unittest.mock import patch

from src.exceptions import CustomError as CustomError_exceptions
from src.main import _RunRaiseException
from src.main import CustomError as CustomError_main
from src.main import run_catch_exception


class CustomError_test(ZeroDivisionError):
    pass


class TestIsinstance(TestCase):
    def test_isinstance_for_all_classes(self):
        assert isinstance(CustomError_exceptions(), CustomError_exceptions)
        assert isinstance(CustomError_main(), CustomError_exceptions)
        assert not isinstance(CustomError_test(), CustomError_exceptions)


class Test_run_catch_exceptions(TestCase):
    def test_exception_is_catched(self):
        self.assertEqual("Catched FileExistsError!", run_catch_exception())

    @patch("src.main._RunRaiseException.run")
    def test_exception_is_catched_if_mocked(self, mock_raise_exception):
        mock_raise_exception.side_effect = ValueError
        self.assertEqual("Catched ValueError!", run_catch_exception())

    @patch("src.main._RunRaiseException.run")
    def test_exception_is_catched_if_mocked_with_custom_error(self, mock_raise_exception):
        mock_raise_exception.side_effect = CustomError_exceptions
        self.assertEqual("Catched CustomError!", run_catch_exception())


class TestRunRaiseException(TestCase):
    def test_catch_method_exception(self):
        is_catched = False
        try:
            _RunRaiseException().run()
        except FileExistsError:
            is_catched = True
        self.assertTrue(is_catched)

    @patch("src.main._RunRaiseException.run")
    def test_catch_mocked_exception_with_built_in_exception(self, mock_raise_exception):
        is_catched = False
        mock_raise_exception.side_effect = ValueError
        try:
            _RunRaiseException().run()
        except ValueError:
            is_catched = True
        self.assertTrue(is_catched)

    @patch("src.main._RunRaiseException.run")
    def test_catch_mocked_exception_with_custom_exception(self, mock_raise_exception):
        is_catched = False
        mock_raise_exception.side_effect = CustomError_exceptions
        try:
            _RunRaiseException().run()
        except CustomError_exceptions:
            is_catched = True
        self.assertTrue(is_catched)
