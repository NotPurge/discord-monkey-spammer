import os
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()

os.system('cls && title [Monkey Mass Reporter] - Imports Installer')
os.system('pip install requests')
os.system('pip install sys')
os.system('pip install colorama')
os.system('pip install os')
os.system('pip install threading')
os.system('pip install time')
print(Fore.YELLOW)
print('[>] Finished installing required imports.')
print('[>] You may now close this prompt and run `monkey.py`')
sys.exit()
