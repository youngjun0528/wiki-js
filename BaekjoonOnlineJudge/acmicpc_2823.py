#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 유턴 싫어
# https://www.acmicpc.net/problem/2823

'''
4 3
XXX
X.X
X.X
XXX

4 3
X.X
XXX
XXX
X.X

3 9
...XXX...
.X.....X.
...XXX...

2 4
....
X...

3 5
.....
XX.X.
XX...
'''


import sys

def debug_print(obj):
    for d in obj:
        print(d)
    print("----------------")

row, col = map(int, sys.stdin.readline().rstrip().split())

matrix = list()

for i in range(row):
    temp_row = list(str(sys.stdin.readline().rstrip()))
    matrix.append(temp_row)

debug_print(matrix)

result = True

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.':
            cnt = 0
            if i-1 >= 0 and matrix[i-1][j] == '.':
                cnt += 1
            if j-1 >= 0 and matrix[i][j-1] == '.':
                cnt += 1
            if i+1 < row and matrix[i+1][j] == '.':
                cnt += 1
            if j+1 < col and  matrix[i][j+1] == '.':
                cnt += 1
            if cnt > 1:
                continue
            else:
                result = False
        if not result:
            break
    if not result:
        break

if result:
    print(0)
else:
    print(1)
