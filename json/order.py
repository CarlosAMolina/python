from collections import OrderedDict
import json

def get_dict() -> dict:
    with open("json.json", "r") as f:
        return json.load(f)


def get_ordered_dict() -> OrderedDict:
    with open("json.json", "r") as f:
        return json.load(f, object_pairs_hook=OrderedDict)


# Both methods preserve the file order
# This is extrange, in another program with a larger dict I need to use `get_ordered_dict` for that
assert list(get_dict().keys()) == ["b", "a"]
assert list(get_ordered_dict().keys()) == ["b", "a"]
