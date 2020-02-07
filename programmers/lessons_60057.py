# [2020카카오공채] 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    # s = "aabbaccc"
    # 2a2ba3c
    answer = 0
    arr = []
    result= []
    cnt_arr = []
    for_cnt = 1
    #     arr.append(s[0:1])
    #     arr.append(s[1:2])

    #     for_cnt = 2
    #     arr.append(s[0:2])
    #     arr.append(s[2:4])

    #     for_cnt = len(s)

    for k in range(1, len(s)):
        for i in range(0 ,len(s), k):
            if i == 0:
                # print(i, k)
                arr.append(s[i:k])
                # print(s)
            else:
                # print(i, i+k)
                if i+k < len(s):
                    arr.append(s[i:i+k])
                else:
                    arr.append(s[i:])
        # print("----")
        # print(arr)

        temp = arr[0]
        cnt = 0
        for i in range(len(arr)):
            str_re = arr[i]
            if str_re == temp:
                cnt = cnt + 1
                if i == (len(arr)-1):
                    if cnt > 1:
                        result.append(str(cnt))
                    result.append(temp)
            else:
                if i == (len(arr)-1):
                    if cnt > 1:
                        result.append(str(cnt))
                    result.append(temp)
                    result.append(str_re)
                else:
                    if cnt > 1:
                        result.append(str(cnt))
                    result.append(temp)
                temp = str_re
                cnt = 1

        answer = len("".join(result)) 
        # print(answer)
        # print("".join(result))
        # print("----")
        result = []
        arr = []
        cnt_arr.append(answer)

    
    if len(cnt_arr) == 0:
        answer = 1
    else:
        answer = min(cnt_arr)
    return answer
