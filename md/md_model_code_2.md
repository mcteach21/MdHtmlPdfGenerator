ummary:           Python NoteBook
id:                python_notebook
categories:        languages
environments:      dev
status:            tutorial
feedback link:     

# Python (NoteBook)


## Introduction

Python est un langage de programmation populaire, créé par Guido van Rossum (1991). C'est un langage :

* interprété
* open source
* simple

![python](images/python_logo.png)

### Utilisation

* développement web (côté serveur),
* développement de logiciels,
* data science (big data),
* script système.

### Caractéristiques Python

* Python est multi-plates-formes (Windows, Mac, Linux, Raspberry Pi, etc.).
* Python a une syntaxe simple et concise. 
* La syntaxe du code utilise l’indentation.
* Python est un langage interprété.
* Python peut être traité de manière procédurale, orientée objet ou fonctionnelle.

### Installation

Aujourd'hui, la plupart des ordinateurs et systèmes d'exploitation sont livrés avec Python, déjà installé. Pour vérifier si Python est déjà présent sur votre machine, exécutez la commande ci-dessous :

        $ python --version

Si Python n'est pas installé sur la machine, nous pouvons le télécharger gratuitement sur le site Web suivant : [https://www.python.org/](https://www.python.org/).

### Executer du code python

On écrit le code source dans un fichier avec l'extension **.py** et exécuter le fichier à l'aide de la commande 'python' :

hello.py :

        [python]
        print('hello from python!')

![exec](images/python_cmd_exec.png)  

6.2. Code en ligne
Le code Python (simple) peut aussi être exécuté directement dans la console python :

![exec](images/python_console_exec.png)  

### Build

pour créer un exe:
 
        pyinstaller -F script_to_build.py

## Bases du Langage Python

### variables & types

Exemple (script **bases.py**) :

        [python]
        # déclaration variables (typage dynamique)
        title = 'python : bases langage'  # portée globale
        x, y = 0, 0                       # affectation valeurs à plusieurs variables    
        
        # fonction variables (commentaire python)
        def variables():
            title = 'fonction variables'  # portée locale (fonction) : masque variable 'title' globale
            print(title)
            global x, y  # faire référence à variable globale
            x = x + 10
            y = y + 20
        
        if __name__ == '__main__':
            print('***********************************')
            variables()
            print(title)
            print('coordonnées : ' + str(x) + 'x' + str(y)+'!')
            print('coordonnées :  {}x{}!'.format(x, y))      # avec format(..)
        
            print('types : ')
            print(type(title))
            print(type(x).__name__)
            print('***********************************')

![exec](images/python_script_exec_1.png)  


> Python a par défaut les types de données (built-in types) :   
> str (texte) , int, float, complex (num.) , list, tuple, range (sequences), 
> dict, set, frozenset (dict , collections) , bool (booleen), 
> bytes, bytearray, memoryview (binary).    
    
> La définition du type se fait lors de l'affectation :      
  x  = 10    # int    
  pi = 3.14  # float    
  sm = 7j    # complex    

### cast & string

Exemple :

        [python]
        def variables_cast_string():
            x = 2608
            x_txt = str(x)  # cast int -> string
            x_float = float(x)
            x_bool = bool(x)
        
            print(type(x_txt).__name__, type(x_float).__name__, type(x_bool).__name__)
            print(x_txt, x_float, x_bool)
        
            parag = '''
                Ceci est un bloc de texte
                (texte sur plusieurs lignes)
                fin bloc
            '''
            parag = parag.replace('bloc de texte', 'paragraphe')
            print(parag)


![exec](images/python_script_exec_2.png)  

> python dispose de nombreuses fonctions pour le type **string** : 
[voir doc.](https://docs.python.org/2.5/lib/string-methods.html)


### operateurs

liste opérateurs python : 

* \+ : Addition
* \- : Soustraction
* \* : Multiplication 
* / : Division
* % : Modulo 
* ** : Exponentiation
* // : Division entière

## Collections

python fournit 4 types de données pour gérer des collections de données : List, Dict, Set et Tuple.

> Comparatif :    
  * **List** : collection ordonnée et **modifiable**, membres en double acceptés.   
  * **Dict** :  **non** ordonnée et **modifiable**, membres en double **non** acceptés.   
  * **Set** : ordonnée et non indexée, membres en double **non** acceptés.    
  * **Tuple** : ordonnée et **immuable**, membres en double acceptés.   


### List

Exemple :

        [python] 
        # list
        langages = ['Java', 'Python', 'PHP', 'Javascript']
        # langages = list(('Java', 'Python', 'PHP', 'Javascript'))
        
        print(langages, ' : ', len(langages))
        
        langages.append('Kotlin')
        langages.append('C#')
        langages.remove('PHP')
        print(langages, ' : ', len(langages))
        for item in langages:
          print(item)
        
        # accéder aux elements
        print(langages[0])
        print(langages[1:2])
        print(langages[2:])

![exec](images/python_script_exec_3.png)  


#### Création List à partir liste existante

        [python]
        langages = ['Java', 'Python', 'PHP', 'Javascript']
        filtered = [x for x in langages if x != 'Javascript']
        print(filtered)
        
        pairs = [n for n in range(10) if n % 2 == 0]  # range(10) : séquence 10 entiers (0..9)
        print(pairs)

![exec](images/python_script_exec_4.png)  

> liste méthodes pour List : 
[voir doc.](https://docs.python.org/fr/3/tutorial/datastructures.html)

### Dict

Les dictionnaires sont utilisés pour stocker des données sous la forme de paires clé:valeur.

Exemple :

        [python]
        #  Dict
        tuto = {
          "titre": "Python pour débutants",
          "année": 2000,
          "note": 10
        }
        print(tuto)
        print('keys :', tuto.keys())
        print('titre :', tuto.get('titre'))
        
        # tuto['titre'] = 'Python : Initiation!'
        tuto.update({'titre': 'Python : Initiation!'})
        
        print(tuto)
        if 'auteur' not in tuto:
          tuto['auteur'] = 'mc'
        print(tuto)
        
        for k, v in tuto.items():
          print(k, v)
        
        copie = tuto.copy()
        # copie = dict(tuto)
        print(copie)
        
        # imbrication..
        tutos = {
          'tuto1': {
              "titre": "Python : Initiation",
              "année": 2000,
              "note": 8
          },
          'tuto2': {
              "titre": "Python : Perfectionnement",
              "année": 2020,
              "note": 10
          }
        }
        print(tutos)

![exec](images/python_script_exec_5.png)  

> liste méthodes pour Dict : 
[voir doc.](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Set

Un tuple est une collection qui est **non ordonnée** et **non indexée**. Les valeurs en double sont **interdites**.

Exemple :

        [python] 
        #   set
        libraries = {'Pandas', 'Numpy', 'Scikit Learn', 'Matpolib', 'Seaborn'}
        # libraries = set(('Pandas', 'Numpy', 'Scikit Learn', 'Matpolib', 'Seaborn'))
        print(libraries, type(libraries))
        
        libraries.add("Keras")  # add item
        libraries.update({'NetworkX', 'BeautifulSoup', 'NLTK'})  # add Set
        print(libraries)

![exec](images/python_script_exec_6.png)  

> liste méthodes pour Set : 
[voir doc.](https://docs.python.org/3/library/stdtypes.html?highlight=set#set)


### Tuple

Un tuple est une collection qui est **ordonnée** et **immuable**. Les valeurs en double sont **autorisées**.

Exemple :

        [python]
        libraries = ('Pandas', 'Numpy', 'Scikit Learn', 'Matpolib', 'Seaborn')
        # libraries = tuple(('Pandas', 'Numpy', 'Scikit Learn', 'Matpolib', 'Seaborn'))
        print(libraries)
        print(libraries[0], libraries[-1], libraries[:4])
        
        try:
          libraries.append("Keras")  # Cette instruction va générer une Exception!
        except:
          print("Exception : ajout d\'items dans un tuple non autorisé!")
        
        #  unpacking : tuple =>  variables
        (lib1, lib2, lib3, lib4, lib5) = libraries
        print(lib1, '|', lib2, '|', lib3, '|', lib4, '|', lib5)
        
        (lib1, lib2, *others) = libraries
        print(lib1, '|', lib2, '|', others)

![exec](images/python_script_exec_7.png)  


## Conditions & Boucles

### Conditions (If Else)

Syntaxe de l'instruction **if** [**else**] :

if condition :  
    instruction(s)
[else:
    instruction(s)
]

        [python] 
        num = int(input( "Entrez un nombre :" ))  
        if num%2 == 0:  
           print ("Le nombre est pair!")  
        else:  
           print("Le nombre est impair!")  

Syntaxe de l'instruction **elif** :

if condition 1:   
    instruction(s)  
elif condition 2:   
    instruction(s)    
elif condition 3:   
    instruction(s)   
else:   
    instruction(s)   
    
        [python] 
        age = int(input("Entrez un age : "))
        if 0 < age <= 14:
            print('Enfant')
        elif 14 < age <= 24:
            print('Adolescent')
        elif 24 < age <= 64:
            print('Adulte')
        elif 64 < age:
            print('Ainé')
        else:
            print('Non Reconnu!')



### Boucles (While For)

Syntaxe de la boucle **for** :

for var_iteration in sequence:    
   instructions(s)   


        [python]
        libraries = ('Pandas', 'Numpy', 'Scikit Learn', 'Matpolib', 'Seaborn')
        for lib in libraries:
            print(lib) 

        for i in range(1, 11):  # 1..10
            print('7*' + str(i) + ' = ' + str(7 * i))

        # for + else :    
        for i in range(len(libraries)):
            print(libraries[i])
        else:
            print('for loop finished!') # si TOUTES itérations exécutées

Syntaxe boucle **while** :

while condition:    
    instruction(s)  
[else:
    instruction(s)
]

        [python]
        i = 0
        while i < len(libraries):
            print(libraries[i])
            if libraries[i]=='Numpy':
                break
            i += 1        
        else:
            print('while loop finished!')


        i = 0
        while i < len(libraries):
            if i == 3:
                i += 1
                continue
            print(libraries[i])
            i += 1


## Ecosystème Python

Tools & Environnements :

### PyPI [home](https://pypi.org)

Find, install and publish Python packages with the Python Package Index

> Positive
> : PyPI (de l'anglais « Python Package Index ») est le dépôt tiers officiel du langage Python. Son objectif est de doter la communauté des développeurs Python d'un catalogue complet recensant tous les paquets Python libres.
La plupart des gestionnaires de paquets Python utilisent ce dépôt, le plus connu est pip.

### Anaconda Distribution [home](https://www.anaconda.com/distribution/)

![Logo](https://www.anaconda.com/wp-content/uploads/2018/06/cropped-Anaconda_horizontal_RGB-1-600x102.png)

> Positive
> : The open-source Anaconda Distribution is the easiest way to perform Python/R data science and machine learning on Linux, Windows, and Mac OS X.

### Spyder  [home](https://www.spyder-ide.org)

> Positive
> : Spyder is a powerful scientific environment written in Python, for Python, and designed by and for scientists, engineers and data analysts. It offers a unique combination of the advanced editing, analysis, debugging, and profiling functionality of a comprehensive development tool with the data exploration, interactive execution, deep inspection, and beautiful visualization capabilities of a scientific package.


### Colaboratory [home](https://colab.research.google.com)

![Logo](https://colab.research.google.com/img/colab_favicon.ico)

> Positive
> :  Colaboratory est un environnement de notebook Jupyter qui ne nécessite aucune configuration et qui s'exécute entièrement dans le cloud.  Il vous permet d'écrire et d'exécuter du code, de sauvegarder et partager vos analyses, et d'accéder à de puissantes ressources informatiques. Tout cela --gratuitement--, depuis votre navigateur.

### PyDrive [home](https://pypi.org/project/PyDrive/)

> Positive
> : PyDrive is a wrapper library of google-api-python-client that simplifies many common Google Drive API tasks.

### Librairies

Python possède des librairies pour à peu près tout..

  * numpy et scipy pour les calculs
  * Matplotlib et Seaborn pour la visualisation
  * Scikit-learn pour les algorithmes
  * Pandas pour les gérer les données (les charger, appliquer des opérations d'algèbre relationnelle, etc.)
  * Tensorflow et PyTorch pour le deep learning
  * etc.

## Python & GTK based GUI application

To run a very simple GTK based GUI application using the **PyGObject** provided Python binding :

Go to [http://www.msys2.org/](http://www.msys2.org/) and download the x86_64 installer
Run C:\msys64\mingw64.exe
Execute 

      [python]
      pacman -Suy  

Execute
       [python]
       pacman -S mingw-w64-x86_64-gtk3 mingw-w64-x86_64-python3 mingw-w64-x86_64-python3-gobject

To test that GTK 3 is working you can run **gtk3-demo**
Copy the hello.py script you created to C:\msys64\home\<username>
In the mingw32 terminal execute python3 hello.py - a window should appear.

hello.py :

        [python]
        import gi
        gi.require_version("Gtk", "3.0")
        from gi.repository import Gtk

        window = Gtk.Window(title="Hello World")
        window.show()
        window.connect("destroy", Gtk.main_quit)
        Gtk.main()

[Python GTK+ 3 Tutorial](https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html)

## Python & Machine-Learning
Duration: 0:10

Liste & Liens:

* [makina corpus](https://makina-corpus.com/blog/metier/2017/initiation-au-machine-learning-avec-python-theorie)
* [ensae_teaching](https://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_3a.html#elements-techniques)
* [oreilly/ai](https://www.oreilly.com/topics/ai)



> [projet blog sur github](https://github.com/mcteach21/Django-Start)
