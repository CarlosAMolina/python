import unittest

from src.exceptions import CustomError as CustomError_exceptions
from src.main import CustomErrorAbsoluteImport as CustomError_absolute_main
from src.main import CustomErrorRelativeImport as CustomError_relative_main


class CustomError_test(FileExistsError):
    pass


class TestIsinstance(unittest.TestCase):
    def test_isinstance_has_excpected_behaviour(self):
        assert isinstance(CustomError_exceptions(), CustomError_absolute_main)
        assert not isinstance(CustomError_exceptions(), CustomError_relative_main)
