import unittest

from src.exceptions import FolderInS3UriError as FolderInS3UriError_exceptions
from src.main import CatchResults
from src.main import FolderInS3UriError_main


class FolderInS3UriError_test(FileExistsError):
    pass


class TestCatchExceptions(unittest.TestCase):
    def test_what_imports_can_catch_exceptions(self):
        """
        Why FolderInS3UriError_main cannot catch FolderInS3UriError_exceptions:
        - https://docs.python.org/3/tutorial/errors.html
        'A class in an except clause matches exceptions which are instances of the class itself or one of
        its derived classes'
        - stackoverflow.com/questions/11461356/issubclass-returns-false-on-the-same-class-imported-from-different-paths
        They aren't the same class. They were created with the same code, but since you executed that code twice
        (once in the import and once in load_module) you get two different class objects. issubclass is comparing
        the identities of the class objects and they're different.

        """
        assert isinstance(FolderInS3UriError_main(), FolderInS3UriError_main)
        assert not isinstance(FolderInS3UriError_main(), FolderInS3UriError_exceptions)
        assert not isinstance(FolderInS3UriError_main(), FolderInS3UriError_test)
        assert not isinstance(FolderInS3UriError_exceptions(), FolderInS3UriError_main)
        assert isinstance(FolderInS3UriError_exceptions(), FolderInS3UriError_exceptions)
        assert not isinstance(FolderInS3UriError_exceptions(), FolderInS3UriError_test)
        assert not isinstance(FolderInS3UriError_test(), FolderInS3UriError_main)
        assert not isinstance(FolderInS3UriError_test(), FolderInS3UriError_exceptions)
        assert isinstance(FolderInS3UriError_test(), FolderInS3UriError_test)
        assert isinstance(FolderInS3UriError_main(), FileExistsError)
        assert isinstance(FolderInS3UriError_exceptions(), FileExistsError)
        assert isinstance(FolderInS3UriError_test(), FileExistsError)
        assert id(FolderInS3UriError_main) != id(FolderInS3UriError_exceptions)
        assert id(FolderInS3UriError_main) != id(FolderInS3UriError_test)
        assert id(FolderInS3UriError_exceptions) != id(FolderInS3UriError_test)
        assert FolderInS3UriError_main is FolderInS3UriError_main
        assert FolderInS3UriError_main == FolderInS3UriError_main
        assert FolderInS3UriError_main is not FolderInS3UriError_exceptions
        assert FolderInS3UriError_main != FolderInS3UriError_exceptions
        assert FolderInS3UriError_main is not FolderInS3UriError_test
        assert FolderInS3UriError_main != FolderInS3UriError_test
        assert FolderInS3UriError_exceptions is not FolderInS3UriError_test
        assert FolderInS3UriError_exceptions != FolderInS3UriError_test
        for test_values in (
            (
                FolderInS3UriError_main,
                {FolderInS3UriError_main},
                {FolderInS3UriError_exceptions, FolderInS3UriError_test},
            ),
            (
                FolderInS3UriError_exceptions,
                {FolderInS3UriError_exceptions},
                {FolderInS3UriError_main, FolderInS3UriError_test},
            ),
            (
                FolderInS3UriError_test,
                {FolderInS3UriError_test},
                {FolderInS3UriError_exceptions, FolderInS3UriError_main},
            ),
        ):
            exception_to_check, expected_catched, expected_not_catched = test_values
            exception_catcher_array = (
                FolderInS3UriError_main,
                FolderInS3UriError_exceptions,
                FolderInS3UriError_test,
            )
            catch_results = self._get_what_imports_can_catch_the_exception(exception_to_check, exception_catcher_array)
            self.assertEqual(expected_catched, catch_results.catched)
            self.assertEqual(expected_not_catched, catch_results.not_catched)

    def _get_what_imports_can_catch_the_exception(self, exception_to_catch, exception_catcher_array) -> CatchResults:
        return ExceptionCatchersClassifier(exception_catcher_array).get_cathers_classified_by_can_catch_the_exception(
            exception_to_catch
        )


class ExceptionCatchersClassifier:
    def __init__(self, exception_catcher_array: tuple[Exception]):
        self._exception_catcher_array = exception_catcher_array

    def get_cathers_classified_by_can_catch_the_exception(self, exception_to_catch) -> CatchResults:
        catch_results = CatchResults()
        for exception_catcher in self._exception_catcher_array:
            if ExceptionCatcherChecker(exception_catcher).can_catch_the_exception(exception_to_catch):
                catch_results.add_to_catched(exception_catcher)
            else:
                catch_results.add_to_not_catched(exception_catcher)
        return catch_results


class ExceptionCatcherChecker:
    def __init__(self, exception_catcher: Exception):
        self._exception_catcher = exception_catcher

    def can_catch_the_exception(self, exception_to_catch: Exception):
        try:
            raise exception_to_catch
        except self._exception_catcher:
            # I add assertions to understand how try-except works to know why some exceptions are different.
            assert isinstance(exception_to_catch(), self._exception_catcher)  # Check is an instance.
            assert exception_to_catch is self._exception_catcher  # Same memory address.
            assert exception_to_catch == self._exception_catcher  # Same value.
            return True
        except:
            assert not isinstance(exception_to_catch(), self._exception_catcher)
            assert exception_to_catch is not self._exception_catcher
            assert exception_to_catch != self._exception_catcher
            return False
