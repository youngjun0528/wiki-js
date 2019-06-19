#!/usr/bin/python
# -*- coding=utf-8 -*-

# 가로 세로 퍼즐
# https://www.acmicpc.net/problem/2784

def main(inputData):
    test = set()
    for i in range(6):
        for j in range(6):
            for k in range(6):
                if i != j and i != k and j != k:
                    result = []
                    result.append(inputData[i])
                    result.append(inputData[j])
                    result.append(inputData[k])
                    testCompare = list(inputData)
                    testCompare[i] = ''
                    testCompare[j] = ''
                    testCompare[k] = ''
                    if result[0][0] + result[1][0] + result[2][0] in testCompare:
                        testCompare[testCompare.index(result[0][0] + result[1][0] + result[2][0])] = ''
                        if result[0][1] + result[1][1] + result[2][1] in testCompare:
                            testCompare[testCompare.index(result[0][1] + result[1][1] + result[2][1])] = ''
                            if result[0][2] + result[1][2] + result[2][2] in testCompare:
                                testCompare[testCompare.index(result[0][2] + result[1][2] + result[2][2])] = ''
                                test.add(''.join(result))
    if len(test) > 0:
        a = sorted(test)
        for cnt in range(0,9,3):
            print(a[0][cnt]+a[0][cnt+1]+a[0][cnt+2])
    else:
        print(0)

import sys
if __name__ == '__main__':
    inputData = []
    for cnt in range(0, 6):
        data = sys.stdin.readline().strip()
        inputData.append(data)
    main(inputData)
