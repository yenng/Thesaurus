from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.treeview import TreeView, TreeViewLabel, TreeViewNode
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
import dictionary

# Sub class of Kivy treeview 
class MyTreeView(TreeView):
    # This will run, when the label inside the treeview was pressed.
    def on_touch_down(self, touch):
        global queryWord
        global tv
        # This code is to convert the touched position to the touched node.
        node = self.get_node_at_pos(touch.pos)

        # Do nothing if the node is empty
        if node != None:
            # This code is to delete the unwanted query word.
            # Remove node when right click.
            if(touch.button=='right'):
                # Only remove the node that contains 'Query Word: '
                if node.text.find('Query Word:') != -1:
                    tv.remove_node(node)
            # ...Other than right click.
            else:
                # If the clicked node's text contains 'Query Word: ', remove it. 
                if node.text.find('Query Word:')==0:
                    wordInput.text = queryWord = node.text[12:]
                # Otherwise use the complete node's text as the selected new query word
                else:
                    wordInput.text = queryWord = node.text
            # Let parent's on_touch_down() performs its jobs
            return super(MyTreeView, self).on_touch_down(touch)

#This is the main class for this application
class FindNearbyWordApp(App):
    # This is to build the GUI.
    def build(self):
        global tv
        
        # Handle TextInput on_enter event.
        def on_enter(instance):
            global word
            word = wordInput.text
            global count
            count = int(levelInput.text)
            self.beginBuildingTree(tv, word)
            
        # Bind the TextInput to the on_enter().
        wordInput.bind(on_text_validate=on_enter)
        levelInput.bind(on_text_validate=on_enter)
        
        # Create scroll view for treeview.
        scrollView = ScrollView()

        # Create box layout for scrollview.
        svPanel = BoxLayout(orientation='vertical',valign='top',height=100)

        # Create box layout for TextPanel.
        inputPanel = BoxLayout(orientation='horizontal',size_hint=(1,.07))

        # Create box layout for main window.
        windowPanel = BoxLayout(orientation='vertical',valign='top')

        # Create box layout for button.
        buttonPanel = BoxLayout(orientation='horizontal',size_hint=(.5,.1))

        # This function is to handle Generate New List button pressed
        def onPressOfGenerateNewList(self):
            global queryWord
            global tv
            global count
            count = int(levelInput.text)
            queryWord = wordInput.text
            # If the query word is empty.
            if queryWord != '':
                FindNearbyWordApp().beginBuildingTree(tv, queryWord)
                
        # Create button and bind to onPressOfGenerateNewList() event.
        button = Button(text='Generate New List', on_press=onPressOfGenerateNewList)

        # Bind the minimum height to treeview height.
        tv.bind(minimum_height = tv.setter('height'))

        '''_________________________________
          | wordInput       |   levelInput  | <<< inputPanel
          |_________________|_______________|
          |            scrollView           |
          |  _____________________________  | <<< svPanel
          | |                             | |
          | |              tv             | |
          | |           (treeview)        | |
          | |_____________________________| |
          |_________________________________|
          | _____________                   |
          ||    button   |                  | <<< buttonPanel 
          ||_____________|                  |
          |_________________________________|
        '''
        buttonPanel.add_widget(button)
        scrollView.add_widget(tv)
        inputPanel.add_widget(wordInput)
        inputPanel.add_widget(levelInput)
        svPanel.add_widget(scrollView)
        windowPanel.add_widget(inputPanel)
        windowPanel.add_widget(svPanel)
        windowPanel.add_widget(buttonPanel)
        return windowPanel

    # Get a list of nearby words from Dictionary.
    def getNear(self,queryWord):
        dic = dictionary.Dictionary()
        dic.getNearbyWord(queryWord)
        nearbyWords = []
        for i in range(len(dic.near)/2):
            nearbyWords.append(dic.near[i])
        return nearbyWords

    # Build a treeview of nearby words recursively.
    def buildTree(self, treeOrigin, queryWord, parentNode, level):
        # This is a recursive function to extract n-level of nearby words from Dictionary
        def addNode(treeOrigin, queryWord, parentNode, level):
            # Abbreviate add_node function of treeOrigin object.
            add = treeOrigin.add_node
            myNodex = []

            # Recursively add into treeview until nodes of all level have been fully added
            if level > 0:
                nearbyWords =  self.getNear(queryWord)
                for x in range(len(nearbyWords)):
                    myNode=add(TreeViewLabel(text=nearbyWords[x], height = 40,
                                                       size_hint_y=None), parentNode)
                    addNode(treeOrigin, nearbyWords[x], myNode, level-1)
        # Run the recursive function
        addNode(treeOrigin, queryWord, parentNode, level)

    # Start building the tree of nearby words
    def beginBuildingTree(self, treeOrigin,queryWord):
        global count
        add = treeOrigin.add_node
        name = add(TreeViewLabel(text='Query Word: '+ queryWord,
                                      is_open=True))
        self.buildTree(treeOrigin, queryWord, name,count)




# Global variable.
count = 0
word = ''
tv = MyTreeView(root_options=dict(text='Nearby Words'),hide_root=True,size_hint = (1,None))
wordInput = TextInput(multiline=False)
levelInput = TextInput(multiline=False,text='2')

# Run the application
FindNearbyWordApp().run()
