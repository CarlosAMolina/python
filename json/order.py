from collections import OrderedDict
import json

def get_dict() -> dict:
    with open("json.json", "r") as f:
        return json.load(f)


def get_ordered_dict() -> OrderedDict:
    with open("json.json", "r") as f:
        return json.load(f, object_pairs_hook=OrderedDict)


# Both methods preserve the file order
assert list(get_dict().keys()) == list(get_ordered_dict().keys())
