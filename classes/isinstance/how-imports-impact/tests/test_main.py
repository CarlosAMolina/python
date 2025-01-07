import unittest

from src.exceptions import CustomError as ExceptionsCustomError
from src.main import AbsoluteImportCustomError as MainAbsoluteImportCustomError
from src.main import RelativeImportCustomError as MainRelativeImportCustomError


class CustomError_test(FileExistsError):
    pass


class TestCustomError(unittest.TestCase):
    def test_id_has_expected_behaviour(self):
        # Not instance.
        self.assertEqual(id(ExceptionsCustomError), id(MainAbsoluteImportCustomError))
        self.assertNotEqual(id(ExceptionsCustomError), id(MainRelativeImportCustomError))
        # Instances.
        self.assertEqual(id(ExceptionsCustomError()), id(MainAbsoluteImportCustomError()))
        self.assertEqual(id(ExceptionsCustomError()), id(MainRelativeImportCustomError()))

    def test_isinstance_has_excpected_behaviour(self):
        assert isinstance(ExceptionsCustomError(), MainAbsoluteImportCustomError)
        assert not isinstance(ExceptionsCustomError(), MainRelativeImportCustomError)
