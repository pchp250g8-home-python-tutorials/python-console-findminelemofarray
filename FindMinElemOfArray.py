# --coding:utf-8--
import os
import array
import random

os.system("cls")
print("Input a count of elements in array")
nElems = int(input())
print(f"Generating array by filling {nElems} elements:")
iNumbers = array.array('i')
for i in range(0, nElems) :
    nItem = random.randint(1, 100)
    iNumbers.append(nItem)
    print(iNumbers[i], end=" ")
iMin = iNumbers[0]
nIndex = 0
for i in range(1, nElems) :
    if iNumbers[i] < iMin :
        iMin = iNumbers[i]
        nIndex = i
print(f"\r\nFound minimum element:{iMin} with index {nIndex}")