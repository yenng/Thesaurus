from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.treeview import TreeView
import dictionary

run = dictionary.Dictionary()


    
def result(self, near):
    self.root.ids.near0.text = run.near[0]
    self.root.ids.near1.text = run.near[1]
    self.root.ids.near2.text = run.near[2]
    self.root.ids.near3.text = run.near[3]
    self.root.ids.near4.text = run.near[4]
    self.root.ids.near5.text = run.near[5]
    self.root.ids.near6.text = run.near[6]
    self.root.ids.near7.text = run.near[7]
    self.root.ids.near8.text = run.near[8]
    self.root.ids.near9.text = run.near[9]

class DictionaryApp(App):        
    def confirmEnter(self):
        run.getNearbyWord(self.root.ids.queryWord.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near0(self):
        run.getNearbyWord(self.root.ids.near0.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near1(self):
        run.getNearbyWord(self.root.ids.near1.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near2(self):
        run.getNearbyWord(self.root.ids.near2.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near3(self):
        run.getNearbyWord(self.root.ids.near3.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near4(self):
        run.getNearbyWord(self.root.ids.near4.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near5(self):
        run.getNearbyWord(self.root.ids.near5.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near6(self):
        run.getNearbyWord(self.root.ids.near6.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near7(self):
        run.getNearbyWord(self.root.ids.near7.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near8(self):
        run.getNearbyWord(self.root.ids.near8.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)

    def near9(self):
        run.getNearbyWord(self.root.ids.near9.text)
        self.root.ids.queryWord.text=run.query
        result(self,run.near)
        
DictionaryApp().run()
