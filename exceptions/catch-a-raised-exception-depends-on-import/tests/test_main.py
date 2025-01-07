import unittest

from src.exceptions import FolderInS3UriError as FolderInS3UriError_exceptions

from src.main import FolderInS3UriError as FolderInS3UriError_main
from src.main import CatchResults


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
        try:
            raise exception_to_check
        except FolderInS3UriError_main:
            catch_results.add_to_catched("FolderInS3UriError_main")
        except:
            catch_results.add_to_not_catched("FolderInS3UriError_main")
        try:
            raise exception_to_check
        except FolderInS3UriError_exceptions:
            catch_results.add_to_catched("FolderInS3UriError_exceptions")
        except:
            catch_results.add_to_not_catched("FolderInS3UriError_exceptions")
        try:
            raise exception_to_check
        except FolderInS3UriError_test:
            catch_results.add_to_catched("FolderInS3UriError_test")
        except:
            catch_results.add_to_not_catched("FolderInS3UriError_test")
        return catch_results
