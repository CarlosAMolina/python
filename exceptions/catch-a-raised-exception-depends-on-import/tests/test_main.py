import unittest

from src.exceptions import FolderInS3UriError as FolderInS3UriError_exceptions
from src.main import CatchResults
from src.main import FolderInS3UriError_main


class FolderInS3UriError_test(FileExistsError):
    pass


class TestCatchExceptions(unittest.TestCase):
    def test_what_imports_can_catch_exceptions(self):
        catch_results = self._get_what_imports_can_catch_the_exception(FolderInS3UriError_main)
        self.assertEqual({"FolderInS3UriError_main"}, catch_results.catched)
        self.assertEqual({"FolderInS3UriError_exceptions", "FolderInS3UriError_test"}, catch_results.not_catched)
        catch_results = self._get_what_imports_can_catch_the_exception(FolderInS3UriError_exceptions)
        self.assertEqual({"FolderInS3UriError_exceptions"}, catch_results.catched)
        self.assertEqual({"FolderInS3UriError_main", "FolderInS3UriError_test"}, catch_results.not_catched)
        catch_results = self._get_what_imports_can_catch_the_exception(FolderInS3UriError_test)
        self.assertEqual({"FolderInS3UriError_test"}, catch_results.catched)
        self.assertEqual({"FolderInS3UriError_exceptions", "FolderInS3UriError_main"}, catch_results.not_catched)

    def _get_what_imports_can_catch_the_exception(self, exception_to_check) -> CatchResults:
        catch_results = CatchResults()
        exception_catcher = FolderInS3UriError_main
        exception_catcher_str = "FolderInS3UriError_main"
        if self._is_exception_catched_by_exception(exception_to_check, exception_catcher):
            catch_results.add_to_catched(exception_catcher_str)
        else:
            catch_results.add_to_not_catched(exception_catcher_str)
        exception_catcher = FolderInS3UriError_exceptions
        exception_catcher_str = "FolderInS3UriError_exceptions"
        if self._is_exception_catched_by_exception(exception_to_check, exception_catcher):
            catch_results.add_to_catched(exception_catcher_str)
        else:
            catch_results.add_to_not_catched(exception_catcher_str)
        exception_catcher = FolderInS3UriError_test
        exception_catcher_str = "FolderInS3UriError_test"
        if self._is_exception_catched_by_exception(exception_to_check, exception_catcher):
            catch_results.add_to_catched(exception_catcher_str)
        else:
            catch_results.add_to_not_catched(exception_catcher_str)
        return catch_results

    def _is_exception_catched_by_exception(self, exception_to_catch, exception_catcher):
        try:
            raise exception_to_catch
        except exception_catcher:
            return True
        except:
            return False
