import abc
from datetime import datetime

import numpy as np

from python_example_project.number_class import Number


class StatsMixin(object):
    __metaclass__ = abc.ABCMeta

    def min(self):
        return np.min(self.data())

    def max(self):
        return np.max(self.data())

    def mean(self):
        return np.mean(self.data())

    @abc.abstractmethod
    def data(self):
        raise NotImplementedError


class FileStream(object):

    def __init__(self, fname):
        self._f = open(fname, 'r')

    def next_number(self):
        return float(next(self._f))


class FileStreamStats(FileStream, StatsMixin):

    def __init__(self, fname):
        super(FileStreamStats, self).__init__(fname)
        self.timestamp = datetime.now()
        self._data = []

    def data(self):
        return np.array(self._data)

    def next_number(self):
        new = super(FileStreamStats, self).next_number()
        self._data.append(new)
        return new
