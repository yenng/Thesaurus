from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty, \
    AliasProperty, NumericProperty, ReferenceListProperty
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.base import runTouchApp, stopTouchApp
from kivy.uix.textinput import TextInput
from kivy.graphics import Color
import dictionary



class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        
    def addChild(self, obj):
        self.children.append(obj)

    def printCurrentNode(self):
        for x in range(len(self.children)):
            print self.children[x].data


        
class List:
    def __init__(self,fnode):
        self.firstNode = fnode

    def addNode(self, newNode, location):
        node = self.firstNode
        if len(node.children)>location:
            node.children[location] = newNode.firstNode
        

class MyTreeView(TreeView):
    def on_node_expand(self,node):
        global word
        word = node.text
    def on_touch_down(self, touch):
        node = self.get_node_at_pos(touch.pos)
        global word
        global tv
        # This code is to delete the unwanted query word
        if(touch.button=='right'):
            # Only remove the node that contains "Query Word:"
            if node.text.find('Query Word:')==0:
                tv.remove_node(node)
        if node != None:
            word = node.text
        return super(MyTreeView, self).on_touch_down(touch)
        
    
class MyWidget(Widget):
    def new(self):
        global word
        global tv
        TestApp().getChildNear(tv, word)##############

class TestApp(App):
    def build(self):
        return 

    def getNear(self,queryWord):
        run = dictionary.Dictionary()
        run.getNearbyWord(queryWord)
        node = Node(queryWord)
        wordList = List(node)
        for x in range(len(run.near)):
            b = Node(run.near[x])
            wordList.addNode(b,x)
            node.addChild(b)
        #print node.children
        return wordList

                        #tv,        
    def buildTree(self, treeOrigin, node, name):
        add = treeOrigin.add_node
        self.root = []
        l = []
        for x in range(len(node.children)):
            self.root.append(add(TreeViewLabel(text=node.children[x].data, height = 40,
                                               size_hint_y=None), name))
            l.append(TestApp().getNear(node.children[x].data))
            nodeT = l[x].firstNode
            for y in range(len(nodeT.children)):
                add(TreeViewLabel(text=nodeT.children[y].data, size_hint_y=None),self.root[x])

    def getChildNear(self, treeOrigin,queryWord):
        wordList = TestApp().getNear(queryWord)
        node = wordList.firstNode
        add = treeOrigin.add_node
        self.queryWord = add(TreeViewLabel(text='Query Word: '+ node.data,
                                      is_open=True))

        nearbyWord = []
        
        for i in range(len(node.children)):
            nearbyWord.append(node.children[i].data)
        TestApp().buildTree(treeOrigin, node, self.queryWord)
        #node.printCurrentNode()

word = raw_input('Enter the word: ')
tvPanel = ScrollView(size_hint=(1,None),Color=(0,1,0,1))
tvBox = BoxLayout(orientation='vertical',valign='top',height=100)
boxPanel = BoxLayout(orientation='vertical',valign='top')
butPanel = BoxLayout(orientation='horizontal',size_hint=(1,.1))
button = Button(text='Generate New List', on_press=MyWidget.new)
#button = Button(text='Generate New List',size_hint=(.1,.1), on_press=MyWidget.new)
tv = MyTreeView(root_options=dict(text='Nearby Words'),hide_root=True)
tv.size_hint = 1,None
tv.bind(minimum_height = tv.setter('height'))
TestApp().getChildNear(tv, word)
butPanel.add_widget(button)
tvPanel.add_widget(tv)
#boxPanel.add_widget(butPanel)
tvBox.add_widget(tvPanel)
boxPanel.add_widget(tvBox)
boxPanel.add_widget(butPanel)
runTouchApp(boxPanel)
