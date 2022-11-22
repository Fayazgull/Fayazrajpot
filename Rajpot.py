#coding=utf-8
import sys,time
from platform import uname
from os import path,system
arch=uname().machine.lower()
if "aarch" in arch:
    arch="aarch"
    print('\033[1;32m\nCongratulatings! Your Deviec Support This Tools');time.sleep(1)
else:
    print('\033[1;31m\nSorry System not support this tools');sys.exit()

try:
    if sys.argv[1]=='update':
        system('cd $HOME && cd Rajpot && rm -f *')
        system("curl -L https://raw.githubusercontent.com/Rajpot110/Rajpot/main/Rajpot.py -o Rajpot.py && python Rajpot.py")
except:
    pass
if path.isfile("dz.so"):
    pass
else:
    system("curl -L https://raw.githubusercontent.com/Rajpot110/Data/main/dz.so -o dz.so")
system('clear')
print('\n\n\033[1;37m[•] This tools only for 64bit device ')
print('\n[1] Start Cloning V1.3.9 \n[2] Start Random Cloning V1.3.8 (Updated)\n[3] Check Update \n')
xd=input('[•] choose: ')
if xd in ['1','01']:
    if path.isfile('Rajpot.so'):
        import Rajpot
    else:
        system("curl -L https://raw.githubusercontent.com/Rajpot110/Data/main/Rajpot.so -o Rajpot.so")
        import AKING
elif xd in ['2','02']:
    if path.isfile('Random.so'):
        import Random
    else:
        system("curl -L https://raw.githubusercontent.com/Rajpot110/Data/main/Random.so -o Random.so")
        import Random
else:
        print('\n[•] Checking updates...')
        system('python Rajpot.py update')
