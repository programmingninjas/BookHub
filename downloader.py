from libgen_api import LibgenSearch
import requests
from bs4 import BeautifulSoup

def download(URL):
    
    # Scraping Amazon for Book Name
    
    if 'amazon.in' in URL:

        raw = requests.get(URL,headers={'User-agent': 'Chrome'})
        
        data = BeautifulSoup(raw.content, 'html5lib')

        raw_title = data.find('span', class_='a-size-extra-large').text

        title = raw_title.lstrip('\n').rstrip('\n').replace('()', '')
        
    # Scraping Flipkart for Book Name
    elif 'flipkart.com' in URL:

        raw = requests.get(URL,headers={'User-agent': 'Chrome'})
        
        data = BeautifulSoup(raw.content, 'html5lib')

        raw_title = data.find('span', class_='B_NuCI').text

        title = ''

        for i in raw_title:

            if i != '(':

                title += i
            
            else:

                break

    else:
        
        title = URL  #it's the pure name not a link

    library = LibgenSearch()

    filters = {"Extension": "pdf"}   #you can specify it as epub also and use a epub reader software

    results = library.search_title_filtered(title,filters)

    item_to_download = results[0]

    download_links = library.resolve_download_links(item_to_download)

    return download_links['Cloudflare']

