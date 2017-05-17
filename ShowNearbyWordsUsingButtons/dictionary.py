
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import urllib

class Dictionary:

	def getNearbyWord(self,queryWord):
		i=0
		j=0
		#queryWord = "none"
		nearbyList = []
		#nearbyList.append(keyWord)
		queryWord = queryWord.replace(" ", "-")
		nearbyListLink = []
		link = "http://www.dictionary.com/browse/" + queryWord
		nearbyListLink.append(link)
		f = urllib.urlopen(link)
		html = f.read()
		# use beautifulsoup
		soup = BeautifulSoup(html,'html.parser')
		for sectionX in soup.find_all('section'):
			if(sectionX.get('class')==[u'right-rail-nearby-words']):
				#print sectionX.find_all('li')
				for nearby in sectionX.find_all('li'):
					listLink = nearby.a['href']
					if(nearby.a.string != queryWord):
						nearbyList.append(nearby.a.string)
						nearbyListLink.append(listLink)
		#print sectionX
		
		#print link
		#for j in range(0,len(nearbyList)):
		#	print nearbyList[j], '		', nearbyListLink[j]

		self.query = queryWord
		self.near = nearbyList
#	rawWord = raw_input("Enter the word: ")
#	count = input("Enter number	:")
#	run = getNearbyWord(rawWord)
#	print count
"""
run = Dictionary()
run.getNearbyWord(raw_input("Enter the word: "))
print run.key
print run.near
"""
