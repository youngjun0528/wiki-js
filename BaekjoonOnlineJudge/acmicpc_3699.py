#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 주차 빌딩
# https://www.acmicpc.net/problem/3699

'''
2
1 5
-1 2 1 -1 3
3 6
-1 5 6 -1 -1 3
-1 -1 7 -1 2 9
-1 10 4 1 8 -1

'''

import collections
import sys

num = int(sys.stdin.readline().strip())

for n in range(num):
    row_col = str(sys.stdin.readline().strip()).split(' ')
    row = int(row_col[0])
    col = int(row_col[1])

    container = list()
    for r in range(row):
        car_arr = str(sys.stdin.readline().strip()).split(' ')
        container.append(collections.deque([int(x) for x in car_arr]))

    last = max(map(max, container))

    res = 0
    cur = 1

    move_check = True

    while cur <= last:
        for i in range(row):
            for j in range(col):
                if container[i][j] == cur:
                    y, x = i, j
                    if x < col - x:
                        d = 1
                    else:
                        x = col - x
                        d = 0
        for i in range(x):
            if d:
                container[y].append(container[y].popleft())
            else:
                container[y].appendleft(container[y].pop())

        res += y * 20 + x * 5
        cur += 1
    print(res)
