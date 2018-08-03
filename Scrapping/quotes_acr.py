from urllib.request import (urlopen)  # , urlparse, urlunparse, urlretrieve)
from bs4 import BeautifulSoup as bs

url = "http://quotes.toscrape.com"
thereIsNextPage = True
page = ""
quotes = []
# Looping and scrapping the pages
while thereIsNextPage:
    print("Processing page: ", url + page)
    soup = bs(urlopen(url + page), 'html5lib')
    # truc plus propre
    for quote in soup.find_all('div', {"class": "quote"}):
        quote_text = quote.find_all('span', {'class': 'text'})[0].get_text()
        quote_text = quote_text.strip('“"')
        quote_author = quote.find_all('small', {'class': 'author'})[0].get_text()
        quotes.append({"Quote": quote_text, "Author": quote_author})

    next_page = soup.find_all('li', {"class": "next"})
    if len(next_page):0
        page = next_page[0].find_all('a')[0].get('href')
    else:
        thereIsNextPage = False

# Printing
for quoteT in quotes:
    print(quoteT["Quote"], " by ", quoteT["Author"])

# Saving the results
import csv

with open("quotes.csv", 'w', encoding='utf-8') as csvfile:
    csvW = csv.DictWriter(csvfile, dialect='excel', delimiter=',', \
                          fieldnames=["Quote", "Author"])
    csvW.writeheader()
    csvW.writerows(quotes)

# Save to a file
# with open("quotes.html", 'w', encoding='utf-8') as file:
#     file.write(soup.__str__())

# truc bizare:
# list_span = soup.find_all(name='span' )
# list_filt = [x for x in list_span if str(x).find('class="text" itemprop="text"') != -1]
# list_text = [x.get_text() for x in list_filt]
#
# print("\n".join(list_text))
# print("\n")
