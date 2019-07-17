#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OX퀴즈
# https://www.acmicpc.net/problem/8958

'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''

import sys
import queue

num = int(sys.stdin.readline().strip())

for cnt in range(num):
    check_str = str(sys.stdin.readline().strip())

    sum = 0
    cnt = 1

    for i in check_str:
        if i == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1

    print(sum)



