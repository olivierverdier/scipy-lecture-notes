Une (très brève) introduction à Python
=======================================

.. warning:: 
    Cette partie ne sera pas abordée lors du cours Python
    scientifique du PAT Dakar, un cours plus long d'introduction au
    langage étant déjà prévu. Si vous connaissez déjà le langage Python
    mais que vous voulez connaître ses applications scientifiques, passez
    directement à la partie suivante.

.. topic:: Le langage Python pour l'informatique scientifique

    Dans ce chapitre, on va apprendre le strict minimum nécessaire pour
    pouvoir utiliser les outils de calcul scientifique fournis par Python
    et ses librairies. En effet, ce cours a été initialement conçu pour
    suivre un autre cours consacré entièrement à une introduction au
    langage, et ce chapitre a été ajouté dans le but que le cours puisse
    être lu indépendamment d'autres sources. 

    On va donc seulement effleurer les spécificités du langage et les
    possibilités qu'il offre. Pour ceux qui voudraient en savoir plus, le
    tutoriel http://docs.python.org/tutorial/ (en anglais) est un bon
    point de départ.

Python c'est quoi ?
----------------------

.. image:: python-logo.png
   :align: right

Python est un **langage de programmation**, comme C, Fortran, BASIC, PHP,
etc... Voici quelques caractéristiques du langage :

* un langage **interprété** et non compilé. Contrairement au C ou au Fortran
  par exemple, l'utilisateur ne doit pas compiler son code Python avant
  de l'éxécuter. Python est par ailleurs un langage qui permet l'
  **utilisation interactive** : il existe plusieurs **interpréteurs** de Python 
  qui permettent d'éxécuter du code Python en mode interactif.

* un langage distribué sous une licence **open-source** : on peut l'utiliser
  gratuitement, même pour construire des logiciels commerciaux payants.

* multi-plateforme : Python tourne sous Windows, Linux/Unix, Mac OS X,
  OS/2, les Palm et les téléphones Nokia, les machines virtuelles Java et
  .NET, donc dans beaucoup d'environnements.

* un langage avec de nombreuses **librairies** devenues des standards
  dans de nombreux domaines, de la construction d'applications web au
  calcul scientifique (l'objet de ce cours !).

* Enfin, quelques caractéristiques techniques que nous allons illustrer
  par la suite : Python est un langage **orienté-objet**, au **typage
  dynamique** (le type d'un objet peut changer au cours d'un programme).

Premiers pas
---------------

Ouvrons l'interpréteur **Ipython** (un très bon interpéteur de Python) en

* tapant "ipython" dans une console Linux ou dans le shell cmd de
  Windows.
* **ou** en le lançant à partir d'un menu (Ipython est installé avec l'EPD ou
  Python(x,y) sous Windows, on peut le trouver dans les sous-menus
  correspondant).

Si vous n'avez pas Ipython sur votre ordinateur (songez à l'installer !),
vous pouvez lancer un autre interpréteur : Idle par exemple est également
un bon interpréteur. Sinon, on peut toujours lancer l'interpréteur "de
base" en tapant simplement "python" dans une console (Linux/Mac/Windows),
mais l'interpréteur ainsi ouvert est assez rustique par rapport aux
autres.

Une fois l'interpréteur ouvert, tapez ::

    >>> print "Hello, world!"
    Hello, world!

Le message "Hello, world!" s'affiche alors : vous avez exécuté votre
première instruction Python. 

Tapez ensuite la série d'instructions suivante ::

    >>> a = 3
    >>> b = 2*a
    >>> type(b)
    <type 'int'>
    >>> print b
    6
    >>> a*b 
    18
    >>> b = 'hello' 
    >>> type(b)
    <type 'str'>
    >>> b + b
    'hellohello'
    >>> 2*b
    'hellohello'

On a défini plus haut deux ojets ``a`` et ``b``. Il n'est pas nécessaire
de déclarer le type d'un objet avant d'assigner la valeur de cet objet,
contraitement par exemple au langage C où on devrait écrire

.. sourcecode:: c

    int a;
    a = 3;

Par ailleurs le type d'un objet peut changer : notre objet ``b`` était
un entier, il est devenu une chaîne de caractères quand nous nous l'avons
assigné à ``hello``. Notons qu'on peut faire de manière native des
opérations sur les entiers (``b=2*a``). De même pour les chaînes de
caractères : l'addition + correspond à la concaténation des chaînes.

.. topic:: Quelques petits trucs Ipython

    * Un certain nombre de commandes shell classiques marchent : ls, pwd,
      cd, etc.

    * Pour avoir de l'aide sur un objet, une fonction, etc., taper ``help
      objet``. Taper help() pour commencer.

    * Utiliser la tab-completion : quand on tape le début d'un objet et
      qu'on appuie sur tab, Ipython va chercher à compléter avec les
      objets qu'il connaît. S'il y a plusieurs objets possibles pour
      compléter, Ipython affiche une liste de ces objets.

    * Historique : se servir de la flèche vers le haut pour chercher dans
      l'historique les lignes qui commencent comme ce qu'on a déjà tapé.

    * Si vous voulez logguer votre session (pour pouvoir retrouver toutes
      les commandes ques vous avez tapé), utilisez la "commande magique"
      %logstart.

.. sourcecode:: ipython

    In [1]: %logstart commandes.log
    Activating auto-logging. Current session state plus future input saved.
    Filename       : commandes.log
    Mode           : backup
    Output logging : False
    Raw input log  : False
    Timestamping   : False
    State          : active
 

Les différents types d'objets
-------------------------------

**Nombres**

On a créé plus haut des entiers (``int``). Il existe aussi des flottants ::

    >>> c = 2.1

et des booléens::

    >>> c > a
    False
    >>> test = (c > a)
    >>> test
    False
    >>> type(test)
    <type 'bool'>

Les nombres complexes correspondent aussi à un type natif de Python ::

    >>> a=1.5+0.5j
    >>> a.real
    1.5
    >>> a.imag
    0.5

On peut se servir de l'interpréteur comme d'une calculatrice, en se
servant de opération +, -, \*, /, ou encore % (modulo)::

    >>> 7 * 3.
    21.0
    >>> a = 8
    >>> b = 3
    >>> a/b # attention : la division d'entiers est la division euclidienne
    2
    >>> float(a)/b # on peut transformer un entier en flottant avec float()
    2.6666666666666665
    >>> a%3
    2

**Chaînes de caractères** 

Les chaînes de caractères sont contenues dans des guillements simples ou
doubles ::

    >>> "bonjour"
    'bonjour'
    >>> 'bonjour'
    'bonjour'
    >>> "c'est bien"
    "c'est bien"

.. sourcecode:: ipython

    In [45]: 'c'est bien'
    ------------------------------------------------------------
	File "<ipython console>", line 1
	'c'est bien'
             ^
    SyntaxError: invalid syntax

Comme vu plus haut, on concatène différentes strings avec + et on les
répète avec * ::

    >>> "bonjour " + "comment" + " va ?" 
    'bonjour comment va ?'
    >>> 2*"bonjour "
    'bonjour bonjour '

Le caractère pour une nouvelle ligne est ``\n``, pour une tabulation
``\t``.

On accède au n-ième caractère d'une string ``s`` par ``s[n]``::

    >>> a = "hello"
    >>> a[0]
    'h'
    >>> a[1]
    'e'
    >>> a[-1]
    'o'

Attention : **l'indexation commence à 0 et non à 1** ! Des indices négatifs
correspondent à compter à partir de la fin de la chaîne.

Pour accéder à des bouts de la chaîne plutôt qu'à un seul caractère à la
fois, on utilise le **slicing** (on découpe des "tranches" de la chaîne)
::

    >>> a = "hello, world!"
    >>> a[3:6] # les elements du 3e au 6e (non inclus !) : elements 3, 4, 5
    'lo,'
    >>> # la slice a[debut:fin] a (fin - debut) elements
    >>> a[2:10:2] # Syntaxe : a[debut:fin:pas]
    'lo o'
    >>> a[::3] # un caractere sur trois, du debut a la fin (si on ne precise pas)
    'hl r!'
    >>> a[:10] # les 10 premiers caractères
    'hello, wor'
    >>> a[::-1] # on parcourt à l'envers
    '!dlrow ,olleh'

On peut aussi créer des strings en Unicode afin de gérer les accents ou
autres caractères spéciaux (voir
http://docs.python.org/tutorial/introduction.html#unicode-strings).

Une string n'est pas mutable, on ne peut pas modifer ses caractères. Par
contre on peut créer des nouvelles strings à partir de strings
existantes.

.. sourcecode:: ipython

    In [53]: a = "hello, world!"
    In [54]: a[2] = 'z'
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call
    last)

    /home/gouillar/travail/sgr/2009/talks/dakar_python/cours/gael/essai/source/<ipython
    console> in <module>()

    TypeError: 'str' object does not support item assignment
    In [55]: a.replace('l', 'z', 1)
    Out[55]: 'hezlo, world!'
    In [56]: a.replace('l', 'z')
    Out[56]: 'hezzo, worzd!'

.. warning:: 

    le langage Python offre de nombreuses possibilités pour transforme les
    strings, chercher des motifs dans une string ou encore les formatter.
    Par manque de temps, on ne les abordera pas dans ce cours mais le
    lecteur intéressé peut aller regarder
    http://docs.python.org/library/stdtypes.html#string-methods et
    http://docs.python.org/library/string.html#new-string-formatting

**Listes**

Une liste est une collection ordonnée d'objets qui peuvent être de type
différents. Par exemple ::

    >>> l = [3, 2, 'bonjour']
    >>> l
    [3, 2, 'bonjour']

On accède aux éléments d'une liste de la même manière que pour les
strings, et on crée des sous-listes grâce au slicing ::

    >>> l[0]
    3
    >>> l[-1]
    'bonjour'
    >>> l[1:]
    [2, 'bonjour']
    >>> l[::2]
    [3, 'bonjour']

Une liste est mutable, on peut changer ses éléments (contrairement à une
string) ::

    >>> l[0] = 1
    >>> l
    [1, 2, 'bonjour']

Comme pour les strings, Python fournit un grand nombre de fonctions pour
modifier des listes ou faire des recherches dans ces listes. En voici
juste quelques exemples, pour plus de détails voir
http://docs.python.org/tutorial/datastructures.html#more-on-lists ::

    >>> a = [66.25, 333, 333, 1, 1234.5]
    >>> print a.count(333), a.count(66.25), a.count('x')
    2 1 0
    >>> a.insert(2, -1)
    >>> a.append(333)
    >>> a
    [66.25, 333, -1, 333, 1, 1234.5, 333]
    >>> a.index(333)
    1
    >>> a.remove(333)
    >>> a
    [66.25, -1, 333, 1, 1234.5, 333]
    >>> a.reverse()
    >>> a
    [333, 1234.5, 1, 333, -1, 66.25]
    >>> a.sort()
    >>> a
    [-1, 1, 66.25, 333, 333, 1234.5]

La notation ``a.fonction()`` est un exemple de *programmation
orientée-objet* (OOP en anglais) : en tant que ``list``, l'objet a
"possède" la *méthode* fonction qu'on appelle avec la notation **.**.
Comprendre le sens de notation **.** est à peu près le seul élément de
programmation orientée objet dont on a besoin pour ce cours. Cependant,
pour une utilisation plus avancée, un petit complément a été ajouté plus
loin.  

**Tuples**

En gros, les tuples sont des listes immutables. Pour la syntaxe, les
éléments d'un tuple sont définis entre parenthèses ou juste séparés par
des virgules ::

    >>> t = 12345, 54321, 'hello!'
    >>> t[0]
    12345
    >>> t
    (12345, 54321, 'hello!')
    >>> u = (0, 2)

**Dictionnaires**

Un dictionnaire est une sorte de mini base de données, ou encore un
*tableau associatif* non ordonné, qui associe des valeurs à des clés. Un
exemple ::

    >>> tel = {'emmanuelle': 5752, 'sebastien': 5578}
    >>> tel['francois'] = 5915 
    >>> tel
    {'sebastien': 5578, 'francois': 5915, 'emmanuelle': 5752}
    >>> tel['sebastien']
    5578
    >>> tel.keys()
    ['sebastien', 'francois', 'emmanuelle']
    >>> 'francois' in tel
    True

Cette structure de données peut être très pratique pour stocker des
couples de variables et faire une recherche sur une de ces deux variables
(e.g. la date, le nom, etc.). Pour plus d'infos
http://docs.python.org/tutorial/datastructures.html#dictionaries

Contrôle de flot
--------------------

**Définition d'une fonction**

Nous allons maintenant définir une fonction qui calcule les ``n``
premiers termes de la suite de Fibonacci. Taper les lignes suivantes dans
votre interpréteur, **en faisant attention à respecter l'indentation**
(l'interpréteur devrait indenter pour vous, pour revenir d'un niveau
d'indentation en moins revenir en arrière avec backspace de 4 espaces --
i.e. jusqu'à être aligné avec le niveau logique correspondant). Pour
sortir de la définition de la fonction on tape deux fois sur Enter. ::

    >>> def fib(n):    
    ...     """Affiche les n premiers termes de la suite de Fibonacci"""
    ...     a, b = 0, 1
    ...     i = 0
    ...     while i < n:
    ...         print b, # la virgule empeche d'aller a la ligne
    ...         a, b = b, a+b
    ...         i +=1
    ...
    >>> fib(10)
    1 1 2 3 5 8 13 21 34 55

Un autre exemple ::

    >>> def message(nom, sentiment='content'):
    ...     message = "Bonjour, je m'appelle " + nom + ", et je suis " + sentiment
    ...     return message # return permet de renvoyer un objet
    ... 
    >>> m = message('Pedro')
    >>> m
    "Bonjour, je m'appelle Pedro, et je suis content"
    >>> type(m)
    <type 'str'>
    >>> message('Isabelle', sentiment='heureuse')
    "Bonjour, je m'appelle Isabelle, et je suis heureuse"
    >>> message('Isabelle', 'heureuse')
    "Bonjour, je m'appelle Isabelle, et je suis heureuse"

Notons la syntaxe pour définir une fonction :

    * le keyword ``def`` ;
    
    * suivi du nom de la fonction, puis

    * des arguments de la fonction entre parenthèses. Python offre la
      possibilité de donner des **arguments optionnels**, dont on fixe la
      valeur par défaut. C'est très pratique pour écrire des fonctions
      modulaires qui peuvent servir dans différents cas.

    * du corps de la fonction ;

    * et enfin, si la fonction retourne un objet, on le fait avec la
      syntaxe ``return objet``.

.. warning:: 

    Python est un langage où l'indentation est interprétée et est donc
    indispensable. Tout bloc de commandes commençant après un **:** doit
    être indenté d'un niveau par rapport à la ligne contenant ce **:**.
    Après un ``def f():`` ou un ``while:`` il faut donc indenter. Quand
    le bloc logique est fini on recule à nouveau d'un niveau
    d'indentation, quitte à réindenter si on reforme un bloc logique
    nécessitant de l'identation, etc. 

    Grâce à l'indentation on évite les ``{`` ou ``;`` qui sont
    obligatoires pour marquer les blocs logiques dans d'autres langages.
    En contrepartie, il faut faire attention à bien indenter quand il le
    faut, sinon Python va produire une erreur de la forme

    .. sourcecode:: ipython

	------------------------------------------------------------
	IndentationError: unexpected indent (test.py, line 2)

    En particulier, il ne faut aller à la ligne que quand la ligne est
    vraiment finie. Si on veut séparer en deux une ligne vraiment très
    longue, il faut utiliser la syntaxe suivante avec un ``\`` ::
    
	>>> longue_ligne = "Voici une très longue ligne \
	... que nous coupons en deux"

    Tout ceci est un peu déroutant au début, mais ça devient vite très
    agréable de ne pas avoir à écrire de signes cabalistiques à chaque
    début/fin de ligne ou de bloc logique ! L'indentation contribue donc
    doublement à la bonne lisibilité du code Python : en facilitant une
    lecture hiérarchique des niveaux logiques, et en supprimant les
    signes non significatifs pour le code.

Comme dans beaucoup de langages, on peut écrire des boucles ``for``,
``while``, ou gérer des conditions avec ``if``, ``else`` ::

    >>> # range(debut, fin, pas) retourne une liste d'entiers
    >>> l = range(0, 10) 
    >>> l     
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> for nombre in l: # une boucle for
    ...     if (nombre%2==0): # une condition if
    ...         print nombre 
    ...     else: # meme niveau d'indentation que if (utiliser backspace)
    ...         print "nombre non pair !"
    ...         
    0
    nombre non pair !
    2
    nombre non pair !
    4
    nombre non pair !
    6
    nombre non pair !
    8
    nombre non pair !

On peut boucler sur autre chose que des indices entiers : Python peut par
exemple itérer sur les éléments d'une liste, les caractères d'une chaîne
de caractères, etc. ::

    >>> message = "hello"
    >>> for c in message:
    ...     print c
    ...     
    h
    e
    l
    l
    o
    >>> message = "Hello how are you?"
    >>> message.split()
    ['Hello', 'how', 'are', 'you?']
    >>> for word in message.split():
    ...     print word
    ...     
    Hello
    how
    are
    you?
    >>> l = [[1, 2, 3], 'coucou', [5, 6]]
    >>> for element in l:
    ...     print element
    ...     
    [1, 2, 3]
    coucou
    [5, 6]

Peu de langages offrent cette possibilité de boucler sur autre chose que
des nombres, qui est fort pratique car on boucle exactement sur l'objet
qu'on considère et non sur un indice sur lequel on finit forcément par se
tromper.

Les scripts et les modules
----------------------------

Pour le moment nous avons tapé toutes nos instructions dans
l'interpréteur. Bien sûr, il faut changer de méthode pour écrire des
programmes plus longs ! On va alors écrire notre code dans des fichiers à
l'aide d'un éditeur de texte (votre éditeur préféré, ou celui fourni par
votre distribution de Python si vous utilisez Python à l'intérieur d'une
suite de calcul scientifique comme EPD ou Python(x,y)). 

Commençons par écrire un **script**, c'est-à-dire un fichier contenant
une simple série d'instructions, qu'on peut par exemple copier-coller à
partir de l'interpréteur (mais en respectant l'indentation !!).
L'extension d'un fichier avec du code python est **.py**. Copier-coller
dans un fichier **test.py** les lignes suivantes ::

    message = "Hello how are you?"
    for word in message.split():
        print word

Pour exécuter ce petit script, on peut :

    * l'exécuter dans une console (console linux/Mac ou console cmd
      Windows). Par exemple, si on est dans le même répertoire que le
      fichier test.py, on peut exécuter dans une console

.. sourcecode:: bash 

    epsilon:~/sandbox$ python test.py
    Hello
    how
    are
    you?

Cependant, il ne s'agit pas d'une utilisation interactive, et dans
le cadre du calcul scientifique, on travaille (le plus) souvent en mode
interactif, c'est-à-dire à l'intérieur d'un interpréteur :

    * dans Ipython, la syntaxe pour exécuter un script est ``%run
      script.py`` (ne pas oublier le ``%`` devant ``run`` !). Par
      exemple, 

.. sourcecode:: ipython

    In [1]: %run test.py
    Hello
    how
    are
    you?

    In [2]: message
    Out[2]: 'Hello how are you?'

    
Le script s'est exécuté, qui plus est les variables définies dans le
script sont maintenant accessibles (comme ``message``).

Si on veut écrire des programmes un peu plus longs et plus organisés, où
on définit des objets (variables, fonctions, classes) que l'on
souhaiterait pouvoir réutiliser plusieurs fois, on définit un **module**.
Voici un exemple de module contenu dans le fichier suites.py (recopier le
contenu dans un fichier appelé suites.py) ::

    def fib(n):
        "return nth term of Fibonacci sequence"
        a, b = 0, 1
        i = 0
        while i<n:
            a, b = b, a+b
            i += 1
        return b
    
    def linear_recurrence(n, (a,b)=(2,0), (u0, u1)=(1,1)):
        """return nth term of the sequence defined by the
        linear recurrence
            u(n+2) = a*u(n+1) + b*u(n)"""
        i = 0
        u, v = u0, u1
        while i<n:
            w = a*v + b*u
            u, v = v, w
            i +=1
        return w
 
Dans ce fichier, on a défini deux types de suite. Supposons maintenant
qu'on veuille appeler la fonction ``fib`` à partir de l'interpréteur. On
pourrait exécuter le module comme un script, mais puiqu'il n'y a pas
d'instructions à exécuter à l'intérieur, nous allons plutôt l'**importer
en tant que module**. La syntaxe est la suivante :: 

    >>> import suites
    >>> suites.linear_recurrence(10)
    1024
    >>> for i in range(5):
    ...     print i, suites.fib(i)
    ...     
    0 1
    1 1
    2 2
    3 3
    4 5

Le code du fichier est exécuté lors de l'import du module. 
On peut ensuite se servir des objets qu'il définit grâce à la syntaxe
``module.objet``. Il ne faut pas oublier de rajouter le nom du module
devant le nom de l'objet, sinon Python ne reconnaît pas l'instruction. 

Si on veut éviter de taper à chaque fois ``module.objet``, on peut
importer certains ou tous les objets du module dans l'"espace de noms"
principal (main namespace en anglais). Par exemple ::

    >>>from suites import fib
    >>> fib(10)
    89
    >>> # ou
    >>> from suites import *
    >>> linear_recurrence(5)
    32


.. sourcecode:: ipython

    In [29]: who
    fib linear_recurrence	

    In [30]: whos
    Variable            Type        Data/Info
    -----------------------------------------
    fib                 function    <function fib at 0x96eb8ec>
    linear_recurrence   function    <function linear_recurrence at 0x96eb9cc>


Quand on utilise ``from module import *``, il faut faire attention à ne
pas écraser un objet déjà existant (par exemple, si on avait déjà une
fonction ou une variable appelée ``fib``). Il faut donc éviter cet usage
pour les modules avec beaucoup d'objets, ou quand on a des noms d'objets
courants (max, mean, etc.). 




Pour raccourcir les noms qu'on tape, on peut importer un module sous un
nom plus court. Par exemple, c'est une convention très classique
d'importer le module ``numpy`` (tableaux de données, que nous allons étudier
par le suite) sous le nom ``np`` ::

    >>> import numpy as np
    >>> type(np)
    <type 'module'>

On peut définir des
sous-modules à l'intérieur d'un module ::

    >>> import scipy # routines de calcul scientifique
    >>> import scipy.optimize # sous-module d'optimisation
    >>> type(scipy.optimize)
    <type 'module'>
    >>> import scipy.optimize as opti # plus court !


Les modules sont donc un moyen d'organiser un code de façon hiérarchique. En fait, tous les
packages
d'informatique scientifique que nous allons utiliser avec Python seront 
des modules ::

    >>> import numpy as np # tableaux de donnees
    >>> np.linspace(0, 10, 6)
    array([  0.,   2.,   4.,   6.,   8.,  10.])
    >>> import scipy # calcul scientifique
    >>> from pylab import * # plot de donnees 
    >>> # appeler Ipython avec le switch -pylab est equivalent
    >>> # à la ligne precedente (ipython -pylab)

Et comme on l'a déjà vu, quand on écrit un fichier de code organisé (ex :
``suites.py``,  on crée un module.

Dans le logiciel Python(x,y), Ipython(x,y) exécute au démarrage les
imports suivants::

    >>> import numpy	
    >>> import numpy as np
    >>> from pylab import *
    >>> import scipy

et il n'est donc pas nécessaire de refaire ces imports.



Input et Output
----------------

Par souci d'exhaustivité, voici quelques informations sur l'input et
l'output dans Python. Néanmoins, nous nous servirons des méthodes de
Numpy pour lire et écrire dans des fichiers, on peut donc sauter ce
paragraphe en première lecture.

On écrit et on lit des **strings** dans les fichiers (il faut convertir
les autres types en strings). Pour écrire dans un fichier 
::

    >>> f = open('workfile', 'w') # ouvre le fichier workfile
    >>> type(f)
    <type 'file'>
    >>> f.write('Ceci est un test \nEncore un test')
    >>> f.close()

Pour lire dans un fichier ::

    >>> f = open('workfile', 'r')
    >>> s = f.read()
    >>> print s
    Ceci est un test 
    Encore un test
    >>> f.close()

Pour plus de détails : http://docs.python.org/tutorial/inputoutput.html

Erreurs et exceptions
------------------------

Si vous avez essayé d'exécuter tous les exemples précédents, il serait
bien étonnant que vous n'ayez pas rencontré une erreur à un moment... :-? 

Vous avez alors peut-être remarqué qu'il y a plusieurs types d'erreurs :
``SyntaxError, ImportError, ValueError``, accompagnée chacune d'un
message d'erreur. Le nom de l'erreur comme le message d'erreur
renseignent sur l'origine de l'erreur et aident donc au débuggage.
Chaque utilisateur peut également prévoir des cas où son code va
retourner une erreur (par exemple si un paramètre d'entrée n'a pas le
type attendu). 

Pour bien profiter de la richesse de Python, il faut donc se servir des
erreurs, par exemple pour prévoir des cas où les utilisateurs font appel
à une fonction pour une utilisation non prévue. Nous laissons
le lecteur se référer à http://docs.python.org/tutorial/errors.html pour
plus de détails sur la gestion des erreurs et des exceptions.

Programmation orientée objet
----------------------------- 

La programmation orientée objet a pour but de 

    * hiérarchiser/organiser du code

    * favoriser la réutilisation de code pour ne pas recopier le même
      bout de code à différents endroits dans des contextes proches mais
      différents.

En voici un petit exemple : on va créer une **classe** Etudiant,
c'est-à-dire un objet regroupant un certain nombre de fonction (des
**méthodes**) et de variables (des **attributs**) qui lui sont propre, et
qu'on pourra appeler ::

    >>> class Etudiant(object):
    ...     def __init__(self, name):
    ...         self.name = name
    ...     def set_age(self, age):
    ...         self.age = age
    ...     def set_major(self, major):
    ...         self.major = major
    ...         
    >>> anne = Etudiant('anne')
    >>> anne.set_age(21)
    >>> anne.set_major('physique')

Dans l'exemple précédent, la classe Etudiant a comme méthode ``__init__,
set_age`` et ``set_major``. Ses attributs sont ``name, age`` et
``major``. On appelle les méthodes et les attributs avec la notation
``instancedelaclasse.methode`` ou  ``instancedelaclasse.attribut``. Le
constructeur ``__init__`` est une méthode à part, qu'on appelle sous la
forme ``instancedelaclasse(paramètres de __init__ s'il y en a)``.

Supposons maintenant qu'on veuille créer une nouvelle classe
EtudiantMaster avec les
mêmes méthodes et attributs que la précédente, mais avec un attribut
``stage`` supplémentaire. On ne va pas réécrire toute la classe
précédente, mais **hériter** de la classe Etudiant :: 

    >>> class EtudiantMaster(Etudiant):
    ...     stage = 'obligatoire, de mars a juin'
    ...     
    >>> benoit = EtudiantMaster('benoit')
    >>> benoit.stage
    'obligatoire, de mars a juin'
    >>> benoit.set_age(23)
    >>> benoit.age
    23

La classe EtudiantMaster a **hérité** des méthodes et attributs de la
classe Etudiant. 

Grâce aux classes et à la programmation orientée objet, on peut donc
organiser son code avec différentes classes correspondant à différents
objets qu'on rencontre (une classe Manip, une class Image, une classe
Ecoulement, etc.), avec leurs méthodes et leurs attributs. On peut alors
se servir de l'héritage pour considérer des variations autour d'une
classe de base, et **mutualiser** ainsi du code. Ex : d'une classe de
base Turbulent, on peut faire hériter une sous-classe EcoulementStokes,
EcoulementNewtonien, EcoulementPotentiel, etc.

Quelques exercices pour terminer cette introduction
----------------------------------------------------

1. Chaînes de caractères

    * Créez une string ``nom`` de la forme "Votreprénom votrenom".

    * Affichez les 5 premiers caractères de cette chaînes, puis un
      caractère sur deux, puis la chaîne parcourue à l'envers.
    
    * Concaténez trois fois la chaînes ``nom`` dans une nouvelle chaîne.


