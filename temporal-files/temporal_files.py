# https://docs.python.org/3/library/tempfile.html#examples

import tempfile

with tempfile.TemporaryDirectory() as tmp_dir_path_name:
    assert isinstance(tmp_dir_path_name, str)
    print('created temporary directory', tmp_dir_path_name)

with tempfile.NamedTemporaryFile() as fp:
    fp.write(b'Hello world!')
    print('created temporary file', fp.name)
    fp.seek(0)
    print(fp.read())
