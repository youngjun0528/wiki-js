#!/usr/bin/python
# -*- coding=utf-8 -*-

# 나는 요리사다
# https://www.acmicpc.net/submit/2953/13460786

def main(inputData):
    # {1: ['5', '4', '4', '5'], 2: ['5', '4', '4', '4'], 3: ['5', '5', '4', '4'], 4: ['5', '5', '5', '4'], 5: ['4', '4', '4', '5']}
    result = {}
    for data in inputData.items():
        result[data[0]] = sum([int(d) for d in data[1]])

    sort_data = sorted(result, key=lambda x: result[x], reverse=True)
    print(str(sort_data[0]) + ' ' + str(result[sort_data[0]]))

import sys
if __name__ == '__main__':
    inputData = {}
    for cnt in range(1, 6):
        data = sys.stdin.readline().strip().split(' ')
        inputData[cnt] = data
    main(inputData)

    
