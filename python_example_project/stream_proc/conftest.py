import pytest
from datetime import datetime

from python_example_project.stream_proc.file_stream import FileStreamStats

TEST_FSSTAT_DATA = [1, 2, 3, 4, 5]


@pytest.fixture(scope="session")
def file_stats_test_data():
    return TEST_FSSTAT_DATA


@pytest.fixture(scope="module")
def file_stats_object():
    class FileStreamStatsMock(FileStreamStats):
        def __init__(self):
            self._data = file_stats_test_data()
            self.timestamp = datetime.strptime('01-01-2000', '%d-%m-%Y')
    return FileStreamStatsMock()
