#author: aaron
#scrapes listingname,link,price sold, shipping cost. outputs to csv. please dont look at this code cuase i dont know what i was doing :))

from bs4 import BeautifulSoup
from string import whitespace
import cookielib
import urllib2
import mechanize
import sys
import requests

reload(sys)
sys.setdefaultencoding('utf8')
#hahaha what am i doing

#browser setup (opens "browser" for us to read html files)
class User(object):
    def __init__(self):
        self.br = mechanize.Browser() # browser object
        self.br.addheaders = [("User-agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)")]
        self.cookies = cookielib.LWPCookieJar()
    
    def searchItem(self, url, search, ofile):
        self.br.open(url)
        self.br.set_handle_robots(False)
        self.br.select_form(nr=0)
        self.br["_nkw"] = search
        self.br.submit() # searches for whatever is wanted to be found
        newurl = self.br.geturl() + "&LH_Complete=1&LH_Sold=1" # set url to show only SOLD listings
        newurl.replace("https", "http")
        self.br.open(newurl)
        
        r = requests.get(self.br.geturl())
        
        soup = BeautifulSoup(r.content,"lxml")
        soup.encode("utf-8")
        
        listcontainer = soup.find_all("li", {"class":"sresult lvresult clearfix li"}) 
        
        for item in listcontainer:
            for string in item.h3.a.stripped_strings: #print name
                newstring = (repr(string)).replace("u'","").replace("'","")
                ofile.write((newstring)+"\t")
            ofile.write(item.h3.a.get("href")+"\t")               #print link
            for string in item.ul.li.span.stripped_strings:
                newstring = (repr(string)).replace("u'","").replace("'","")
                ofile.write((repr(newstring))+"\t")                  #print price
            for string in item.ul.li.find_next_sibling("li").find_next_sibling("li").span.stripped_strings:
                newstring = (repr(string)).replace("u'","").replace("'","")
                ofile.write((repr(newstring))+"\n")                  #print shipping price
                
        print "Completed searching for item: " + search
        
if __name__ == "__main__":
    bot = User()
    url = "http://www.ebay.com"
    
    with open("itemList.txt") as f:
        item = f.readline()
        while item:
            thing = item
            thing.split()
            thing = "_".join(thing.split())
            ofile = open(thing+".tsv","w+")
            bot.searchItem(url,item,ofile)
            ofile.close()
            item = f.readline()
            
    print "We outta here"
    
        
