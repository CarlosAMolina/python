"""Script that uses functions in different paths
"""

import sys
import os


def add_functions_paths():
    this_script_path = os.path.dirname(os.path.abspath(__file__))
    for path in ["..", "../folder_2", "folder_3"]:
        sys.path.append(this_script_path + '/' + path)


add_functions_paths()


from script_in_upper_path import say_hi
from script_in_upper_external_folder import say_bye
from script_in_lower_path import say_later


# use functions
say_hi()
say_bye()
say_later()
