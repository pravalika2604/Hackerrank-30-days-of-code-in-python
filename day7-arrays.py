#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    a1 = []
    while(n>0):
        a1.append(arr[n-1])
        n-=1
    for ele in a1:
        print(ele,end=' ')    

