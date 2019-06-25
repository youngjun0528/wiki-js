#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

import sys

inputData = []
cnt = int(sys.stdin.readline().strip())
for i in range(cnt):
    inputNum = sys.stdin.readline().strip()
    inputData.append(int(inputNum))

for data in inputData:
    d = dict()
    d[1] = 1 # [1] : {1을 만들기 위한 방법}
    d[2] = 2 # [1+1, 2] : {2을 만들기 위한 방법}
    d[3] = 4 # [1+2, 2+1, 1+1+1, 3] : {3을 만들기 위한 방법}

    d[4] = d[3] + d[2] + d[1]
    # 4를 만들기 위해서
    # [1 + {3을 만들기 위한 방법}] + [2 + {2을 만들기 위한 방법}] + [3 + {1을 만들기 위한 방법}]
    d[5] = d[4] + d[3] + d[2]
    # 5를 만들기 위해서
    # [1 + {4을 만들기 위한 방법}] + [2 + {3을 만들기 위한 방법}] + [3 + {2을 만들기 위한 방법}]
    # [1 + [1 + {3을 만들기 위한 방법}] + [2 + {2을 만들기 위한 방법}] + [3 + {1을 만들기 위한 방법}]] + [2 + {3을 만들기 위한 방법}] + [3 + {2을 만들기 위한 방법}]

    for cnt in range(4, data+1):
        d[cnt] = d[cnt-1] + d[cnt-2] + d[cnt-3]

    print(d[data])
