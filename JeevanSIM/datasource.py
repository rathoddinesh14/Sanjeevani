from abc import ABC, abstractmethod

# Base DataSource Abstract Class
class DataSource(ABC):
    @abstractmethod
    def save(self, data):
        pass

class DataSourceDecorator(DataSource):
    def __init__(self, source=None):
        self._source = source

    def save(self, data):
        if self._source is not None:
            self._source.save(data)