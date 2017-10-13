#!/usr/bin python
from django.shortcuts import render
from django.template import loader, Context
from imdb import IMDb
from tpb import CATEGORIES, ORDERS
import ssl

import urllib2
import string
from bs4 import BeautifulSoup
from lxml import *
import requests
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import template

register = template.Library()

@register.filter(name='magnetize')
def magnetize(ia):
	
 
	try:

		palavra=ia

        	ctx = ssl.create_default_context()
        	ctx.check_hostname = False
        	ctx.verify_mode = ssl.CERT_NONE

       
       		url= "https://thepiratebay.org/search/"

        	req = urllib2.Request(url + palavra + "/")
        	req.add_header('User-agent', 'Chrome/44.0.2403.107')
        	page = urllib2.urlopen(req,context=ctx).read()
        	soup = BeautifulSoup(page,'lxml')
        	data = soup.findAll("a",{"title" : "Download this torrent using magnet"})
        	print data[0]['href']
		magnetic = data[0]['href']
		return magnetic
	except:
		return "//ops"

'''
@register.filter(name='legendize')
def legendize(ia):
	try:
		palavra=ia
		url="https://www.opensubtitles.org/pt/search/sublanguageid-por,pob/imdbid-"
		req = urllib2.Request(url + palavra)
		req.add_header('User-agent', 'Mozilla 5.10')
		page = urllib2.urlopen(req).read()
		soup = BeautifulSoup(page,'lxml')
		body=soup.find('tr',{"class" : 'change even expandable'})
		td=body.findAll('td',{ "align" : "center"})
				
		data=td[4].a['href']
		print data
		return data
		
	except:
		return "/../ops"


'''

	
        



        
