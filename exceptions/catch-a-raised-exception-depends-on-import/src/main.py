from exceptions import FolderInS3UriError


def run():
    print("Do some stuff with the exception: ", FolderInS3UriError)


class CatchResults:
    def __init__(self):
        self._catched = set()
        self._not_catched = set()

    def __repr__(self) -> str:
        catched_summary = self._get_summary("catched", self._catched)
        not_catched_summary = self._get_summary("not catched", self._not_catched)
        return f"{catched_summary}\n{not_catched_summary}"

    def _get_summary(self, type_str: str, values: set) -> str:
        return f"{type_str} ({len(self._catched)}): {','.join(values)}"

    @property
    def catched(self) -> set:
        return self._catched

    @property
    def not_catched(self) -> set:
        return self._not_catched

    def add_to_catched(self, name: str):
        self._catched.add(name)

    def add_to_not_catched(self, name: str):
        self._not_catched.add(name)


if __name__ == "__main__":
    run()
