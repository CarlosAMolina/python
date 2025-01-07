import unittest

from src.exceptions import CustomError as ExceptionsCustomError
from src.main import AbsoluteImportCustomError as MainAbsoluteImportCustomError
from src.main import RelativeImportCustomError as MainRelativeImportCustomError


class CustomError_test(FileExistsError):
    pass


class TestIsinstance(unittest.TestCase):
    def test_isinstance_has_excpected_behaviour(self):
        assert id(ExceptionsCustomError) == id(MainAbsoluteImportCustomError)
        assert id(ExceptionsCustomError) != id(MainRelativeImportCustomError)
        assert id(ExceptionsCustomError()) == id(MainAbsoluteImportCustomError()) == id(MainRelativeImportCustomError())
        assert isinstance(ExceptionsCustomError(), MainAbsoluteImportCustomError)
        assert not isinstance(ExceptionsCustomError(), MainRelativeImportCustomError)
