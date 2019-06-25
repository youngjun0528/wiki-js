#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 가로수 
# https://www.acmicpc.net/problem/2485

# 가능한 모든 가로수의 경우의 수를 확인하여 비교 

import sys

if __name__ == '__main__':
    num = int(sys.stdin.readline().strip())
    inputData = []
    for cnt in range(num):
        inputData.append(int(sys.stdin.readline().strip()))

    #print(inputData)
    #inputData = sorted(inputData)
    max = max(inputData)
    min = min(inputData)
    size = max - min + 1

    inputData_init = [x-min for x in inputData]
    #print(inputData_init)

    check_init = [0]*(size)
    #print(check_init)
    for data in inputData_init:
        check_init[data] = 1

    #print(check_init)

    #1
    result = {}
    for k in range(1, size):
        compare_arr = [0]*(size)
        compare_arr[0] = 1
        for cnt in range(1, size):
            if cnt % k == 0:
                compare_arr[cnt] = 1
        check = []
        for p in range(size):
            if check_init[p] == 1 and compare_arr[p] == 1:
                check.append(p)
        if check == inputData_init:
            result[k] = compare_arr.count(1) - num
    #print(result)

    a = sorted(result, key=lambda x:result[x])
    print(result[a[0]])





