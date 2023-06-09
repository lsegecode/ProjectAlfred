from abc import ABC, abstractmethod


class ScraperStrategy(ABC):
    @abstractmethod
    def get_url(self, product):
        pass

    def read_information(self, product) -> str:
        pass


