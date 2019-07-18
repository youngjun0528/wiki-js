#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

'''
5
3 -4
1 -1
1 1
2 2
3 3
'''

import sys
import queue

num = int(sys.stdin.readline().strip())

num_arr = list()
for cnt in range(num):
    num_str = str(sys.stdin.readline().strip()).split(' ')
    num_set = (int(num_str[0]), int(num_str[1]))
    num_arr.append(num_set)

sorted_C_union = sorted(num_arr, key=lambda x: (x[0], x[1]))

for str_prt in sorted_C_union:
    print(str_prt[0], str_prt[1])
