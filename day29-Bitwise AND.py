#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        # def getAnswer(n, k):
        #     power = int(math.log(n, 2)) - 1
        #     floor = 2**power

        #     maxNum = 0
        #     for i in range(floor+1, n+1):
        #         for j in range(1, i):
        #             test = i&j
        #             if test > maxNum and test < k:
        #                 maxNum = test
        #         if maxNum == k-1:
        #             break
        #     return maxNum
        # getAnswer(n, k)

        # maxk = 0
        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #         curk = i&j
        #         if curk > maxk and curk < k:
        #             maxk = curk
        #         if maxk == (k - 1):
        #             break
        #     if maxk == (k - 1):
        #         break

        # print (maxk)
        print(k-1 if ((k-1) | k) <= n else k-2)
        #print (max([a&b for a,b in combinations(range(1,n+1), 2) if a&b < k]))
        # l = []
        # for i in range(1,n+1):
        #     for j in range(i+1,n+1):
        #         l.append(i&j)
        # for i in l:
        #     if i>=k:
        #         l.remove(i)
        # print(max(l))
