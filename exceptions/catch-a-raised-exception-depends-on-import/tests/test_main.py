import unittest

from src.exceptions import FolderInS3UriError as FolderInS3UriError_exceptions

from src.main import FolderInS3UriError as FolderInS3UriError_main


class FolderInS3UriError_test(FileExistsError):
    pass


class CatchResults:
    def __init__(self):
        self._catched = set()
        self._not_catched = set()

    def __repr__(self) -> str:
        catched_summary = self._get_summary('catched', self._catched)
        not_catched_summary = self._get_summary('not catched', self._not_catched)
        return f"{catched_summary}\n{not_catched_summary}"

    def _get_summary(self, type_str: str, values: set) -> str:
        return f"{type_str} ({len(self._catched)}): {','.join(values)}"

    @property
    def catched(self) -> set:
        return self._catched

    @property
    def not_catched(self) -> set:
        return self._not_catched

    def add_to_catched(self, name: str):
        self._catched.add(name)

    def add_to_not_catched(self, name: str):
        self._not_catched.add(name)


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
