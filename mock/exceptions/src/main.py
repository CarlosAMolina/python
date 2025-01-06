from src.exceptions import CustomError


def run_cath_exception():
    try:
        _RunRaiseException().raise_file_exists_error()
    except FileExistsError:
        return "Catched!"
    return "No catched :("


class _RunRaiseException:
    def raise_file_exists_error(self):
        raise FileExistsError

    def raise_custom_error(self):
        raise CustomError
