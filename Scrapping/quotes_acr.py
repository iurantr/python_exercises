url = "http://quotes.toscrape.com/"

from urllib.request import (urlopen) #, urlparse, urlunparse, urlretrieve)

from bs4 import BeautifulSoup as bs

thereIsNextPage = True
page = ""
quotes = []
while thereIsNextPage:
    print("Processing page: ", url+page)
    soup = bs(urlopen(url+page), 'html5lib')
    # truc plus propre
    for quote in soup.find_all('div', {"class":"quote"}):
        quote_text = quote.find_all('span', {'class':'text'})[0].get_text()
        quote_author = quote.find_all('small', {'class': 'author'})[0].get_text()
        quotes.append({"quote text": quote_text, "quote author": quote_author})

    next_page = soup.find_all('li', {"class":"next"})
    if len(next_page):
        page = next_page[0].find_all('a')[0].get('href')
    else:
        thereIsNextPage = False

for quoteT in quotes:
    print(quoteT["quote text"], " by ", quoteT["quote author"])

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


