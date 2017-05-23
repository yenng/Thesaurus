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

    `On a Windows10 OS:`
      1. Ensure you have the latest pip and wheel:
        python -m pip install --upgrade pip wheel setuptools
      2. Install the dependencies (python2):
        python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
      3. Install kivy:
        python -m pip install kivy
      4. Make sure kivy successfully installed
        C:\Users\user3>python
        Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import kivy
        [INFO   ] [Logger      ] Record log in C:\Users\user3\.kivy\logs\kivy_17-05-23_0.txt
        [INFO   ] [Kivy        ] v1.10.0
        [INFO   ] [Python      ] v2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)]
        >>>
        * If the message above appeared, kivy is installed succesfully
        
      Note:
        If you encounter any permission denied errors, try opening the Command prompt as administrator and trying again.

    `On a Ubuntu-16 OS:`
      1. Add a stable build PPAs
        $ sudo add-apt-repository ppa:kivy-team/kivy
      2. Update your package list using your package manager
        $ sudo apt-get update
      3. Install Kivy for python2 (python2 is used in this project)
        $ sudo apt-get install python-kivy
      4. Make sure kivy successfully installed.
        $ python
        >>> import kivy
        Purge log fired. Analysing...
        Purge finished!
        [INFO   ] [Logger      ] Record log in C:\Users\user3\.kivy\logs\kivy_17-05-23_0.txt
        [INFO   ] [Kivy        ] v1.10.0
        [INFO   ] [Python      ] v2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)]
        >>>
        * If the message above appeared, kivy is installed succesfully

[Screenshot]: https://github.com/yenng/Dictionary/blob/master/Document/Image/SynonymsExample.PNG 
[1]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
