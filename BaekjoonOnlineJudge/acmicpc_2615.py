#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 오목 
# https://www.acmicpc.net/problem/2615

import sys
import copy

if __name__ == '__main__':
    matrix = []
    for cnt in range(19):
        row_data = [int(x) for x in sys.stdin.readline().strip().replace(' ','')]
        matrix.append(row_data)

    # 1이 이기는 경우
    num_matrix = [[0] * 19 for x in range(19)]
    num = 1
    for i in range(19):
        for j in range(19):
            if matrix[i][j] == 1:
                num_matrix[i][j] = num
                num += 1
    graph_first = {}
    for i in range(19):
        for j in range(19):
            if num_matrix[i][j] > 0:
                # 가로
                result = []
                if i == 0 or num_matrix[i - 1][j] == 0:
                    for cnt in range(1, 6):
                        if i + cnt < 19 and num_matrix[i + cnt][j] > 0:
                            result.append(str(num_matrix[i + cnt][j]))
                        else:
                            break
                if len(result) == 4:
                    graph_first[str(num_matrix[i][j])] = result
                    break

                # 세로
                result = []
                if j == 0 or num_matrix[i][j - 1] == 0:
                    for cnt in range(1, 6):
                        if j + cnt < 19 and num_matrix[i][j + cnt] > 0:
                            result.append(str(num_matrix[i][j + cnt]))
                        else:
                            break
                if len(result) == 4:
                    graph_first[str(num_matrix[i][j])] = result
                    break

                # 우하 대각선
                result = []
                if i == 18 or j == 0 or num_matrix[i - 1][j - 1] == 0:
                    for cnt in range(1, 6):
                        if j + cnt < 19 and i + cnt < 19 and num_matrix[i + cnt][j + cnt] > 0:
                            result.append(str(num_matrix[i + cnt][j + cnt]))
                        else:
                            break
                if len(result) == 4:
                    graph_first[str(num_matrix[i][j])] = result
                    break

                # 우상 대각선
                result = []
                if i == 18 or j == 0 or num_matrix[i + 1][j - 1] == 0:
                    for cnt in range(1, 6):
                        if j + cnt < 19 and i - cnt >= 0 and num_matrix[i - cnt][j + cnt] > 0:
                            result.append(str(num_matrix[i - cnt][j + cnt]))
                        else:
                            break
                if len(result) == 4:
                    graph_first[str(num_matrix[i][j])] = result
                    break

    # 2이 이기는 경우
    num_matrix_2 = [[0] * 19 for x in range(19)]
    num = 1
    for i in range(19):
        for j in range(19):
            if matrix[i][j] == 2:
                num_matrix_2[i][j] = num
                num += 1
    graph_second = {}
    for i in range(19):
        for j in range(19):
            if num_matrix_2[i][j] > 0:
                # 가로
                result = []
                if i == 0 or num_matrix_2[i - 1][j] == 0:
                    for cnt in range(1, 6):
                        if i + cnt < 19 and num_matrix_2[i + cnt][j] > 0:
                            result.append(str(num_matrix_2[i + cnt][j]))
                        else:
                            break
                if len(result) == 4:
                    graph_second[str(num_matrix_2[i][j])] = result
                    break

                # 세로
                result = []
                if j == 0 or num_matrix_2[i][j - 1] == 0:
                    for cnt in range(1, 6):
                        if j + cnt < 19 and num_matrix_2[i][j + cnt] > 0:
                            result.append(str(num_matrix_2[i][j + cnt]))
                        else:
                            break
                if len(result) == 4:
                    graph_second[str(num_matrix_2[i][j])] = result
                    break

                # 우하 대각선
                result = []
                if i == 18 or j == 0 or num_matrix_2[i - 1][j - 1] == 0:
                    for cnt in range(1, 6):
                        if j + cnt < 19 and i + cnt < 19 and num_matrix_2[i + cnt][j + cnt] > 0:
                            result.append(str(num_matrix_2[i + cnt][j + cnt]))
                        else:
                            break
                if len(result) == 4:
                    graph_second[str(num_matrix_2[i][j])] = result
                    break

                # 우상 대각선
                result = []
                if i == 18 or j == 0 or num_matrix_2[i + 1][j - 1] == 0:
                    for cnt in range(1, 6):
                        if j + cnt < 19 and i - cnt >= 0 and num_matrix_2[i - cnt][j + cnt] > 0:
                            result.append(str(num_matrix_2[i - cnt][j + cnt]))
                        else:
                            break
                if len(result) == 4:
                    graph_second[str(num_matrix_2[i][j])] = result
                    break

    check_one = True
    if len(graph_first) > 0:
        for d in graph_first.items():
            if len(d[1]) == 4:
                print(1)
                i = 0
                for mat in num_matrix:
                    if mat.count(int(d[0])) > 0:
                        print(str(i + 1) + ' ' + str(mat.index(int(d[0])) + 1))
                        check_one = False
                    i += 1

    check_sec = True
    if len(graph_second) > 0:
        for d in graph_second.items():
            if len(d[1]) == 4:
                print(2)
                i = 0
                for mat in num_matrix_2:
                    if mat.count(int(d[0])) > 0:
                        print(str(i + 1) + ' ' + str(mat.index(int(d[0])) + 1))
                        check_sec = False
                    i += 1

    if check_one and check_sec:
        print(0)

        
