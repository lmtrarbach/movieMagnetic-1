
import string
from bs4 import BeautifulSoup
from lxml import *
import urllib
import requests
from imdb import IMDb
import urllib2

url="https://thepiratebay.org/search/"
a=IMDb()
for ia in a.get_top250_movies():

	palavra=str(ia)
	req = urllib2.Request(url + palavra + "/")
	req.add_header('User-agent', 'Mozilla 5.10')

	page = urllib2.urlopen(req).read()
	soup = BeautifulSoup(page,'lxml')	
	data = soup.find('tr',{"class" : "alt"})
	if  data is None:
		pass
	else:
		link = data.findAll("a")
		print ia
		print link[3]['href']
	
	




