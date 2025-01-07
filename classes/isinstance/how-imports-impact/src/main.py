from src.exceptions import CustomError as CustomErrorAbsoluteImport

from exceptions import CustomError as CustomErrorRelativeImport


def _call_imports_to_avoid_pre_commit_dead_code_deletion():
    print(CustomErrorAbsoluteImport, CustomErrorRelativeImport)
