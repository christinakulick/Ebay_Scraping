<h1>HW3 Scraping From Ebay</h1>

**What It Does**

My `ebay-dl.py` file works to scrape information from ebay and put the info in a json file. It downloads the first 10 pages of a specific search term from ebay and returns the important information about that items that appear from the seach. The json file will shows items such as name, quality status, price, shipping price, if the item can have free returns, and how many of that item have been sold.

**How To Run File**

To run this file open `ebay-dl.py`. In the terminal enter the information below:

```
/usr/local/bin/python3 /Users/christinakulick/Documents/GitHub/HW_03/ebay-dl.py 'search term'
```

To search for a specific item on Ebay enter whatever you would like to seach for in the area 'search term'. Change the term as many times as you would like to generate a new json file.

Here is exactly what I entered to generate my 3 json files:

```
/usr/local/bin/python3 /Users/christinakulick/Documents/GitHub/HW_03/ebay-dl.py 'blankets'
```

```
/usr/local/bin/python3 /Users/christinakulick/Documents/GitHub/HW_03/ebay-dl.py 'nike shoes'
```

```
/usr/local/bin/python3 /Users/christinakulick/Documents/GitHub/HW_03/ebay-dl.py 'water bottle'
```

**Link**

Here is the link to the [course project](https://github.com/mikeizbicki/cmc-csci040/tree/2021fall/hw_03)

_Thank You_
