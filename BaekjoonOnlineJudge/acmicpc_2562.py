#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 최댓값 
# https://www.acmicpc.net/problem/2562

def main(inputData):
    sort_data = sorted(inputData, reverse=True)
    max_val = sort_data[0]
    index = inputData.index(max_val)
    print(max_val)
    print(index+1)

import sys
if __name__ == '__main__':
    inputData = []
    for cnt in range(9):
        inputData.append(int(sys.stdin.readline().strip()))
    main(inputData)

    
