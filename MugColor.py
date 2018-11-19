#Problem        : Mug Color
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

colorsList = ['White','Black','Blue','Red','Yellow']

lines = list(data)
linesLen = int(lines[0])+1
for i in range(1,linesLen):
    if lines[i] in colorsList:
        colorsList.remove(lines[i])
print(colorsList[0])
#for line in data :
#    print(line)
