from enum import Enum
from selenium_scrap import SeleniumScrap
from requests_scrap import RequestScrap


class YahooScrapper:
    def __init__(self, ticker, settings):
        self.ticker = ticker
        self.parameters = settings

    def scrap(self):
        if self.parameters == ScrappingType.full:
            selenium = SeleniumScrap(self.ticker)
            soups = selenium.get_statements()
            return soups

        elif self.parameters == ScrappingType.normal:
            normal_scrap = RequestScrap(self.ticker)
            soups = normal_scrap.get_statements()
            return soups


class ScrappingType(Enum):
    full = 1
    normal = 2
