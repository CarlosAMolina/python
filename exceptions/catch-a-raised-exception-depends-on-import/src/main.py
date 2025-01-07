from src.exceptions import CustomError as AbsoluteImportCustomError

from exceptions import CustomError as RelativeImportCustomError


def _call_imports_to_avoid_pre_commit_dead_code_deletion():
    print(AbsoluteImportCustomError, RelativeImportCustomError)
