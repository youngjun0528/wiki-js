#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 명령 프롬프트
# https://www.acmicpc.net/problem/1032

def main(inputData):
    result = []
    inputData.sort(key=len, reverse=False)
    testData = inputData.pop(0)

    for idx in range(len(testData)):
        check = True
        for data in inputData:
            if data[idx] != testData[idx]:
                check = False
        if check:
            result.append(testData[idx])
        else:
            result.append('?')
    print(''.join(result))

import sys
if __name__ == '__main__':
    num = sys.stdin.readline()
    map = []
    for cnt in range(int(num)):
        map.append(sys.stdin.readline().strip())
    main(map)
