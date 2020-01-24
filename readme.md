# Learn programming by Python

## WSL
Windows Subsystem for Linux([WSL](https://docs.microsoft.com/en-us/windows/wsl/about)) is an environment in Windows 10 for running unmodified Linux binaries.

### How to enable
```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
> [!IMPORTANT]
> This command require administrative priviledge

### How install Ubuntu 
Download one of these and install it:
- [Ubuntu 16.04 LTS](https://www.microsoft.com/en-us/p/ubuntu-1604/9pjn388hp8c9)
- [Ubuntu 18.04 LTS](https://www.microsoft.com/en-us/p/ubuntu-1804/9n9tngvndl3q)
- [Ubuntu](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6)

## How install python

### From store
```bash
sudo apt install python3.7
```

### From Source
```bash
sudo -i
apt update -y
apt install -y \
    wget \
    build-essential \
    libffi-dev \
    libgdbm-dev \
    libc6-dev \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev

cd /usr/src
PYTHON_VERSION=3.8.1
wget http://python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tar.xz
tar xf Python-$PYTHON_VERSION.tar.xz
cd Python-$PYTHON_VERSION
./configure --enable-optimizations
make altinstall
exit
```
> [!IMPORTANT]
> make altinstall causes it to not replace the built in python executable.

### Upgrade pip
```bash
pip3.8 install --upgrade pip
```

## Select Text Editor or IDE
Having a well configured text editor can make the programming experience much more enjoyable. Much like a carpenter, having sharp tools leads to a more productive creative experience.

### Terminal based editors
- [Vim](https://www.vim.org/)
- [Emacs](https://www.gnu.org/software/emacs/)
- [Nano](https://www.nano-editor.org/)

### GUI Based Editors
- [Atom](https://atom.io/)
- [VS Code](https://code.visualstudio.com/)

    Suggested extensions(VS Code offer extensions as you keep using it):
    - [Remote - WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)

        > [!IMPORTANT]
        > This extension is required in order to work with `WSL`
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    - [GitLens — Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
    - [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)
- [SublimeText](https://www.sublimetext.com/)
- [Notepad++](https://notepad-plus-plus.org/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

## REPL

### What is REPL?
REPL stands for: **R**ead, **E**valuate, **P**rint, **L**oop

Each line is read and evaluated. The return value is then printed to the screen, and then the process repeats.

Python ships with a REPL, accessible by running python3.8 from a terminal.

### Using REPL
The `>>>` indicates a line to type in, like a command prompt for Python. Later on we'll see a ..., which means that we are currently sitting in a scoped area. The only way out is to enter a blank line (no spaces) before the interpreter will evaluate the entire code block.

The simplest use of this would be to do some math:
```python
>>> 1 + 1
2
>>>
```

2 is the return value of the expression and it is then printed to the screen. If something doesn't have a return value, then nothing will be printed to the screen and we'll just land back at a `>>>` prompt. We'll cover this later, but an example would be `None`:
```python
>>> None
>>>
```

To exit the REPL, we can either type `exit()` (the parentheses are important) or hit `Ctrl+d` on your keyboard.

## Git

### What is Git?
Git is a Distributed Version Control Systems(DVCS) to records changes to a file or set of files over time so that you can recall specific versions later.

### Usefull commands
[git clone](https://git-scm.com/docs/git-clone): Clone a git repository to local file system.

[git pull](https://git-scm.com/docs/git-pull): Get changes from the server and merge them with your local copy.

[git status](https://git-scm.com/docs/git-status): Show the working tree status.

[git checkout](https://git-scm.com/docs/git-checkout): Switch branches or restore working tree files.

[git add](https://git-scm.com/docs/git-add): This command updates the index using the current content found in the working tree, to prepare the content staged for the next commit.

[git commit](https://git-scm.com/docs/git-commit): Commit your changes to local git repository.

[git push](https://git-scm.com/docs/git-push): Update remote refs along with associated objects.

## Basics of programming
Writing a program is the art of breaking the problem into small blocks of tasks that work in cooperation with each other to achieve a bigger task and provide a useful service.

### Using comments
Writing a simple program is easy enough, but writing a good program that provide a service for a long time require some skill and to comply with some rule.

Writing a program for an actual useful problem, require many services. And over time many of this services will change. New services will added to the list of required service, some old services will be removed and some of them will be changed.

It is not always the same person that work on a piece of code, so we should write codes in a way that someone else may understand them at a later time. One of the easiest and most efficient ways to express our intention of writing a code is comment, one or two lines of code that describe our intention.

Comments in python start with `#` and continue till the end of the line.
```python
# This is a full line comment
print("Hello user!")    # Great user of the program
```

### Python basic types
#### Strings
Strings are a sequence of characters. In python they will be called [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-strl).
They may be quoted with `'` or `"`. There is no difference in using each one of these but internally python will use `'` to represent strings.
```python
>>> 'single quoted string'
'single quoted string'
>>> "double quoted string"
'double quoted string'
>>> print('"double quote" in single quoted string')
"double quote" in single quoted string
>>> print("'single quote' in double quoted string")
'single quote' in double quoted string
```

In order to write long strings that span multiple lines you may use triple quote, either `'''` or `"""`
```python
>>>'''This is line 1 of the string
... This is line 2
... And line3'''
'This is line of the string\nThis is line 2\nAnd line3'
```

In order to write special characters in middle of an string literal we use an escape character. In python this special character is backslash: `\`. Any time that python see `\\` in middle of an string literal it will lookup next character(s) to identify the single character that you wanted to use.
In order to write `\` in a middle of an string you must use `\\`.
```python
>>> print('single quote(\') in middle of single quoted(\') string')
single quote ' in middle of single quoted(') string
>>> print("double quote(\") in middle of double quoted(\") string") 
double quote " in middle of double quoted(") string
>>> print("New\nLine")
New
Line
>>> print('Tab\tdelimited')
Tab    delimited
>>> print('Backslash\\ In middle of an string literal')
Backslash\ In middle of an string literal
```

There are a bunch of operations that you can do with strings
```python
>>> 'Hello ' + 'World!'
'Hello World!'
>>> 3 * '!'
'!!!'
>>> '!' * 3
'!!!'
>>> 'Hello ' + 'World' + 3 * '!'
'Hello World!!!'
```

String also have many useful methods:
```python
>>> # Methods to change case of the letters
...
>>> 'test'.upper() # TEST
'TEST'
>>> 'TesT'.upper() # TEST
'TEST'
>>> 'Test'.lower() # test
'test'
>>> 'test'.capitalize() # Test
'Test'
>>> # Methods to search for substrings
...
>>> 'test'.find('e')
1
>>> 'test'.find('st')
2
>>> 'test'.find('T')
-1
```
> [!IMPORTANT]
> In python string literals are **immutable** and you can't change them.

#### Numbers
There are to main types of numbers we'll use in Python: [`int` and `float`](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex). For the most part, we won't be calling methods on number types — instead, we will use a variety of operators.
```python
>>> 2 + 2 # Addition
4
>>> 10 - 4 # Subtraction
6
>>> 3 * 9 # Multiplication
27
>>> 5 / 3 # Division
1.66666666666667
>>> 5 // 3 # Floor division, always returns a number without a remainder
1
>>> 8 % 3 # Modulo division, returns the remainder
2
>>> 2 ** 3 # Exponent
8
```

If either of the numbers in a mathematical operation in Python is a `float`, then the other will be converted before carrying out the operation and the result will always be a `float`.
```python
>>> 2 + 3.0
5.0
>>> 2 * 3.0
6.0
```

##### Converting Strings and Numbers
It's not uncommon for us to need to convert from one type to another when writing a script. Python provides built-in functions for doing that with the built-in types. For strings and numbers, we can use the `str`, `int`, and `float` functions to convert from one type to another (within reason).
```python
>>> str(1.1)
'1.1'
>>> int("10")
10
>>> int(5.99999)
5
>>> float("5.6")
5.6
>>> float(5)
5.0
```

You'll run into issues trying to convert strings to other types if they aren't present in the string.
```python
>>> float("1.1 things")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: '1.1 things'
```

#### Boolean and None
Python way of representing truthiness and nothingness is [`bool` and `None`](https://docs.python.org/3/library/stdtypes.html#truth-value-testing).

##### Boolean
`bool` represent **truthiness** and Python has two boolean constants: `True` and `False`.

Notice that these both start with capital letters. Later we will learn about comparisons operations, and those will often return either `True` or `False`.

##### Representing Nothingness with `None`
Most programming languages have a type that represents the lack of a value, and Python is no different. The constant used to represent nothingness in Python is `None`. `None` is a **falsy**, and we'll often use it to represent when a variable has no value yet.

An interesting thing to note about `None` is that if you type `None` into your REPL there will be nothing printed to the screen. That's because `None` actually evaluates into nothing.

#### Working with variables
Almost any script we write will need to have a way for us to hold on to information for use later on. That's where variables come into play.

We can assign a value to a variable by using a single `=` and we don't need to (nor can we) specify the type of the variable.
```python
>>> my_var = "This is a simple string"
```
Now we can print the value of that string by using *my_var* later on:
```python
>>> print(my_var)
This is a simple string
>>> print(my_var + '.')
This is a simple string.
```

Before, we talked about how we can't change a string because it's immutable. This is easier to see now that we have variables.
```python
>>> my_var += " testing"
>>> my_var
'This is a simple string testing'
```

That didn't change the string — it reassigned the variable. The original string of `"This is a simple string"` was unchanged.

An important thing to realize is that the contents of a variable can be changed, and we don't need to maintain the same type.
```python
>>> my_str = 'test'
>>> my_str = 1
>>> print(my_str)
1
```
Ideally, we wouldn't change the contents of a variable called `my_str` to be an `int`, but it is something that Python would let us do.

One last thing to remember is that if we assign a variable with another variable it will be assigned to the result of the variable and not whatever that varible points to later.
```python
>>> my_str = 1
>>> my_int = my_str
>>> my_str = "testing"
>>> print(my_int)
1
>>> print(my_str)
testing
```

#### Lists
In Python, there are a few different [sequence](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) types that we're going to work with, the most common of which being the [list](https://docs.python.org/3/library/stdtypes.html#list) type.
A list is created in Python by using the square brackets ([, and ]) and separating the values by commas. Here's an example list:
```python
>>> my_list = [1, 2, 3, 4, 5]
```
There's really not a limit to how long our list can be (there is, but it's very unlikely that we'll hit it while scripting)

##### Reading from Lists
To access an individual element of a `list` you can use the index and Python uses a zero based index system.
```python
>>> my_list[0]
1
>>> my_list[2]
3
```
If we try to access an index that is too high (or too low) then we'll receive an error:
```python
>>> my_list[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```
To make sure that we're not trying to get an index that is out of range, we can test the length using the `len` function (and then subtract 1)
```python
>>> len(my_list)
5
```
Additionally, we can access subsections of a list by **"slicing"** it. We provide the starting index and the ending index (the object at that index won't be included).
```python
>>> my_list[0:2]
[1, 2]
>>> my_list[1:]
[2, 3, 4, 5]
>>> my_list[:3]
[1, 2, 3]
>>> my_list[0::1]
[1, 2, 3, 4, 5]
>>> my_list[0::2]
[1, 3, 5]
```

##### Modifying a List
Unlike strings which can't be modified (you can't change a character in a string), you can change a value in a `list` using the subscript equals operation:
```python
>>> my_list[0] = "a"
>>> my_list
['a', 2, 3, 4, 5]
```
If we want to add to a list we can use the `.append` method. This is an example of a method that modifies the object that is calling the method:
```python
>>> my_list.append(6)
>>> my_list.append(7)
>>> my_list
['a', 2, 3, 4, 5, 6, 7]
```
Lists can be added together (concatenated):
```python
>>> my_list + [8, 9, 10]
['a', 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> my_list += [8, 9, 10]
>>> my_list
['a', 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
Items in lists can be set using slices also:
```python
>>> my_list[1:3] = ['b', 'c']
>>> my_list
['a', 'b', 'c', 4, 5, 6, 7, 8, 9, 10]
# Replacing 2 sized slice with length 3 list inserts new element
>>> my_list[3:5] = ['d', 'e', 'f']
>>> print(my_list)
['a', 'b', 'c', 'd', 'e', 'f', 6, 7, 8, 9, 10]
>>> len(my_list)
11
```
We can remove a section of a `list` by assigning an empty `list` to the slice:
```python
>>> my_list = ['a', 'b', 'c', 'd', 5, 6, 7]
>>> my_list[4:] = []
>>> my_list
['a', 'b', 'c', 'd']
```
Removing items from a `list` based on value can be done using the `.remove` method:
```python
>>> my_list.remove('b')
>>> my_list
['a', 'c', 'd']
```
Attempting to remove and item that isn't in the `list` will result in an error:
```python
>>> my_list.remove('f')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```
Items can also be removed from the end of a list using the `pop` method:
```python
>>> my_list = ['a', 'c', 'd']
>>> my_list.pop()
'd'
>>> my_list
['a', 'c']
```
We can also use the `pop` method to remove items at a specific index:
```python
>>> my_list.pop(0)
'a'
>>> my_list
['c']
>>> my_list.pop(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> [].pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop from empty list
```

#### Tuples and Ranges
The most common immutable [sequence type](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) that we're going to work with is going to be the [tuple](https://docs.python.org/3/library/stdtypes.html#tuple). We'll also look at the [range](https://docs.python.org/3/library/stdtypes.html#range) type as an alternative to a sequential [list](https://docs.python.org/3/library/stdtypes.html#list).

##### Tuples
Tuples are a fixed-width, immutable sequence type. We create tuples using parenthesis (`(`, `)`) and at least one comma (,):
```python
>>> point = (2.0, 3.0)
```
Since tuples are immutable, we don't have access to the same methods that we do on a list. We can use tuples in some operations like concatenation, but we can't change the original tuple that we created.
```python
>>> point_3d = point + (4.0,)
>>> point_3d
(2.0, 3.0, 4.0)
```
One interesting characteristic of tuples is that we can unpack them into multiple variables at the same time:
```python
>>> x, y, z = point_3d
>>> x
2.0
>>> y
3.0
>>> z
4.0
```
The time we're most likely to see tuples will be when looking at a format string that's compatible with Python 2:
```python
>>> print("My name is: %s %s" % ("Mohammad Mahdi", "Roozitalab"))
My name is: Mohammad Mahdi Roozitalab
```

##### Ranges
Ranges are an immutable sequence type that defines a start, a stop, and a step value, and then the values within are calculated as it is interacted with. This allows for ranges to be used in place of sequential lists and while taking less memory and including more items.
```python
>>> my_range = range(10)
>>> my_range
range(0, 10)
>>> list(my_range)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 14, 2))
[1, 3, 5, 7, 9, 11, 13]
```
Notice that the "stop" value is not included in the range, the values are all up-until the stop.

#### Dictionaries
We will use [dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) type to hold onto key/value information in Python.

[dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) is the main mapping type that we'll use in Python. This object is comparable to a Hash or "associative array" in other languages.
We will use it to hold onto key/value information in Python.

We create dictionary literals by using curly braces (`{` and `}`), separating keys from values using colons (`:`), and separating key/value pairs using commas (`,`). Here's an example dictionary:
```python
>>> ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
>>> ages
{'kevin': 59, 'alex': 29, 'bob': 40}
```
We can read a value from a dictionary by subscripting using the key:
```python
>>> ages['kevin']
59
>>> ages['billy']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'billy'
```
Keys can be added and their value may be changed using subscripting and assignment:
```python
>>> ages['kayla'] = 21
>>> ages
{'kevin': 59, 'alex': 29, 'bob': 40, 'kayla': 21}
```
Items can be removed from a dictionary using the `del` statement or by using the `pop` method:
```python
>>> del ages['kevin']
>>> ages
{'alex': 29, 'bob': 40, 'kayla': 21}
>>> del ages
>>> ages
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ages' is not defined
>>> ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
>>> ages.pop('alex')
29
>>> ages
{'kevin': 59, 'bob': 40}
>>> {}.pop('billy')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'billy'
```
Since this is our second time running into a `KeyError` it's worth looking at a way to avoid these when we're attempting to read data from a dictionary. For that, we can use the get method:
```python
>>> ages.get('kevin')
59
>>> ages.get('billy')
>>>
```
Now we're receiving `None` instead of raising an error when we try to get the value for a key that doesn't exist.

It's not uncommon to want to know what keys or values we have without caring about the pairings. For that situation we have the `values` and `keys` methods:
```python
>>> ages = {'kevin': 59, 'bob': 40}
>>> ages.keys()
dict_keys(['kevin', 'bob'])
>>> list(ages.keys())
['kevin', 'bob']
>>> ages.values()
dict_values([59, 40])
>>> list(ages.values())
[59, 40]
```

##### Alternative ways to create a `dict` using Keyword Arguments
There are a few other ways to create dictionaries that we might see, those being using the `dict` constructor with key/value arguments and a list of tuples:
```python
>>> weights = dict(kevin=160, bob=240, kayla=135)
>>> weights
{'kevin': 160, 'bob': 240, 'kayla': 135}
>>> colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
>>> colors
{'kevin': 'blue', 'bob': 'green', 'kayla': 'red'}
```

##### Things to note about dictionaries:
- Unlike Python 2 dictionaries, as of Python 3.6 keys are ordered in dictionaries. Will need `OrderedDict` if you want this to work on another version of Python.
- You can set the key to any **IMMUTABLE** type (no `list`)
- Avoid using things other than simple objects as keys.
- Each key can only have one value (so don't have duplicates when creating a `dict`)