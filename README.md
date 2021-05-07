# Scrapping financial statements from Yahoo Finance

Command line based. Scrap [yahoo finance](https://finance.yahoo.com) and return an excel file containing data of all 3 financial statements, with a different sheet for each company scrapped.

### Financial statements
Return data for these 3 financial statements:
* Income Statement
* Balance Sheet
* Cash Flow

### Utilisation
Here is an example of how to use the program. Type the following in your terminal:

`python main.py AAPL AMZN TSLA -full`

After yahoo_finance.py, add as much tickers of companies for which you want to retrieve the data. Ie: AAPL for Apple, NFLX for Netflix, etc...

Add '-full' at the end **_only_** if you want to scrap the complete table. By default, without the '-full' option, only the first level entries will be scrapped (in green in the screenshot below).

![yahoo](https://user-images.githubusercontent.com/69766734/105063145-ae7f7d00-5a7b-11eb-9f63-d676e5f2633d.png)

With the '-full' option added, all the content of the tables will be retrieved, including the lines in red. Beware that using this option will result in a **_much longer_** computing time. This is because the page is using Javascript to hide these lines by default, and we need Selenium to simulate a click on these rows to expand them and be able to retrieve the data.

Once the scrapping is done, simply open the file output.xlsx and directly start analyzing the data as you wish! It will be already formatted correctly (ie: numeric data converted as numbers) and you will find a different sheet for each ticker you entered.

### Requirements and libraries

* Firefox 
* Selenium 
* Beautiful Soup
* Requests
* Pandas

### Changelog
20/01/2021: Changed file structure and improved performances for '-full' option.
