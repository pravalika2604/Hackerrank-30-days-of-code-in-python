#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
l = len(a)
count = 0
for i in range(l):

    for i in range(l-1):
        if a[i]>a[i+1]:
            c = a[i]
            a[i] = a[i+1]
            a[i+1] = c
            count+=1
    # if count==0:
    #     break
print('Array is sorted in {} swaps.'.format(count))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[l-1]))
