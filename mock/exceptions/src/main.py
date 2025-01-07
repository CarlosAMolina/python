from src.exceptions import CustomError


def run_catch_exception() -> str:
    try:
        _RunRaiseException().run()
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
    def run(self):
        raise FileExistsError
