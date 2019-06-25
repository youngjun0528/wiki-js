#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 후보 추천하기
# https://www.acmicpc.net/problem/1713

def main(photo_size, vote_cnt, inputData):
    # {학생번호: 투표수, 시간}
    result = {}
    for cnt in range(vote_cnt):
        if len(result) > (photo_size-1):
            if inputData[cnt] in result.keys():
                result[inputData[cnt]][0] = result[inputData[cnt]][0] + 1
            else:
                test = sorted(result, key=lambda x: (result[x][0], result[x][1]))[0]
                del result[test]
                result[inputData[cnt]] = [1, cnt]
        else:
            if inputData[cnt] in result.keys():
                result[inputData[cnt]][0] = result[inputData[cnt]][0] + 1
            else:
                result[inputData[cnt]] = [1, cnt]
    test_data = [int(x) for x in result.keys()]
    sort_data = sorted(test_data)
    result = ''
    for i in sort_data:
        result = result + str(i) + ' '
    print(result.rstrip())


import sys
if __name__ == '__main__':
    student = int(sys.stdin.readline().strip())
    num = int(sys.stdin.readline().strip())
    inputData = sys.stdin.readline().strip().split(' ')
    main(student, num, inputData)
