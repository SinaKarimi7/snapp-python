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
