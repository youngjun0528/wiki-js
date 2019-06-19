#!/usr/bin/python
# -*- coding=utf-8 -*-

# KMP는 왜 KMP일까?
# https://www.acmicpc.net/problem/2902

def main(inputData):
    result = inputData[0]
    for cnt in range(len(inputData)):
        data = inputData[cnt]
        if data == '-':
            result += inputData[cnt+1]
    print(result)

import sys
if __name__ == '__main__':
    inputData = sys.stdin.readline().strip()
    main(inputData)
