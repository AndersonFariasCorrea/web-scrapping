from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def search(self, query):
        pass

    @abstractmethod
    def get_contents(self, request_result):
        pass

    @abstractmethod
    def __format_contents(self, content):
        pass
