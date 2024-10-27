"""
https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
"""

def get_array_wrong(list_to_modify=[]):
    """The args musn't have `[]` as default value."""
    list_to_modify.append(1)
    return list_to_modify 


def run_array_modified_wrong():
    assert [1] == get_array_wrong()
    assert [1, 1] == get_array_wrong()
    assert [1, 1, 1] == get_array_wrong()


def get_array_ok(list_to_modify=None):
    if list_to_modify is None:
        list_to_modify = []
    list_to_modify.append(1)
    return list_to_modify 


def run_array_modified_ok():
    assert [1] == get_array_ok()
    assert [1] == get_array_ok()
    assert [1] == get_array_ok()


def run_array_modified_ok_if_argument_is_list():
    assert [1, 1] == get_array_ok(list_to_modify=list({1:1}.keys()))
    assert [1, 1] == get_array_ok(list_to_modify=list({1:1}.keys()))
    assert [1, 1] == get_array_ok(list_to_modify=list({1:1}.keys()))


if __name__ == "__main__":
    run_array_modified_wrong()
    run_array_modified_ok()
    run_array_modified_ok_if_argument_is_list()

