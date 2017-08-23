#! python3
# webScrapeData.py - Web scraping data from a table on a website and displaying that data
# https://pythonprogramminglanguage.com/web-scraping-with-pandas-and-beautifulsoup/

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

res = requests.get("http://racerxonline.com/results/2017/las-vegas/450sx")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
print( tabulate(df[0], headers='keys', tablefmt='psql') )
