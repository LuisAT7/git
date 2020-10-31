# -*- encoding: utf-8 -*-
#class for scraping

import os

import requests
from lxml import html
from bs4 import BeautifulSoup

#import urlparse

class Scraping:
    
    def scrapingBeautifulSoup(self,url):
    
        try:
            print("Obteniendo las imagenes con BeautifulSoup "+ url)
            
            response = requests.get(url)
            bs = BeautifulSoup(response.text, 'lxml')
            
            os.system("mkdir images")
            
            for tagImage in bs.find_all("img"): 
                if tagImage['src'].startswith("http") == False:
                    download = url + tagImage['src']
                else:
                    download = tagImage['src']
                print(download)
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
        
        except Exception as e:
                print(e)
                print("Error conexion " + url)
                pass
				
    def scrapingImages(self,url):
        print("\nObteniendo imagenes de la url:"+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)
            images = parsed_body.xpath('//img/@src')

            print ('Imagenes %s encontradas' % len(images))
            os.system("mkdir images")
            for image in images:
                if image.startswith("http") == False:
                    download = url + image
                else:
                    download = image
                print(download)
                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
                
        except Exception as e:
                print(e)
                print ("Error conexion con " + url)
                pass
            
    def scrapingPDF(self,url):
        print("\nObteniendo pdfs de la url:"+ url)
    
        try:
            response = requests.get(url)  
            parsed_body = html.fromstring(response.text)
            pdfs = parsed_body.xpath('//a[@href[contains(., ".pdf")]]/@href')
            if len(pdfs) >0:
                os.system("mkdir pdfs")
        
            print ('Encontrados %s pdf' % len(pdfs))
                
            for pdf in pdfs:
                if pdf.startswith("http") == False:
                    download = url + pdf
                else:
                    download = pdf
                print(download)
                r = requests.get(download)
                f = open('pdfs/%s' % download.split('/')[-1], 'wb')
                f.write(r.content)
                f.close()
    
        except Exception as e:
            print(e)
            print("Error conexion con " + url)
            pass
    
    def scrapingLinks(self,url):
            print("\nObteniendo links de la url:"+ url)
        
            try:
                response = requests.get(url)  
                parsed_body = html.fromstring(response.text)
                links = parsed_body.xpath('//a/@href')
    
                print('links %s encontrados' % len(links))
    
                for link in links:
                    print(link)
                    
            except Exception as e:
                    print(e)
                    print("Error conexion con " + url)
                    pass
