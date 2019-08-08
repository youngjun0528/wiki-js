#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 배열 돌리기 1 - 시계방향
# https://www.acmicpc.net/problem/16926

'''
4 4 1
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''

def debug_print(obj):
    for d in obj:
        print(d)
    print("----------------")


def dfs(x, y, dir, r, Range, Orig):
    global row
    global col
    global rotate
    global change_visit
    if r == rotate:
        change_visit[x][y] = Orig
        return

    if dir == 0: # Move East
        if y + 1 < col - Range:
            dfs(x, y + 1, dir, r + 1, Range, Orig)
        else:
            dfs(x + 1, y, 2, r + 1, Range, Orig)

    if dir == 1: # Move West
        if y - 1 >= Range:
            dfs(x, y - 1, dir, r + 1, Range, Orig)
        else:
            dfs(x - 1, y, 3, r + 1, Range, Orig)

    if dir == 2: # Move South
        if x + 1 < row - Range:
            dfs(x + 1, y, dir, r + 1, Range, Orig)
        else:
            dfs(x, y - 1, 1, r + 1, Range, Orig)

    if dir == 3: # Move North
        if x - 1 >= Range:
            dfs(x - 1, y, dir, r + 1, Range, Orig)
        else:
            dfs(x + 1, y, 2, r + 1, Range, Orig)

import sys
num_str = str(sys.stdin.readline().strip()).split()
row = int(num_str[0])
col = int(num_str[1])
rotate = int(num_str[2])

matrix = list()
visit = [[0]*row for x in range(col)]
change_visit = [[0]*row for x in range(col)]

for i in range(row):
    row_str = str(sys.stdin.readline().strip()).split()
    temp_row = list()
    matrix.append(temp_row)


    for j in range(col):
        temp_row.append(int(row_str[j]))
# N = row
# M = col
# R = retate

rotate_idx = 0
if row > col:
    rotate_idx = col // 2
else:
    rotate_idx = row // 2

# qkstlr
for rp in range(rotate_idx):
    x = rp
    y = rp

    for i in range(col - 1 - rp, rp-1, -1):
        if visit[x][i] == 0:
            dfs(x, i, 0, 0, rp, matrix[x][i])
            visit[x][i] = 1

    for i in range(x, row-rp):
        if visit[i][y] == 0:
            dfs(i, y, 3, 0, rp, matrix[i][y])
            visit[i][y] = 1
    #
    for i in range(y, col-rp):
        if visit[row - 1 - rp][i] == 0:
            dfs(row - 1 - rp, i, 1, 0, rp, matrix[row - 1 - rp][i])
            visit[row - 1 - rp][i] = 1
    # # #
    for i in range(row-1-rp, rp-1, -1):
        if visit[i][col - 1 - rp] == 0:
            dfs(i, col - 1 - rp, 2, 0, rp, matrix[i][col - 1 - rp])
            visit[i][col - 1 - rp] = 1
    # #
    break

debug_print(matrix)

debug_print(change_visit)

debug_print(visit)

