#Problem        : Laundry Day
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

clothesDic = {}
lines = list(data)
linesLen = len(lines)
for i in range(0,linesLen):
    if lines[i] not in clothesDic.keys():
        clothesDic[lines[i]] = 1
    else:
        clothesDic[lines[i]] = int(clothesDic[lines[i]]) + 1

for key in sorted(clothesDic):
    if key.endswith(" sock"):
        numSocksPiers = round((clothesDic[key]- clothesDic[key] % 2)/2)
        NumSocksAlone = round(clothesDic[key] % 2)
        if(clothesDic[key]==1):
            print("0|"+key)
        else:
            print(str(numSocksPiers)+"|"+key)
            if(NumSocksAlone>0):
                print("0|"+key)
    else:
        print(str(int(clothesDic[key]))+"|"+key)