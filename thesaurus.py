from bs4 import BeautifulSoup
import urllib

# Get the nearby words from www.thesaurus.com
class Thesaurus:
  def getNearbyWord(self,queryWord):
    count = 10
    # Create an array to store all synonyms
    nearbyList = []
    
    # Replace all ' ' with '-' in the query word
    queryWord = queryWord.replace(" ", "-")

    # Create the link that connect to www.thesaurus.com with given query word
    self.link = "http://www.thesaurus.com/browse/" + queryWord

    # Open the url and read the html
    f = urllib.urlopen(self.link)
    html = f.read()
    
    # Pass html using beautifulsoup
    soup = BeautifulSoup(html,'html.parser')
    for divClass in soup.find_all('div'):
      # Travese the html parse tree to relevancy-list section
      if(divClass.get('class')==[u'relevancy-list']):
        # Extract all nearby words.
        for nearby in divClass.find_all('li'):
          if count > 0:
            if(nearby.a.string != queryWord):
              nearbyList.append(nearby.span.string)
            count-=1
        break

    self.query = queryWord
    self.near = nearbyList
'''
syn = Thesaurus()
syn.getNearbyWord('test')
print syn.near'''
