import os
import tempfile
import pytest
from datetime import datetime
from mock import Mock, patch

import numpy as np

from python_example_project.stream_proc.file_stream import FileStreamStats,\
        FileStatsError, check_file_stats


def test_file_stream_stats_next():
    fsstat = FileStreamStats(os.path.join(os.path.dirname(__file__), 'data/numbers.txt'))

    test_data = []
    for i in range(1,11):
        test_data.append(i)
        assert float(i) == fsstat.next_number()
        assert test_data == fsstat._data
        np.testing.assert_array_equal(np.array(test_data), fsstat.data())


@patch.object(FileStreamStats, 'data')
def test_file_stream_stats(mock_fsstat_data, file_stats_test_data):
    with tempfile.NamedTemporaryFile(mode='r') as f_tmp:
        fsstat = FileStreamStats(f_tmp.name)

        mock_fsstat_data.return_value = np.array(file_stats_test_data)

        assert fsstat.min() == 1
        assert fsstat.max() == 5
        assert fsstat.mean() == 3


@patch.object(FileStreamStats, 'min')
@patch.object(FileStreamStats, 'max')
def test_check_file_stats(mock_fsstat_max, mock_fsstat_min):
    with tempfile.NamedTemporaryFile(mode='r') as f_tmp:
        fsstat = FileStreamStats(f_tmp.name)

        mock_fsstat_min.return_value = 1
        mock_fsstat_max.return_value = 10

        assert check_file_stats(fsstat)

        mock_fsstat_min.return_value = 1
        mock_fsstat_max.return_value = 1000

        with pytest.raises(FileStatsError) as e:
            check_file_stats(fsstat)
        assert e.value.message == 'Maximum value is too high!'

        mock_fsstat_min.return_value = -1
        mock_fsstat_max.return_value = 10

        with pytest.raises(FileStatsError) as e:
            check_file_stats(fsstat)
        assert e.value.message == 'Minimum value is too low!'

        assert mock_fsstat_min.call_count == 3
        assert mock_fsstat_max.call_count == 2


def test_file_stream_stats_fixture(file_stats_object):
    fsstat = file_stats_object
    assert fsstat.timestamp == datetime.strptime('01-01-2000', '%d-%m-%Y')
