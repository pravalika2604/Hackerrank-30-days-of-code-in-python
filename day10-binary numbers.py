#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    l=[]
    n = int(input())
    while(n > 0):
        rem = n%2
        #print(rem)
        n = int(n/2)
        l.append(rem)
#print(l)   
c=0
max=0
count=0
for i in l:
    count=count+1
    if i==1:
        c+=1
    if count==len(l):
        if c>max:
            max=c
        c=0
    if i==0:
        if c>max:
            max=c
        c=0
print(max)

