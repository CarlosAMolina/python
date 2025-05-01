def assert_order_is_preserved():
    dict_ = dict()
    dict_["x"] = "foo"
    dict_["a"] = "foo"
    assert list(dict_.keys()) == ["x", "a"]

if __name__ == "__main__":
    assert_order_is_preserved()
