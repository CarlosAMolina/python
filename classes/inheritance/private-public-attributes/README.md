## Introduction

This example shows how class attributes that are or are not used by child classes should be defined, if they should be public or private.

## Problem explanation

I want to refactor the example code. The child classes have two common methods to move to the ABC, the points to take into account are:

- `_get_price_apply_special_discount`: is used by child classes. This method must be protected.
- `_is_today_weekend`: is only used by `_get_price_apply_special_discount`, the child classes does not call it directly. This method must be private.

## References

This [link](https://stackoverflow.com/questions/11483366/protected-method-in-python) points to this [blog](https://radek.io/posts/private-protected-and-public-in-python/) and [the official documentation](https://peps.python.org/pep-0008/#designing-for-inheritance).



