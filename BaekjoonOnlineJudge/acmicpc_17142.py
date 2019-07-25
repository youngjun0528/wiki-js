#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 연구소 3
# https://www.acmicpc.net/problem/17142 

import sys
import collections
import itertools

def debug_print(obj):
    for d in obj:
        print(d)
    print("----------------")

def bfs(v):
    global v_c
    global matrix_temp
    q = collections.deque(v)
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    visited = [[False]*N for _ in range(N)]
    level = 0
    if v_c:
        for e in v:
            visited[e[0]][e[1]] = True

        while q:
            level += 1
            for _ in range(len(q)):
                v = q.popleft()
                for a in range(4):
                    i = v[0] + di[a]
                    j = v[1] + dj[a]
                    if 0 <= i <= N-1 and 0 <= j <= N-1 and not(visited[i][j]) and lab[i][j] != 1:
                        visited[i][j] = True
                        matrix_temp[i][j] = level
                        if lab[i][j] == 0:
                            v_c -= 1
                        if v_c == 0:
                            return level
                        q.append([i, j])
        #debug_print(matrix_temp)

        return -1
    else:
        return 0

num_str = str(sys.stdin.readline().strip()).split()
N = int(num_str[0])
M = int(num_str[1])

lab = []
virus = []
virus_cnt = 0
min_t = 999999

for i in range(N):
    temp_matrix = list()
    num_str = str(sys.stdin.readline().strip()).split()
    for c in range(N):
        temp_matrix.append(int(num_str[c]))
    lab.append(temp_matrix)
    for j, e in enumerate(temp_matrix):
        if e == 2:
            virus.append([i, j])
        elif e == 0:
            virus_cnt += 1

import copy
matrix_temp = copy.deepcopy(lab)
# debug_print(lab)
# debug_print(virus)

for virus_com in itertools.combinations(virus, M):
    v_c = virus_cnt
    t = bfs(virus_com)
    if t != -1 and min_t > t:
        min_t = t
if min_t == 999999:
    print(-1)
else:
    print(min_t)
