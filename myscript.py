#import myFunction
#import myFunction as m
from myFunction import Command

Command('pwd')


import os
import platform
import sys


if platform.system() == 'Linux':
        os.system('clear')
else:
        os.system('cls')


print(sys.argv[1])

sys.exit()




_DIR="/var/log"

for item in os.listdir(_DIR):
        path= os.path.join(_DIR, item)
        if os.path.isfile(path):
                print(f"{path}    is a file")
        else:
                print(f"{path}    is a directory")                        
                        
                        