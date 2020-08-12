import collections

def solution(s):
    answer = True
    deq = collections.deque([])
    # 여는 괄호 수와 닫는 괄호 수가 같아야지 올바른 괄호
    # 아니면 불필요한 계산을 줄이기 위해 False
    if s.count('(') != s.count(')'):
        return False
    else:
        idx = 0
        for i in s:
            if i == '(': # 여는 괄호 추가
                deq.append(i)
            elif idx == 0 and i == ')': # 첫번째부터 닫는 괄호이면 False
                return False
            elif idx > 0 and i == ')': # 두번째부터 닫는 괄호와 쌍을 이루는 여는 괄호가 있는지 확인
                check = deq.pop()
                if check == ')':
                    deq.append(check)
            # 만약 deq에 아무것도 없다면 index 값을 0으로 초기화
            # 마치 처음과 같은 상태로
            if len(deq) == 0:
                idx = 0
            else:
                idx += 1
            print(deq)
        if len(deq) > 0:
            return False
        else:
            return True

print(solution("()))(("))
