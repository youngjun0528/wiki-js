#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 윷놀이
# https://www.acmicpc.net/problem/2490

'''
0 1 0 1
1 1 1 0
1 1 1 1
'''

import sys

def debug_print(obj):
    for d in obj:
        print(d)
    print("----------------")

# 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개)
# A - 0 : 1 , 1 : 3 = 3
# B - 0 : 2 , 1 : 2 = 2
# C - 0 : 3 , 1 : 1 = 1
# D - 0 : 4 , 1 : 0 = 0
# E - 0 : 0 , 1 : 4 = 4
for _ in range(3):
    result = list(map(int, sys.stdin.readline().rstrip().split()))
    import collections

    test = collections.Counter(result)
    check = {3 : 'A', 2 : 'B', 1 : 'C', 0 : 'D', 4 : 'E'}
    print(check[sum(result)])



