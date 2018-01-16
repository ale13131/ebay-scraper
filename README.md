Ebay Item value scraper

Need the following py packages
-BeautifulSoup4 (pip install beautifulsoup4)
-mechanize (pip install mechanize)
-requests (pip install requests)

Need the following files (if using unmodified scraper.py)
-itemList.txt

To run:
1. Enter items to be searched in itemList.txt. Each item has its own line. See the demoItemList.txt as a guide
2. Run the scraper by calling the following line
			scraper.py
3. Once script is completed, a csv file will be generated for each item searched.


BUGS/ISSUES:
1. Strings have a "u'" prepended and a "'" appended to them (item names, price and shipping)
2. Item names with a ',' character will cause the csv to add an extra column
3. Numbers are represented as a String and not a double/float

