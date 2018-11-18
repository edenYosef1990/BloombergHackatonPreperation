#Problem        : Base Arithmetic
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

def numberToBase(digit):
    if(digit>='0' and digit<='9'):
        return int(digit)+1
    else:
        return (ord(digit)-ord('A'))+11
        
def DigitToNum(digit):
    if(digit>='0' and digit<='9'):
        return digit
    else:
        return((ord(digit)-ord('A'))+10)
        
def minBase(number):
    max_base_X=0; 
    for c in number:
        temp_num = numberToBase(c)
        max_base_X=max_base_X if (int(temp_num) <= int(max_base_X)) else temp_num
    return max_base_X

def CalcNum(Number,base):
    finalNum=0
    multi=0
    for c in reversed(str(Number)):
        finalNum = int(finalNum) + int(DigitToNum(c))*(pow(base,multi))
        multi = multi+1
    return finalNum

mySum=0    
for line in data:
    mySum = mySum + int(CalcFirstNum(line,minBase(line)))
print(mySum)