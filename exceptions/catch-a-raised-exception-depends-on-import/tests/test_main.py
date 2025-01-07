import unittest

from src.exceptions import FolderInS3UriError as FolderInS3UriError_exceptions
from src.main import CatchResults
from src.main import FolderInS3UriError_main


class FolderInS3UriError_test(FileExistsError):
    pass


class TestCatchExceptions(unittest.TestCase):
    def test_what_imports_can_catch_exceptions(self):
        for test_values in (
            (
                FolderInS3UriError_main,
                {"FolderInS3UriError_main"},
                {"FolderInS3UriError_exceptions", "FolderInS3UriError_test"},
            ),
            (
                FolderInS3UriError_exceptions,
                {"FolderInS3UriError_exceptions"},
                {"FolderInS3UriError_main", "FolderInS3UriError_test"},
            ),
            (
                FolderInS3UriError_test,
                {"FolderInS3UriError_test"},
                {"FolderInS3UriError_exceptions", "FolderInS3UriError_main"},
            ),
        ):
            exception_to_check, expected_catched, expected_not_catched = test_values
            exception_catcher_str_array = (
                "FolderInS3UriError_main",
                "FolderInS3UriError_exceptions",
                "FolderInS3UriError_test",
            )
            catch_results = self._get_what_imports_can_catch_the_exception(
                exception_to_check, exception_catcher_str_array
            )
            self.assertEqual(expected_catched, catch_results.catched)
            self.assertEqual(expected_not_catched, catch_results.not_catched)

    def _get_what_imports_can_catch_the_exception(
        self, exception_to_catch, exception_catcher_str_array
    ) -> CatchResults:
        return ExceptionCatchersClassifier(
            exception_catcher_str_array
        ).get_cathers_classified_by_can_catch_the_exception(exception_to_catch)


class ExceptionCatchersClassifier:
    def __init__(self, exception_catcher_str_array: tuple[str, ...]):
        self._exception_catcher_str_array = exception_catcher_str_array

    def get_cathers_classified_by_can_catch_the_exception(self, exception_to_catch) -> CatchResults:
        catch_results = CatchResults()
        for exception_catcher_str in self._exception_catcher_str_array:
            if ExceptionCatcherChecker(exception_catcher_str).can_catch_the_exception(exception_to_catch):
                catch_results.add_to_catched(exception_catcher_str)
            else:
                catch_results.add_to_not_catched(exception_catcher_str)
        return catch_results


class ExceptionCatcherChecker:
    def __init__(self, exception_catcher_str: str):
        self._exception_catcher = eval(exception_catcher_str)

    def can_catch_the_exception(self, exception_to_catch):
        try:
            raise exception_to_catch
        except self._exception_catcher:
            return True
        except:
            return False
