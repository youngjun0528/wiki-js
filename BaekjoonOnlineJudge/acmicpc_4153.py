#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 직각삼각형
# https://www.acmicpc.net/problem/4153

'''
6 8 10
25 52 60
5 12 13
0 0 0
'''

import sys
import queue

while True:
    square = str(sys.stdin.readline().strip()).split(' ')
    a = int(square[0])
    b = int(square[1])
    c = int(square[2])

    if (a + b + c) == 0:
        break

    if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        print("right")
    else:
        print("wrong")


