#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 단어 공부
# https://www.acmicpc.net/problem/1157

'''
Mississipi
'''

import sys

def debug_print(obj):
    for d in obj:
        print(d)
    print("----------------")

result = str(sys.stdin.readline().rstrip()).upper()

import collections

if len(result) > 1:
    test = (collections.Counter(result).most_common(2))
    if test[0][1] == test[1][1]:
        print('?')
    else:
        print(test[0][0])
else:
    print(result)
