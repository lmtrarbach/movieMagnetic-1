
import re

from django.shortcuts import render
from django.template import loader, Context
from models import *
from imdb import IMDb
from tpb import CATEGORIES, ORDERS
import urllib2
import string
from bs4 import BeautifulSoup
from lxml import *
import requests
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import template
import urllib
import requests
from django.views.decorators.cache import cache_page
from django.core.cache import cache

register = template.Library()

# Create your views here.

#######################################################################
##############The Home function #####################################
########################################################################
@cache_page(60 * 3000)
def home(request):
        url= "http://www.imdb.com/?ref_=nv_home"
        req = urllib2.Request(url)
        req.add_header( 'User-agent','Mozilla 5.10') 
	req.add_header("Accept-Language" ,"en-us,en;q=0.5")
	page = urllib2.urlopen(req).read()

        soup =BeautifulSoup(page,'lxml')
        find = soup.find('div',{ "class" : "rhs-body" })
        movie=find.findAll('div',{ "class" : "title" })
    
	thriler=soup.find('div',{ "class" : "ninja_left" })
	th_each=soup.find('img',{ "class" : "pri_image" })
	video=[]
        data=[]
	for vd in th_each:
		video.append(vd)
		print vd

        for link in movie:
                title=link.a.text
		sub=link.a['href']
		subt=re.sub('\?p.*$','',sub)
		subtt=re.sub('/title/tt','',subt)
		
		
	      
		data.append([title,subtt])
		print subtt
			
        print link.a.text
	
                      
        return render_to_response("home.html", {"data" : data , "video" : video })

	




     
###########################################################################
###################The Top 250 IMDB function##############################
###########################################################################
@cache_page(60 * 3000)
def rankingIMDB(request):
	# If a search will looking for the Movie and his magneticc
      
	url= "http://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3021371422&pf_rd_r=16YTZRM8JHHR7TQBRW24&pf_rd_s=right-4&pf_rd_t=15506&pf_r$"
	req = urllib2.Request(url)
	req.add_header( 'User-agent' , 'Mozilla 5.10') 
	req.add_header( "Accept-Language" , "en-us,en;q=0.5" )

	page = urllib2.urlopen(req).read()

    	soup = BeautifulSoup(page,'lxml')
    	find = soup.find('tbody',{ "class" :"lister-list" })
    	movie=find.findAll('tr')
    	data=[]
    	for link in movie:
	    	title=link.find('td',{"class" : "titleColumn"})
	    	image=link.find('td',{"class" : "posterColumn"})
	    	print title.a.text
        	data.append([title.a.text,image.a.img['src'] ])

		      
    	return render_to_response("pagina_lista.html", {"data" : data })
       

########################################################################
######################################################################
###################The main IMDB funcion##############################
######################################################################	
#@cache_page(60 * 3000)
def listaopcao(request):
	keyword=request.GET['search']
	data=[]
        a=IMDb('mobile')
        for ia in a.search_movie(keyword, results=15):

                data.append(ia.data['title'].encode('utf-8'))
	print keyword
	return render_to_response("pagina_lista.html", {"data" : data })
#####################################################################################################################################
###########Error Handler#####################################################
############################################################################
def ops(request):
	return render_to_response("ops.html")	


###################################################################
#############Function Games#######################################
################################################################	
#This function will check the request if is a search or a new acess	
def games(request):
	try:
# If was a new acess will redirect to the home page
		url= "http://thegamesdb.net/api/GetPlatformsList.php"
		req = urllib2.Request(url)
		req.add_header('User-agent', 'Mozilla 5.10')
		soup = BeautifulSoup(page,'xml')
		datas = soup.findAll("Platform")
		data=[]
		for plataform in datas:
			data.append([plataform.id, plataform.name])
			print plataform.id					
                return render_to_response("gamehome.html",{ "data" : data })
	except:
		mensagem = "Erro nas plataforms"
                return render_to_response("ops.html")

		
'''
		else:
# If a search will looking for the game and his magnetic
			try:
				palavra= request.GET['search']
                		url= "http://thegamesdb.net/api/GetGamesList.php?name="
                		req = urllib2.Request(url + palavra + "")
                		req.add_header('User-agent', 'Mozilla 5.10')

                		page = urllib2.urlopen(req).read()
                		soup = BeautifulSoup(page,'xml')
                		datas = soup.findAll("GameTitle")
				data=[]
                		for title in datas:
                        		data.append(title.text)
				return render_to_response("pagina_lista.html", {"data" : data })
        		except:
                		mensagem = "Problemas na procura"
				return render_to_response("ops.html")
# this check is for the first time also
	else:
		data=plataformGames.objects.all()
		return render_to_response("gamehome.html", { "data" : data })
'''

####################################################################################################################################################
#####################################################################################################################################################
##################################  Games by Genre  #################################################################################################
####################################################################################################################################################
def gamesByGenre(request,string):
	url="http://thegamesdb.net/api/GetPlatformGames.php?platform="
	req = urllib2.Request(url + string)
	req.add_header('User-agent', 'Mozilla 5.10')
	req.add_header("Accept-Language" ,"en-us,en;q=0.5")
	page = urllib2.urlopen(req).read()
        soup = BeautifulSoup(page,'xml')
	datas=soup.findAll('Game')
	data=[]
	for game in datas:
		data.append([game.id,game.GameTitle])
	return render_to_response("game_lista.html", { "data" : data })


def movies(request):
	data=genreMovies.objects.all()
	if request.method == 'GET' and 'search' in request.GET:
		return listaopcao(request)
	else:
		return render_to_response("serieshome.html", { "data" : data })	
#######################################################################
#############Functions TV series
########################################################################
#### This function test if have a query in the resquest and define the way.
def series(request):
	data=genreSeries.objects.all()
	if request.method == 'GET' and 'search' in request.GET:
		return listaopcao(request)			

	else:

		return render_to_response("serieshome.html", { "data" : data }) 
##############################################################################
def topSeries(request):
	
# If a search will looking for the game and his magneticc
	try:
                url= "http://www.imdb.com/chart/toptv/?ref_=nv_tvv_250_3"
                req = urllib2.Request(url)
                req.add_header('User-agent', 'Mozilla 5.10')
		req.add_header("Accept-Language" ,"en-us,en;q=0.5")
                page = urllib2.urlopen(req).read()
                soup = BeautifulSoup(page,'lxml')
                find = soup.findAll('td',{"class" : "titleColumn"})
		data=[]
                for link in find:
          	      data.append(link.text)
                return render_to_response("pagina_lista.html", {"data" : data })
	except:
        	mensagem = "Problemas na procura"
                return render_to_response("ops.html")

##############################################################################
####################Movies by genre###########################################
#############################################################################
def moviesByGenre(request,string):
	try:
		genre=string
		url1="http://www.imdb.com/search/title?genres="
        	url2="&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2406822102&pf_rd_r=097SZEKQSMJ1ZM0M0WNX&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1"
		req = urllib2.Request(url1 + genre + url2)
		req.add_header('User-agent', 'Mozilla 5.10')
		req.add_header("Accept-Language" ,"en-us,en;q=0.5")
                page = urllib2.urlopen(req).read()
                soup = BeautifulSoup(page,'lxml')
                find = soup.findAll('div',{"class" : "lister-item mode-advanced"})
                data=[]
                for link in find:
                      	data.append([link.a[1].text])
                return render_to_response("pagina_lista.html", {"data" : data })

        except:
                mensagem = "Problemas na procura"
                return render_to_response("ops.html")

	
##############################################################################
########################Tv Series by genre####################################
##############################################################################

def seriesByGenre(request,string):
	try:
        	genre=string
		cache.clear()

                url1="http://www.imdb.com/search/title?genres="
		url2="&sort=user_rating,desc&title_type=tv_series,mini_series&num_votes=5000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2295992002&pf_rd_r=05WDJCMYKW0ZNKA75CE1&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_gnr_1"
                req = urllib2.Request(url1 + genre + url2)
                req.add_header('User-agent', 'Mozilla 5.10')
		req.add_header("Accept-Language" ,"en-us,en;q=0.5")
                page = urllib2.urlopen(req).read()
                soup = BeautifulSoup(page,'lxml')
                find = soup.findAll('div',{"class" : "lister-item mode-advanced"})

               
		data=[]
		
                for link in find:
			
			clean = link.a.get('href').replace('/title/','')
			clean2=clean.replace('/?ref_=adv_li_tt','')
			image=link.find('img',{ "class" : "loadlate" })
                        data.append([link.h3.a.text, clean2, image['loadlate']])
			
			
			
                return render_to_response("serie_lista.html", {"data" : data })
	


	except:
                mensagem = "Problemas na procura"
                return render_to_response("ops.html")
##############################################################################
##############################################################################
##################TV show detail##############################################
##############################################################################
def seriesByDetail(request,id):
        try:
                genre=id
                cache.clear()

                url1="http://www.imdb.com/title/"
                url2="/?ref_=adv_li_tt"                
		req = urllib2.Request(url1 + genre + url2)
                req.add_header('User-agent', 'Mozilla 5.10')
		req.add_header("Accept-Language" ,"en-us,en;q=0.5")
                page = urllib2.urlopen(req).read()
                soup = BeautifulSoup(page,'lxml')
                find = soup.findAll('div',{"class" : "seasons-and-year-nav"})
		titleWraper=soup.findAll('div',{"class" : "title_wrapper"})
		title=titleWraper[0].h1.text
		getPoster=soup.findAll('div',{"class" : "poster"})

		poster=str(getPoster[0].a.img['src'])

                data=[]

                for link in find:
                	for ia in link.findAll('a'):
				
				if re.search('year',str(ia)):
					continue
				else:
					text=ia.text
					
					clean=str(ia.get('href'))
					
    					href= re.sub('&ref_=tt_eps_sn_\d+','',clean)
					re.escape
					hra= re.sub('episodes?season=','',href)
					data.append([text,hra])
					
		return render_to_response("detalhes_serie.html", {"data" : data , "title" : title, "poster" : poster })



        except:
		mensagem = "Problemas na procura"


        	return render_to_response("ops.html")

###############################################################################
###############################################################################
##################TV show season###############################################
###############################################################################

def seasonSeries(request,id,season):
	title=id
	seasons=season
        url1="http://www.imdb.com/title/"
        url2="/episodes?season=" 
        req = urllib2.Request(url1 + title + url2 + seasons)
        req.add_header('User-agent', 'Mozilla 5.10')
	req.add_header("Accept-Language" ,"en-us,en;q=0.5")
        page = urllib2.urlopen(req).read()
        soup = BeautifulSoup(page,'lxml')
        find = soup.findAll('div',{ "class" : "list_item odd" })
	magn= soup.find('div',{ "class" : "subpage_title_block" })
	 
	data=[]
	link=magn.find('div',{ "class" : "parent" })
	ht=link.h3.a.text

	eplink= " " + ht + " "  
	episode=find
	
	for ia in episode:
		
		
	
		image=ia.find('a',{"itemprop" : "url" })
		linkMag=image.find('div')
		#subtitle=find.find('div',{ "class" : "info" })
		#subtt=subltitle.strong.a['href']
		im=image.find('img',{ "class" : "zero-z-index" })
		slang=re.sub(', Ep', 'E0',str(linkMag.div.text))
		magnetic= eplink.encode('utf-8') +  re.sub('S', 'S0',slang).encode('utf-8')
		data.append([ia.meta['content'],im['src'],magnetic])
		
	
	return render_to_response("episodeSeason.html", { "data" : data })
	




##########################################################################################################################
##########################################################################################################################
##################################### Movies By Detail####################################################################
##########################################################################################################################

#http://www.imdb.com/title/tt2975590/?ref_=nv_sr_1
@cache_page(60 * 3000)
def moviesByDetail(request,id):
	
	genre=id
                

        url1="http://www.imdb.com/title/"
        url2="/?ref_=nv_sr_1"
        req = urllib2.Request(url1 + genre + url2)
 	
        req.add_header('User-agent', 'Mozilla 5.10')
       	req.add_header("Accept-Language" ,"en-us,en;q=0.5")
        page = urllib2.urlopen(req).read()
        soup = BeautifulSoup(page,'lxml')
        find = soup.find('div',{"class" : "slate_wrapper"})
        getPoster=soup.find('div',{"class" : "poster"})
        

        poster=str(getPoster.a.img['src'])
	
	
	titl=str(getPoster.a.img["title"])
	title=titl.replace('Poster','')


	
        
	print title
	print poster
        return render_to_response("detalhe.html", {"title" : title , "poster" : poster })



       
         























































