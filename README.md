# Introduction
This program finds n-levels of synonyms of a word given by the user and tabulates them in the treeview form. It is written in Python 2.7.13 and Kivy 1.10.0 (graphical user interface library). The synonyms are searched and extracted from the www.thesaurus.com website and tabulate the first 5 of the synonyms found. 

# How it works
Here's the screenshot of the program:

![alt text][Screenshot]

The thesaurus provides a large number of synonyms but we choose only the first 5 for each depth level to reduce wait time. The user input the interested word into the **query word** text input and hit on 'Enter' key or click on 'Generate New List' button. User can expand and collapse the list. Also user can choose a new query word from the list by clicking the word, the new query will be added below the last list. The treeview is scrollable for lengthy list. Any of the searched result can be removed by right-clicking on the **query word** result. By default the depth of search is 2 levels, but user can change that. However, deeper level will result in longer wait time.

# Implementation
The code that parse the html from www.thesaurus.com is in `thesaurus.py`. It uses [BeautifulSoup][1] packages to parse html file. The main program is `FindNearByWordsApp.py`. The synonym are extracted using recursive call of n-level.

# Installation
In order to run this program, the following packages are needed.
 1. Python2
 2. BeautifulSoup package
 3. Kivy

### Kivy installation instruction
Kivy can be downloaded from the official website (https://kivy.org/#download), choose an appropriate version and follow the   instructions. The procedure is pretty straightforward and simple. 
  
  To check whether the installation is working, follow the instructions:
    
    `On a Linux machine:`
      1.Open a terminal.
      2.Run python.
      3.The Python prompt, >>>, should appear. Type import kivy.
      4.The command should print a message similar to [INFO] Kivy v1.8.0.

    `On a Windows box:`
      1.Double-click kivy.bat inside the Kivy package directory.
      2.Type python at the command prompt. 
      3.Type import kivy.
      4.The command should print a message similar to [INFO] Kivy v1.8.0.
      
[Screenshot]: https://github.com/yenng/Dictionary/blob/master/Document/Image/SynonymsExample.PNG 
[1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
