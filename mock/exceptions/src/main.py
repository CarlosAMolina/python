from src.exceptions import CustomError


def run_cath_exception() -> str:
    try:
        _RunRaiseException().raise_file_exists_error()
        return "No exception :("
    except FileExistsError:
        return "Catched FileExistsError!"
    except ValueError:
        return "Catched ValueError!"
    except CustomError:
        return "Catched CustomError!"
    except:
        return "No catched :("


class _RunRaiseException:
    def raise_file_exists_error(self):
        raise FileExistsError

    def raise_custom_error(self):
        raise CustomError
