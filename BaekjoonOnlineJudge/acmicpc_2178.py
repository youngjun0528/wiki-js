#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys
sys.setrecursionlimit(10**6)

from collections import deque

def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = dist[at] + [next]
                q.append(next)
    return dist[end]


if __name__ == '__main__':
    row_col = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    row = row_col[0]
    col = row_col[1]
    matrix = []
    for cnt in range(row):
        row_data = [int(x) for x in sys.stdin.readline().strip()]
        matrix.append(row_data)

    num_matrix = [[0] * col for x in range(row)]
    num = 1
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                num_matrix[i][j] = num
                num += 1

    graph = {}
    for i in range(row):
        for j in range(col):
            if num_matrix[i][j] > 0:
                result = []
                if i-1 >= 0 and num_matrix[i-1][j] > 0:
                    result.append(str(num_matrix[i-1][j]))
                if i+1 < row and num_matrix[i+1][j] > 0:
                    result.append(str(num_matrix[i+1][j]))
                if j-1 >= 0 and num_matrix[i][j-1] > 0:
                    result.append(str(num_matrix[i][j-1]))
                if j+1 < col and num_matrix[i][j+1] > 0:
                    result.append(str(num_matrix[i][j+1]))
                graph[str(num_matrix[i][j])] = result

    end = num_matrix[row-1][col-1]
    path = find_shortest_path(graph, '1', str(end))
    print(len(path))

    
