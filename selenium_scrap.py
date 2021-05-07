from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


class SeleniumScrap:
    def __init__(self, ticker):
        self.ticker = ticker
        self.soups = []
        self.driver, self.wait = self.configure_driver()
        self.consent_cookies()

    def configure_driver(self):
        options = Options()
        # options.headless = True
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://finance.yahoo.com/quote/{self.ticker}/financials?p={self.ticker}")
        wait = WebDriverWait(driver, 10)

        return driver, wait

    def consent_cookies(self):
        # Consent cookies
        python_button = self.driver.find_elements_by_xpath(
            "//*[@id='consent-page']/div/div/div/div[2]/div[2]/form/button")[0]
        python_button.click()

    def expand_all(self):
        # Expand all
        xpath = "//*[ @id='Col1-1-Financials-Proxy']/section/div[2]/button/div/span"
        self.wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath), 'Expand All'))
        python_button = self.driver.find_element_by_xpath(xpath)
        try:
            python_button.click()
        except exceptions.StaleElementReferenceException:
            python_button = self.driver.find_element_by_xpath(xpath)
            python_button.click()

    def get_statements(self):
        # Income statement
        self.expand_all()
        self.get_soup()

        # Balance sheet and cash flow
        pages = ['balance-sheet', 'cash-flow']
        for i in range(1, 3):
            xpath = f"//*[@id='Col1-1-Financials-Proxy']/section/div[1]/div[1]/div/a[{i}]"

            python_button = self.driver.find_elements_by_xpath(xpath)[0]
            python_button.click()
            self.wait.until(EC.url_contains(pages[i-1]))
            self.expand_all()

            xpath = "//*[@id='Col1-1-Financials-Proxy']/section/div[4]/div[1]/div[1]/div[2]/div[3]/div[2]/div/div[1]"
            self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            self.get_soup()

        self.driver.quit()

        return self.soups

    def get_soup(self):
        html = self.driver.execute_script('return document.body.innerHTML;')
        self.soups.append(BeautifulSoup(html, 'html.parser'))
