Ebay Item value scraper

Need the following py packages
1. BeautifulSoup4 (pip install beautifulsoup4)
2. mechanize (pip install mechanize)
3. requests (pip install requests)
4. lxml (pip install lxml)

Need the following files (if using unmodified scraper.py)
1. itemList.txt

To run:
1. Enter items to be searched in itemList.txt. Each item has its own line. See the demoItemList.txt as a guide
2. Run the scraper by calling the following line: scraper.py
3. Once script is completed, a csv file will be generated for each item searched.


BUGS/ISSUES:
1. Strings have a "'" appended to them (price and shipping)
3. Numbers are represented as a String and not a double/float

This was made in like a day or so, so excuse the poor coding
