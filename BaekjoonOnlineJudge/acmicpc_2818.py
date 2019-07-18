#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 숙제하기 싫을 때
# https://www.acmicpc.net/problem/2818

'''
3 2

1 4
1 5
3 5

4번 반복시 원상태로 복귀하므로 전체 열에서 나누어서 합계를 더하고 나머지만 구한다.

1) start
  5
4 6 3 1
  2
  
2) right_move : 2) 주사위에서 첫번째 4를 마지막 1 의 자리로 이동
  5
6 3 1 4
  2
  
3) right_move : 2) 주사위에서 첫번째 6을 마지막 4 의 자리로 이동
  5
3 1 4 6
  2
  
2-1) left_move : 1) 주사위에서 마지막 3을 마지막 6 의 자리로 이동
  5
1 4 6 3
  2
  
2-1) down_move : 1) 주사위에서 5를 1의 자리로, 1은 2의 자리로, 2는 6의 자리로, 6은 5의 자리로 순환 이동 
  6
4 2 3 5
  1
'''

import sys

row_col = str(sys.stdin.readline().strip()).split(' ')

row = int(row_col[0])
col = int(row_col[1])

dice = [4, 6, 3, 1]
up = 5
down = 2

result_sum = 1

def right_move():
    global dice
    global up
    global down
    dice.append(dice[0])
    dice.pop(0)

def left_move():
    global dice
    global up
    global down
    temp = dice.pop()
    dice.insert(0, temp)

def down_move():
    global dice
    global up
    global down
    temp1 = dice[1]
    temp2 = dice[3]
    dice[1] = down
    dice[3] = up
    up = temp1
    down = temp2

right_check = True
left_check = False

for i in range(row):
    repeat = (col - 1) // 4
    result_sum += repeat * sum(dice)

    rest = (col - 1) % 4
    if i > 0:
        down_move()
        result_sum += dice[-1]
        #print('down move', dice, up, down)

    if right_check:
        for j in range(rest):
            right_move()
            result_sum += dice[-1]
        right_check = False
        left_check = True

        #print('right move', dice, up, down)
        continue

    if left_check:
        for j in range(rest):
            left_move()
            result_sum += dice[-1]
        right_check = True
        left_check = False

        #print('left move', dice, up, down)
        continue

print(result_sum)
