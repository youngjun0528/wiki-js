#!/usr/bin/python
# -*- coding=utf-8 -*-

# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

def main(inputData):
    check = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    cnt = 0
    for c in check:
        if c in inputData:
            cnt += 1
            inputData = inputData.replace(c, '0')
    print(len(inputData))

import sys
if __name__ == '__main__':
    inputData = sys.stdin.readline().strip()
    main(inputData)

    
