
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#비밀번호 발음하기
#https://www.acmicpc.net/problem/4659

import sys

if __name__ == '__main__':
    pw = ''
    check = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ja_check = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    mo_check = ['a', 'e', 'i', 'o', 'u']
    inputData = []

    while(1):
        inputd = sys.stdin.readline().strip()
        if inputd == 'end':
            break
        inputData.append(inputd)


    for pw in inputData:
        first_check = False
        for d in mo_check:
            if d in pw:
                first_check = True

        second_check = True
        for cnt in range(len(pw)):
            mo_cnt = 0
            ja_cnt = 0
            if cnt+3 <= len(pw):
                for data in pw[cnt:cnt+3]:
                    if data in mo_check:
                        mo_cnt += 1
                    if data in ja_check:
                        ja_cnt += 1
                if mo_cnt == 3 or ja_cnt == 3:
                    second_check = False
                    break
            if second_check is False:
                break

        third_check = True
        for d in check:
            if (d + d) in pw:
                third_check = False

        if first_check and second_check and third_check:
            print('<' + pw + '> is acceptable.')
        else:
            print('<' + pw + '> is not acceptable.')
