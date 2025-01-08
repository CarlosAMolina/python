import unittest

from src.exceptions import CustomError as ExceptionsCustomError
from src.main import FromSrcImportCustomError as MainFromSrcImportCustomError
from src.main import FromExceptionsImportCustomError as MainFromExceptionsImportCustomError


class _TestCustomError(FileExistsError):
    pass


class TestCustomError(unittest.TestCase):
    def test_isinstance_has_expected_behaviour(self):
        # When the import is done in the same way in both files, isinstance is True.
        self.assertTrue(isinstance(ExceptionsCustomError(), MainFromSrcImportCustomError))
        self.assertFalse(isinstance(ExceptionsCustomError(), MainFromExceptionsImportCustomError))
        self.assertFalse(isinstance(_TestCustomError(), ExceptionsCustomError))
        self.assertFalse(isinstance(_TestCustomError(), MainFromSrcImportCustomError))
        self.assertFalse(isinstance(_TestCustomError(), MainFromExceptionsImportCustomError))

    def test_id_has_expected_behaviour(self):
        # Not instance.
        self.assertEqual(id(ExceptionsCustomError), id(MainFromSrcImportCustomError))
        self.assertNotEqual(id(ExceptionsCustomError), id(MainFromExceptionsImportCustomError))
        self.assertNotEqual(id(_TestCustomError), id(ExceptionsCustomError))
        self.assertNotEqual(id(_TestCustomError), id(MainFromSrcImportCustomError))
        self.assertNotEqual(id(_TestCustomError), id(MainFromExceptionsImportCustomError))
        # Instances.
        self.assertEqual(id(ExceptionsCustomError()), id(MainFromSrcImportCustomError()))
        self.assertEqual(id(ExceptionsCustomError()), id(MainFromExceptionsImportCustomError()))
