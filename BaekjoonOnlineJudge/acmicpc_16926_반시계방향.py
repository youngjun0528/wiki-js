#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 배열 돌리기 1 - 반시계방향
# https://www.acmicpc.net/problem/16926

'''
4 4 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''


import sys
sys.setrecursionlimit(10**6)

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
            dfs(x - 1, y, 3, r + 1, Range, Orig)

    if dir == 1: # Move West
        if y - 1 >= Range:
            dfs(x, y - 1, dir, r + 1, Range, Orig)
        else:
            dfs(x + 1, y, 2, r + 1, Range, Orig)

    if dir == 2: # Move South
        if x + 1 < row - Range:
            dfs(x + 1, y, dir, r + 1, Range, Orig)
        else:
            dfs(x, y + 1, 0, r + 1, Range, Orig)

    if dir == 3: # Move North
        if x - 1 >= Range:
            dfs(x - 1, y, dir, r + 1, Range, Orig)
        else:
            dfs(x, y - 1, 1, r + 1, Range, Orig)


row, col, rotate = map(int, sys.stdin.readline().rstrip().split())

matrix = list()
visit = [[0]*col for x in range(row)]
change_visit = [[0]*col for x in range(row)]

for i in range(row):
    temp_row = list(map(int, sys.stdin.readline().rstrip().split()))
    matrix.append(temp_row)

# N = row
# M = col
# R = retate

rotate_idx = 0
if row > col:
    rotate_idx = col // 2
else:
    rotate_idx = row // 2

check_row = row
check_col = col
#
for rp in range(rotate_idx):
    if (check_row * check_col - 4) > 0:
        rotate = rotate % (check_row * check_col - 4)

    x = rp
    y = rp

    #
    for i in range(y, col-rp):
        if visit[row - 1 - rp][i] == 0:
            dfs(row - 1 - rp, i, 0, 0, rp, matrix[row - 1 - rp][i])
            visit[row - 1 - rp][i] = 1
    # # #
    for i in range(row-1-rp, rp-1, -1):
        if visit[i][col - 1 - rp] == 0:
            dfs(i, col - 1 - rp, 3, 0, rp, matrix[i][col - 1 - rp])
            visit[i][col - 1 - rp] = 1

    for i in range(col - 1 - rp, rp-1, -1):
        if visit[x][i] == 0:
            dfs(x, i, 1, 0, rp, matrix[x][i])
            visit[x][i] = 1

    for i in range(x, row-rp):
        if visit[i][y] == 0:
            dfs(i, y, 2, 0, rp, matrix[i][y])
            visit[i][y] = 1

    check_row = check_row - 2
    check_col = check_col - 2
    # #

for d in change_visit:
    print(' '.join(map(str,d)))
