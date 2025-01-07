from src.exceptions import CustomError as AbsoluteImportCustomError

from exceptions import CustomError as RelativeImportCustomError


def run_catch_exception() -> str:
    try:
        _RunRaiseException().run()
        return "No exception :("
    except FileExistsError:
        return "Catched FileExistsError!"
    except ValueError:
        return "Catched ValueError!"
    except RelativeImportCustomError:
        return "Catched RelativeImportCustomError!"
    except AbsoluteImportCustomError:
        return "Catched AbsoluteImportCustomError!"
    except:
        return "No catched :("


class _RunRaiseException:
    def run(self):
        raise FileExistsError
