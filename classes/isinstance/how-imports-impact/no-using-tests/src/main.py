import pathlib
import sys

from subfolder.exceptions import CustomError as FromSubfolderCustomError

sys.path.append(str(pathlib.Path(__file__).parent.absolute().joinpath("subfolder")))

from exceptions import CustomError as FromFileCustomError


# Despite the class is imported from the same file, it has a different ID in each different import.
# https://docs.python.org/3/reference/expressions.html#is-not
# https://docs.python.org/3/library/functions.html#id
# https://docs.python.org/3/library/functions.html#isinstance
assert FromFileCustomError is not FromSubfolderCustomError
assert not isinstance(FromFileCustomError(), FromSubfolderCustomError)
assert not isinstance(FromSubfolderCustomError(), FromFileCustomError)
