import pathlib
import sys

from subfolder.exceptions import CustomError as FromSubfolderCustomError
from subfolder.exceptions import CustomError as BFromSubfolderCustomError

sys.path.append(str(pathlib.Path(__file__).parent.absolute().joinpath("subfolder")))

from exceptions import CustomError as FromFileCustomError

# Show classes are different.
# Despite the class is imported from the same file, it has a different ID in each different import.
# https://docs.python.org/3/reference/expressions.html#is-not
# https://docs.python.org/3/library/functions.html#id
# https://docs.python.org/3/library/functions.html#isinstance
assert FromSubfolderCustomError is BFromSubfolderCustomError  # The alias does not change the object (same id()).
assert FromFileCustomError is not FromSubfolderCustomError  # The different import changes the object.
assert isinstance(FromSubfolderCustomError(), BFromSubfolderCustomError)
assert not isinstance(FromFileCustomError(), FromSubfolderCustomError)
assert not isinstance(FromSubfolderCustomError(), FromFileCustomError)

# Why are different?
print(FromSubfolderCustomError)  # <class 'subfolder.exceptions.CustomError'>
print(BFromSubfolderCustomError)  # <class 'subfolder.exceptions.CustomError'>
print(FromFileCustomError)  # <class 'exceptions.CustomError'>
# What is the value after `class`?
# I think that is some value of the module.
for module_name, module in sys.modules.copy().items():
    if 'exceptions' in module_name:
        print(module_name)
