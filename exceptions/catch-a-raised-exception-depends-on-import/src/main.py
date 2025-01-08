from src.exceptions import CustomError as FromSrcImportCustomError

from exceptions import CustomError as FromExceptionsImportCustomError


def _call_imports_to_avoid_pre_commit_dead_code_deletion():
    print(FromSrcImportCustomError, FromExceptionsImportCustomError)
