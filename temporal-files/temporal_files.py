# https://docs.python.org/3/library/tempfile.html#examples

import tempfile

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)

with tempfile.NamedTemporaryFile() as fp:
    fp.write(b'Hello world!')
    print('created temporary file', fp.name)
    fp.seek(0)
    print(fp.read())
