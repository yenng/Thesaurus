# programmer: yen

import unittest
import dictionary

run = dictionary.Dictionary()
nearbyWordForLove = ['lovable','lovably','lovage','lovastatin','lovat',
                     'love affair','love apple','love arrows','love at first sight',
                     'love beads']
nearbyWordForTest = ['tesseract','tesserae','tessie','tessin','tessitura',
                     'test act','test ban','test blank','test card',
                     'test case']
class TestStringMethods(unittest.TestCase):
    def test_key_word(self):
        run.getNearbyWord('love')
        self.assertEqual('love',run.query)
    
    def test_1st_nearby_word_of_love(self):
        run.getNearbyWord('love')
        self.assertEqual('lovable',run.near[0])
    
    def test_2nd_nearby_word_of_love(self):
        run.getNearbyWord('love')
        self.assertEqual('lovably',run.near[1])
    
    def test_3rd_nearby_word_of_love(self):
        run.getNearbyWord('love')
        self.assertEqual('lovage',run.near[2])

    def test_all_nearby_word_of_love(self):
        run.getNearbyWord('love')
        for x in range(len(nearbyWordForLove)):
            self.assertEqual(nearbyWordForLove[x],run.near[x])

    def test_1st_nearby_word_of_test(self):
        run.getNearbyWord('test')
        self.assertEqual('tesseract',run.near[0])

    def test_all_nearby_word_of_test(self):
        run.getNearbyWord('test')
        for x in range(len(nearbyWordForTest)):
            self.assertEqual(nearbyWordForTest[x],run.near[x])

    def test_website_link_for_test(self):
        run.getNearbyWord('test')
        self.assertEqual('http://www.dictionary.com/browse/test',run.link)

    #'love affair' are two seperate words, website will replace the ' ' to '-'
    def test_website_link_for_love_affair(self):
        run.getNearbyWord('love affair')
        self.assertEqual('http://www.dictionary.com/browse/love-affair',run.link)
    
    def test_website_link_for_love_at_first_sight(self):
        run.getNearbyWord('love at first sight')
        self.assertEqual('http://www.dictionary.com/browse/love-at-first-sight',
                         run.link)
    
if __name__ == '__main__':
    unittest.main()
