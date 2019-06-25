#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 하얀 칸
# https://www.acmicpc.net/problem/1100

def main(inputData):
    # 체스판 초기화
    chess = [[0] * 8 for i in range(8)]
    # 체스판 검정 은 0, 흰색은 1
    for i in range(8):
        for j in range(8):
            if (i % 2 == 0) and (j % 2 == 0):
                chess[i][j] = 1
            if (i % 2 == 1) and (j % 2 == 1):
                chess[i][j] = 1
    result = 0
    for i in range(8):
        for j in range(8):
            if chess[i][j] == 1 and inputData[i][j] == 'F':
                result += 1
    print(result)


import sys
if __name__ == '__main__':
    map = []
    for cnt in range(8):
        map.append([data for data in sys.stdin.readline().strip()])
    main(map)

    
