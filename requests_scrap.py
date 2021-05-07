from bs4 import BeautifulSoup
import requests


class RequestScrap:
    def __init__(self, ticker):
        self.ticker = ticker
        self.req_type_list = ['financials', 'balance-sheet', 'cash-flow']
        self.soups = []

    def get_statements(self):
        for req_type in self.req_type_list:
            html_link = f"https://finance.yahoo.com/quote/{self.ticker}/{req_type}?p={self.ticker}"
            html_page = requests.get(html_link)

            self.soups.append(BeautifulSoup(html_page.content, 'html.parser'))

        return self.soups
