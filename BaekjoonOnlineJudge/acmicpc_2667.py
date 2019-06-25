#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 단지번호붙이기 
# https://www.acmicpc.net/problem/2667

'''
NXN 행렬에서 인접한 영토가 1이면 하나의 영토로 판단합니다.
아래 예제에서는 아래 영역을 하나의 영토라고 판단합니다.
[0,1], [0,2], [1,1], [1,2], [3,0], [3,1], [3,2]
동일한 방식으로 아래 예제에서는 3개의 영토가 존해하며
각 영토의 크기는 7개, 8개, 9개 입니다.

[0, 1, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 1, 1],
[0, 1, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 0, 0, 0]
'''

# 재귀함수를 사용하기 위한 전역변수
# 주어진 영역
map = []
# 방문 여부를 판별하기 위한 변수
visitedMap = []
# 영역 갯수
holeCnt = 0

def main(inputData):
    global holeCnt
    global visitedMap
    global map

    # 값 할당
    map = list(inputData)

    # 방문 포인트를 저장하기 위한 2차원 배열 초기화
    visitedMap = [[0]*len(map) for i in range(len(map))]

    # 영역 Count 변수
    # map 에는 1로 저장되어 있으므로 2부터 시작하여 영역 표시
    curFill = 2

    # 전체 배열 순회
    for i in range(len(map)):
        for j in range(len(map)):
            # 현재 Row 와 Col
            curRow = i
            curCol = j
            # 영역 Count
            holeCnt = 0
            # 깊이우선탐색 시작
            dfs(curRow, curCol, curFill)
            # 깊이우선탐색 이후 영역이 존재한다면 영역 Count 를 1 증가시키고 진행
            if holeCnt > 0:
                curFill += 1
    print(curFill-2)

    result = {}
    for check in range(2, int(curFill)):
        result[check] = 0
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j] == check:
                    result[check] += 1

    for d in sorted(result.values()):
        print(d)


def dfs(curRow, curCol, curFill):
    global holeCnt
    global visitedMap
    global map

    if visitedMap[curRow][curCol] == 1:
        return
    visitedMap[curRow][curCol] = 1
    if map[curRow][curCol] == 1:
        holeCnt += 1
        map[curRow][curCol] = curFill

        # 위로 이동
        if curRow - 1 >= 0 and map[curRow - 1][curCol] == 1:
            dfs(curRow - 1, curCol, curFill)
        # 아래로 이동
        if curRow + 1 < len(map) and map[curRow + 1][curCol] == 1:
            dfs(curRow+1, curCol, curFill)
        # 왼쪽으로 이동
        if curCol - 1 >= 0 and map[curRow][curCol - 1] == 1:
            dfs(curRow, curCol-1, curFill)
        # 오른쪽으로 이동
        if curCol + 1 < len(map) and map[curRow][curCol + 1] == 1:
            dfs(curRow, curCol + 1, curFill)

    return

import sys
if __name__ == '__main__':
    num = sys.stdin.readline()
    map = []
    for cnt in range(int(num)):
        map.append([int(data) for data in sys.stdin.readline().strip()])
    main(map)

    
