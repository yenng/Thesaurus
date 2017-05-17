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
    _obj = ObjectProperty()
    def on_node_expand(self,node):
        global word
        word = node.text
    def on_touch_down(self, touch):
        node = self.get_node_at_pos(touch.pos)
        global word
        word = node.text
        return super(MyTreeView, self).on_touch_down(touch)
        
    
class MyWidget(Widget):
    def new(self):
        global word
        global tv
        TestApp().getChildNear(tv, word)

class TestApp(App):
    def build(self):
        return root

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


    def buildTree(self, treeOrigin, node, name):
        add = treeOrigin.add_node
        self.root = []
        l = []
        for x in range(len(node.children)):
            self.root.append(add(TreeViewLabel(text=node.children[x].data, height = 40),
                                 name))
            l.append(TestApp().getNear(node.children[x].data))
            nodeT = l[x].firstNode
            for y in range(len(nodeT.children)):
                add(TreeViewLabel(text=nodeT.children[y].data), self.root[x])

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
window = ScrollView(size_hunt=(1,None), size = (Window.width,Window.height))
root = BoxLayout(orientation='vertical',height = 100)
root.bind(minimum_height=root.setter('height'))
root1 = BoxLayout(orientation='horizontal')
#button1 = Button(text='Exit',size_hint=(.1,.1),on_press=MyWidget.close)
button = Button(text='Generate New List',size_hint=(.1,.1), on_press=MyWidget.new)
tv = MyTreeView(hide_root=True)
TestApp().getChildNear(tv, word)
root1.add_widget(button)
#root1.add_widget(button1)
root.add_widget(tv)
root.add_widget(root1)
window.add_widget(root)
runTouchApp(window)
