from src.exceptions import CustomError as FromSrcImportCustomError

from exceptions import CustomError as FromExceptionsImportCustomError


def run_catch_exception() -> str:
    try:
        _RunRaiseException().run()
        return "No exception :("
    except FileExistsError:
        return "Catched FileExistsError!"
    except ValueError:
        return "Catched ValueError!"
    except FromExceptionsImportCustomError:
        return "Catched FromExceptionsImportCustomError!"
    except FromSrcImportCustomError:
        return "Catched FromSrcImportCustomError!"
    except:
        return "No catched :("


class _RunRaiseException:
    def run(self):
        raise FileExistsError
