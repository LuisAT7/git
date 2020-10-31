from Practica6pt2 import Scraping

if __name__ == "__main__":
	url = 'http://www.fcfm.uanl.mx'
	scraping = Scraping()
	scraping.scrapingImages(url)
	scraping.scrapingPDF(url)
	scraping.scrapingLinks(url)
	#scraping.scrapingBeautifulSoup(url)

"""El código saca las imágenes y pdf's de la página web que se le indique"""


