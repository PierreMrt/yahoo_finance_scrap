import sys
from yahoo_scrapping import YahooScrapper, ScrappingType
from excel_creation import OutputCreator


if __name__ == '__main__':

    ticker_list = []
    settings = ScrappingType.normal

    if '-full' in sys.argv:
        sys.argv.remove('-full')
        settings = ScrappingType.full

    for elt in sys.argv[1:]:
        ticker_list.append(elt)

    for ticker in ticker_list:
        print(f'Scrapping {ticker} ...')
        scrapper = YahooScrapper(ticker, settings)
        soups = scrapper.scrap()

        creator = OutputCreator(soups, ticker)
        creator.create_dataframe()
        creator.df_to_excel()

    print('Scrapping done ! Results extracted in output.xlsx')
