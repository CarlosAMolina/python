import unittest

from src.exceptions import CustomError as ExceptionsCustomError
from src.main import FromSrcImportCustomError as MainFromSrcImportCustomError
from src.main import FromExceptionsImportCustomError as MainFromExceptionsImportCustomError


class _TestCustomError(FileExistsError):
    pass


class TestCatchExceptions(unittest.TestCase):
    def test_what_imports_can_catch_exceptions(self):
        # When the import is done in the same way in both files, the exception can be catched.
        self.assertTrue(_can_exception_be_catched_by_catcher(MainFromSrcImportCustomError, FileExistsError))
        self.assertTrue(_can_exception_be_catched_by_catcher(MainFromSrcImportCustomError, ExceptionsCustomError))
        self.assertFalse(_can_exception_be_catched_by_catcher(MainFromSrcImportCustomError, _TestCustomError))
        self.assertTrue(_can_exception_be_catched_by_catcher(MainFromExceptionsImportCustomError, FileExistsError))
        self.assertFalse(_can_exception_be_catched_by_catcher(MainFromExceptionsImportCustomError, ExceptionsCustomError))
        self.assertFalse(_can_exception_be_catched_by_catcher(MainFromExceptionsImportCustomError, _TestCustomError))
        self.assertTrue(_can_exception_be_catched_by_catcher(ExceptionsCustomError, FileExistsError))
        self.assertTrue(_can_exception_be_catched_by_catcher(ExceptionsCustomError, MainFromSrcImportCustomError))
        self.assertFalse(_can_exception_be_catched_by_catcher(ExceptionsCustomError, MainFromExceptionsImportCustomError))
        self.assertFalse(_can_exception_be_catched_by_catcher(ExceptionsCustomError, _TestCustomError))


def _can_exception_be_catched_by_catcher(exception_to_catch: type[Exception], exception_catcher: type[Exception]):
    """
    - What catch does (https://docs.python.org/3/tutorial/errors.html): A class in an except clause
    matches exceptions which are instances of the class itself or one of its derived classes.
    """
    try:
        raise exception_to_catch
    except exception_catcher:
        # I add assertions to understand how try-except works.
        assert isinstance(exception_to_catch(), exception_catcher)
        return True
    except:
        assert not isinstance(exception_to_catch(), exception_catcher)
        return False
