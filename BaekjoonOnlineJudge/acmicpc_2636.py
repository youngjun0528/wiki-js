#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 치즈 
# https://www.acmicpc.net/problem/2636

import copy

row_num = 0
col_num = 0
cheese = []
dy = [ -1,0,1,0 ]
dx = [ 0,1,0,-1 ]

def outair(x, y):
    global row_num
    global col_num
    global cheese
    global dy
    global dx
    if 0 <= x and x < row_num and 0 <= y and y < col_num :
        if cheese[x][y] == 0 and cheese[x][y] != 2:
            cheese[x][y] = 2
            for dir in range(0, 4, 1):
                nextx = x + dy[dir]
                nexty = y + dx[dir]
                outair(nextx, nexty)

def main(inputData):
    global row_num
    global col_num
    global cheese
    global dy
    global dx

    row_num = len(inputData)
    col_num = len(inputData[0])
    cheese = copy.deepcopy(inputData)
    nextMelt = []
    cnt = 0
    melt = {}
    melt['map'] = inputData
    melt['count'] = sum([sum(data) for data in cheese])
    nextMelt.append(melt)
    while sum([sum(data) for data in cheese]) > 0:
        cnt += 1
        outair(0, 0)
        inputData_hole = copy.deepcopy(cheese)
        for i in range(row_num):
            for j in range(col_num):
                if cheese[i][j] == 1:
                    if cheese[i - 1][j] == 2 or \
                            cheese[i + 1][j] == 2 or \
                            cheese[i][j - 1] == 2 or \
                            cheese[i][j + 1] == 2:
                        inputData_hole[i][j] = 2
        for i in range(row_num):
            for j in range(col_num):
                if inputData_hole[i][j] == 2:
                    inputData_hole[i][j] = 0
        cheese = copy.deepcopy(inputData_hole)
        melt = {}
        melt['map'] = inputData_hole
        melt['count'] = sum([sum(data) for data in cheese])
        nextMelt.append(melt)


    # for i in range(len(nextMelt)):
    #     data = nextMelt[i]
    #     print(data['count'])
    #     print(data['map'])
    #     print("====================")
    print(len(nextMelt) - 1)
    nextMelt.pop()
    if nextMelt:
        print(nextMelt[-1]['count'])
    else:
        print(0)


import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    row_col = sys.stdin.readline().strip().split(" ")
    inputData = []
    for cnt in range(int(row_col[0])):
        row = sys.stdin.readline().strip().split(" ")
        inputData.append([int(data) for data in row])
    main(inputData)
