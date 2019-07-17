#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ATM 
# https://www.acmicpc.net/problem/11399

'''
5
3 1 4 3 2
'''

import sys
import queue

num = int(sys.stdin.readline().strip())
check_str = str(sys.stdin.readline().strip()).split()

check_int = [int(x) for x in check_str]

check_int.sort()

result = 0

for i in range(len(check_int)+1):
    print(check_int[:i])
    result += sum(check_int[:i])

print(result)
