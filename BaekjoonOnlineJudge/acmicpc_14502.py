#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 연구소
# https://www.acmicpc.net/problem/14502

'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''


# 재귀함수를 사용하기 위한 전역변수
# 주어진 영역
map = []
# 방문 여부를 판별하기 위한 변수
visitedMap = []
# 영역 갯수
holeCnt = 0

def debug_print(obj):
    for d in obj:
        print(d)
    print("----------------")


def dfs(curRow, curCol, curFill):
    global holeCnt
    global visitedMap
    global map

    if visitedMap[curRow][curCol] == 1:
        return
    visitedMap[curRow][curCol] = 1
    if map[curRow][curCol] == 2 or map[curRow][curCol] == 0:
        holeCnt += 1
        map[curRow][curCol] = curFill

        # 위로 이동
        if curRow - 1 >= 0 and map[curRow - 1][curCol] == 0:
            dfs(curRow - 1, curCol, curFill)
        # 아래로 이동 / row_size 보다 작게
        if curRow + 1 < len(map) and map[curRow + 1][curCol] == 0:
            dfs(curRow+1, curCol, curFill)
        # 왼쪽으로 이동
        if curCol - 1 >= 0 and map[curRow][curCol - 1] == 0:
            dfs(curRow, curCol-1, curFill)
        # 오른쪽으로 이동 / col_size 보다 작게
        if curCol + 1 < len(map[0]) and map[curRow][curCol + 1] == 0:
            dfs(curRow, curCol + 1, curFill)

    return

import sys
row_col = str(sys.stdin.readline().strip()).split(' ')
row = int(row_col[0])
col = int(row_col[1])

matrix = []
for i in range(row):
    row_data = str(sys.stdin.readline().strip()).split(' ')
    row_mat = []
    for j in range(col):
        row_mat.append(int(row_data[j]))
    matrix.append(row_mat)

#debug_print(matrix)

# 벽세우기
# 초기화
init_mat = [[0]*col for x in range(row)]
num = 0
for i in range(row):
    for j in range(col):
       init_mat[i][j] = str(num)
       num += 1

#debug_print(init_mat)
total_num = col * row
total_arr = [str(x) for x in range(total_num)]
import itertools
combination_arr = list(itertools.combinations(total_arr, 3))

min_cnt = 0

import copy
for zip_sub in combination_arr:
    check_num = True
    check_mat = copy.deepcopy(matrix)
    for check in zip_sub:
        for i in range(row):
            for j in range(col):
                if init_mat[i][j] == check:
                    check_mat[i][j] = 1
                    if matrix[i][j] > 0:
                        check_num = False

    if check_num is True:
        #debug_print(check_mat)
        # 값 할당
        map = list(check_mat)

        # 방문 포인트를 저장하기 위한 2차원 배열 초기화
        col_size = len(map[0])
        row_size = len(map)
        visitedMap = [[0]*len(map[0]) for i in range(len(map))]

        # 영역 Count 변수
        # map 에는 1로 저장되어 있으므로 2부터 시작하여 영역 표시
        curFill = 2

        # 전체 배열 순회
        for i in range(row):
            for j in range(col):
                # 현재 Row 와 Col
                curRow = i
                curCol = j
                if map[curRow][curCol] == 2:
                    # 영역 Count
                    holeCnt = 0
                    # 깊이우선탐색 시작
                    dfs(curRow, curCol, curFill)
                    # 깊이우선탐색 이후 영역이 존재한다면 영역 Count 를 1 증가시키고 진행
                    #print(holeCnt)
                    if holeCnt > 0:
                        curFill += 1

        count = 0
        for i in range(row):
            for j in range(col):
                if map[i][j] == 0:
                    count += 1
        if min_cnt < count:
            min_cnt = count

print(min_cnt)

