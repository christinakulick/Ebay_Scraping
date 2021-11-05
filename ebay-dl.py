import argparse
from typing import Text
import requests
from bs4 import BeautifulSoup
import json

def parse_itemssold(text):
    '''
    takes as input a string and returns the number of items sold, as specified in the string
    
    >>> parse_itemssold('47 sold')
    47
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers =''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0

def parse_price(text):
    '''
    >>> parse_price('$5.69 to $6.09')
    $5.69
    '''
 
    numbers =''
    for char in text:
        if char in '1234567890':
            numbers += char
    if '$' in text:
        return '$' + str(int(numbers)/100)
    elif 'to' in text:
        price_str = str(int(numbers)/100)
        i = price_str.index(" ")
        return '$' + price_str[:i]
        
def parse_shipping(text):
        
        numbers =''
        for char in text:
            if char in '1234567890':
                numbers += char
        if '$' in text:
            return '$' + str(int(numbers)/100)
        elif 'Free' in text:
            return 0

if __name__ == '__main__':


    #this if statement says only run the code below when the python file is run "normally"
    #where normally means not in the docs tests


    # get command line arguments
        parser = argparse.ArgumentParser(description='Dowload information from ebay and concert to Json')
        parser.add_argument('search_term')
        parser.add_argument('--num_pages', default = 10)
        args = parser.parse_args()
        print('args.search_term=', args.search_term)

        #list of all items found in all ebay webpages
        items = []

        # loop over all ebay pages
        for pg_num in range(1,int(args.num_pages)+1):

            # build the url
            url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='
            url += args.search_term
            url += '&_sacat=0&_pgn='
            url += str(pg_num)
            url += '&rt=nc'
            print('url=', url)

            # download the html
            r = requests.get(url)
            status = r.status_code
            print('status=', status)
            html = r.text

            # process the html
            soup = BeautifulSoup(html, 'html.parser')
            
            #loop over the items in the page
            tags_items = soup.select('.s-item')
            for tag_item in tags_items:

                name = None
                tags_name = tag_item.select('.s-item__title')
                for tag in tags_name:
                    name = tag.text

                price = None
                tags_price = tag_item.select('.s-item__price')
                for tag in tags_price:
                    price = parse_price(tag.text)

                status = None
                tags_status = tag_item.select('.s-item__subtitle')
                for tag in tags_status:
                    status = tag.text
                
                shipping = None
                tags_shipping = tag_item.select('.s-item__shipping')
                for tag in tags_shipping:
                    shipping = parse_shipping(tag.text)

                freereturns = False    
                tags_freereturns = tag_item.select('.s-item__free-returns')
                for tag in tags_freereturns:
                    freereturns = True

                items_sold = None
                tags_itemssold = tag_item.select('.s-item__hotness')
                for tag in tags_itemssold:
                    items_sold = parse_itemssold(tag.text)

                item = {
                    'name': name,
                    'status': status,
                    'price': price,
                    'shipping': shipping,
                    'free_returns' : freereturns,
                    'item_sold': items_sold, 
                }
                items.append(item)

            print('len(tags_items)=', len(tags_items))
            print('len(items)=', len(items))

            # write the json to a file
            filename = args.search_term+'.json'
            with open(filename, 'w', encoding='ascii') as f:
                f.write(json.dumps(items))

