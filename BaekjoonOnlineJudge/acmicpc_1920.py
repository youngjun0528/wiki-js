#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 수 찾기
# https://www.acmicpc.net/problem/1920

def main(A, S):
    for d in S:
        if d in A:
            print(1)
        else:
            print(0)

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

import sys
if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    A = sorted([int(x) for x in sys.stdin.readline().strip().split(' ')])
    M = int(sys.stdin.readline().strip())
    S = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    for d in S:
        if binary_search(d, A) is not None:
            print(1)
        else:
            print(0)
