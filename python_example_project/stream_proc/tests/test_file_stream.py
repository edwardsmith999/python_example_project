import os

from python_example_project.stream_proc.file_stream import FileStream


def test_file_stream():
    fstream = FileStream(os.path.join(os.path.dirname(__file__), 'data/numbers.txt'))

    for i in range(1,11):
        assert float(i) == fstream.next_number()
