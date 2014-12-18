import re
import httplib
import urllib2
from urlparse import urlparse
import BeautifulSoup
from youtube import *


regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

reg = re.compile(
	r'^/watch?v='
	, re.IGNORECASE)

def isValidUrl(url):
    if (url.find("watch?v=") == 1):
        return True;
    return False

def crawler(SeedUrl):
    tocrawl=[SeedUrl]
    crawled=[]
    while tocrawl:
        page=tocrawl.pop()
        print 'Crawled:'+page
	if(SeedUrl != page):
		print "Starting download of page : " + str(page) + "\n"
		download(page)

        pagesource=urllib2.urlopen(page)
        s=pagesource.read()
        soup=BeautifulSoup.BeautifulSoup(s)
        links=soup.findAll('a',href=True)
        if page not in crawled:
            for l in links:
     		if isValidUrl(l['href']):
                	print "Valid Link: " + str(l['href'])
			tocrawl.append("https://www.youtube.com" + str(l['href']))
            crawled.append(page)   
    return crawled

crawler('https://www.youtube.com/results?search_query=drums')
