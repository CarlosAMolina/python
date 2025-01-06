from src.exceptions import CustomError


def run_cath_exceptions():
    try:
        _RunRaiseException().raise_file_exists_error()
    except FileExistsError:
        return "exception: FileExistsError"
    except:
        raise Exception("No exception was catched")

class _RunRaiseException:
    def raise_file_exists_error(self):
        raise FileExistsError

    def raise_custom_error(self):
        raise CustomError
