from abc import ABC, abstractmethod


class Parser(ABC):

    def __init__(self):
        self.data_parsed = {}

    @abstractmethod
    def parse(self, html):
        return self.data_parsed
