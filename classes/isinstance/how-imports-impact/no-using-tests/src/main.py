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

# Why different imports of the same file generate different objects?
# The difference between these classes is:
print(FromSubfolderCustomError)  # <class 'subfolder.exceptions.CustomError'>
print(BFromSubfolderCustomError)  # <class 'subfolder.exceptions.CustomError'>
print(FromFileCustomError)  # <class 'exceptions.CustomError'>
# What is the value after `class`? It is the loaded module.
# https://docs.python.org/3/library/sys.html#sys.modules
# sys.modules: This is a dictionary that maps module names to modules which have already been loaded
print(sys.modules["subfolder.exceptions"]) # <module 'subfolder.exceptions' from '/home/x/Software/python/classes/
                                           # isinstance/how-imports-impact/no-using-tests/src/subfolder/exceptions.py'>
print(sys.modules["exceptions"]) # <module 'exceptions' from '/home/x/Software/python/classes/isinstance/
                                 # how-imports-impact/no-using-tests/src/subfolder/exceptions.py'>
# https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces:
# - A namespace is a mapping from names to objects
# - there is absolutely no relation between names in different namespaces
# https://docs.python.org/3/tutorial/modules.html: Each module has its own private namespace
# - https://docs.python.org/3/tutorial/modules.html: There is a variant of the import statement that imports names from
# a module directly into the importing module’s namespace. For example: from fibo import fib, fib2
# Conclusion: as FromFileCustomError and FromSubfolderCustomError are from different modules, as each module has its
# own namespace, in each namepsace they are different objects, and when are imported to the namespace of
# the module that makes the imports, they are different objects.
