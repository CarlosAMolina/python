from unittest import TestCase
from unittest.mock import patch

from src.exceptions import CustomError as ExceptionsCustomError
from src.main import _RunRaiseException
from src.main import RelativeImportCustomError as MainRelativeImportCustomError
from src.main import run_catch_exception


class Test_run_catch_exceptions(TestCase):
    def test_exception_is_catched(self):
        self.assertEqual("Catched FileExistsError!", run_catch_exception())

    @patch("src.main._RunRaiseException.run")
    def test_exception_is_catched_if_mocked(self, mock_raise_exception):
        mock_raise_exception.side_effect = ValueError
        self.assertEqual("Catched ValueError!", run_catch_exception())

    @patch("src.main._RunRaiseException.run")
    def test_exception_is_catched_if_mocked_with_custom_error_absolute_import(self, mock_raise_exception):
        mock_raise_exception.side_effect = ExceptionsCustomError
        self.assertEqual("Catched AbsoluteImportCustomError!", run_catch_exception())

    @patch("src.main._RunRaiseException.run")
    def test_exception_is_catched_if_mocked_with_custom_error_relative_import(self, mock_raise_exception):
        mock_raise_exception.side_effect = MainRelativeImportCustomError
        self.assertEqual("Catched RelativeImportCustomError!", run_catch_exception())


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
        mock_raise_exception.side_effect = ExceptionsCustomError
        try:
            _RunRaiseException().run()
        except ExceptionsCustomError:
            is_catched = True
        self.assertTrue(is_catched)
