

#https://velog.io/@04_miffy/N-Rook
import copy

# NxN 사이즈의 0 으로 초기화한 배열을 만들어주는 함수
# param: n
# return: 2 - d array
def initList(n):
    ret = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        ret.append(temp)
    return ret

totalRet = []
count = 0
table = []

# 인자로 받은 행(row) 에서 가능한 열(c) 를 모은 후보 배열(candidate)을 반환하는 함수
# N - Queen 이기 때문에, 열만 생각하면 됨
# param: row
# return: array
def getCandidate(getRow, n):
    global table
    candidate = []
    for c in range(n):
        isPromising = True
        for r in range(getRow):
            if (table[r][c] == 1):
                isPromising = False
                break
        if (isPromising):
            candidate.append(c)
    return candidate

# backtracking 을 하는 함수
# param: row
# return: none
def backtracking(row, n):
    global totalRet
    global table
    global count
    if (row == n):
        totalRet.append(copy.deepcopy(table) )
        count = count + 1
    else:
        candidate = getCandidate(row, n)
        for col in range(len(candidate)):
            table[row][candidate[col]] = 1
            backtracking(row + 1, n)
            table[row][candidate[col]] = 0

# n - rook 문제를 푸는 함수
# param: n
# return: count
def rook(n):
    global table
    global count
    table = initList(n)
    backtracking(0, n)
    return count

print(rook(5))
# 1, 2, 6, 24, 120
