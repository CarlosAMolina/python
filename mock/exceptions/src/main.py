class RunRaiseException:
    def raise_file_exists_error(self):
        raise FileExistsError

    def raise_custom_error(self):
        raise _CustomError


class _CustomError(ZeroDivisionError):
    pass
