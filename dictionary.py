from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
import urllib

# Get the nearby words from www.dictionary.com
class Dictionary:
  def getNearbyWord(self,queryWord):
    # Create an array to store all nearby words
    nearbyList = []
    
    # Replace all ' ' with '-' in the query word
    queryWord = queryWord.replace(" ", "-")

    # Create the link that connect to www.dictionary.com with given query word
    self.link = "http://www.dictionary.com/browse/" + queryWord

    # Open the url and read the html
    f = urllib.urlopen(self.link)
    html = f.read()
    
    # Pass html using beautifulsoup
    soup = BeautifulSoup(html,'html.parser')
    for sectionClass in soup.find_all('section'):
      # Travese the html parse tree to nearby words section
      if(sectionClass.get('class')==[u'right-rail-nearby-words']):
        # Extract all nearby words.
        for nearby in sectionClass.find_all('li'):
          if(nearby.a.string != queryWord):
            nearbyList.append(nearby.a.string)

    self.query = queryWord
    self.near = nearbyList
