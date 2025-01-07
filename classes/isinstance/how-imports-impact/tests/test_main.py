import unittest

from src.exceptions import CustomError as ExceptionsCustomError
from src.main import AbsoluteImportCustomError as MainAbsoluteImportCustomError
from src.main import RelativeImportCustomError as MainRelativeImportCustomError


class _TestCustomError(FileExistsError):
    pass


class TestCustomError(unittest.TestCase):
    def test_id_has_expected_behaviour(self):
        # Not instance.
        self.assertEqual(id(ExceptionsCustomError), id(MainAbsoluteImportCustomError))
        self.assertNotEqual(id(ExceptionsCustomError), id(MainRelativeImportCustomError))
        self.assertNotEqual(id(_TestCustomError), id(ExceptionsCustomError))
        self.assertNotEqual(id(_TestCustomError), id(MainAbsoluteImportCustomError))
        self.assertNotEqual(id(_TestCustomError), id(MainRelativeImportCustomError))
        # Instances.
        self.assertEqual(id(ExceptionsCustomError()), id(MainAbsoluteImportCustomError()))
        self.assertEqual(id(ExceptionsCustomError()), id(MainRelativeImportCustomError()))

    def test_isinstance_has_expected_behaviour(self):
        self.assertTrue(isinstance(ExceptionsCustomError(), MainAbsoluteImportCustomError))
        self.assertFalse(isinstance(ExceptionsCustomError(), MainRelativeImportCustomError))
        self.assertFalse(isinstance(_TestCustomError(), ExceptionsCustomError))
        self.assertFalse(isinstance(_TestCustomError(), MainAbsoluteImportCustomError))
        self.assertFalse(isinstance(_TestCustomError(), MainRelativeImportCustomError))
