from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty, \
    AliasProperty, NumericProperty, ReferenceListProperty
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode
from kivy.app import App
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
        

    
    
        


class TestApp(App):    
    def build(self):
        #button = Button(text='testing')
        tv = TreeView(hide_root=True, Scroll = True)
        TestApp().getChildNear(2,tv, word)
        return tv

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
            self.root.append(add(TreeViewLabel(text=node.children[x].data),
                                 name))
            l.append(TestApp().getNear(node.children[x].data))
            nodeT = l[x].firstNode
            for y in range(len(nodeT.children)):
                add(TreeViewLabel(text=nodeT.children[y].data), self.root[x])

    def getChildNear(self, count, treeOrigin,queryWord):
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
TestApp().run()
