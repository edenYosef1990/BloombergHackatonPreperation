#Problem        : Expecto Palindronum
#Language       : Python
#Compiled Using : py_compile
#Version        : Python 2.7.8
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

from __future__ import print_function
import sys

data = sys.stdin.read().splitlines()


def minPaliLength(word):
    for i in reversed(range(0,len(word))):
        temp_word = word[i:len(word)][::-1]
        tested_word = temp_word+str(word)
        if tested_word == tested_word[::-1]:
            return len(tested_word)
    return 2*len(word)-1

for line in data:
    if(len(line)>1):
        print(minPaliLength(line))
    else:
        print(len(line))