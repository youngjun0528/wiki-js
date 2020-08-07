# https://www.crocus.co.kr/773
# ttps://www.programmersought.com/article/91912312744/
# https://justicehui.github.io/ps/2019/03/27/BOJ9525/
MAX_N = 102
map = [[0]*MAX_N for _ in range(MAX_N)]
col = [[0]*MAX_N for _ in range(MAX_N)]
row = [[0]*MAX_N for _ in range(MAX_N)]

adj = [[0]*5002 for _ in range(5002)]
aMatch = [[0]*5002 for _ in range(5002)] # vector < int >
bMatch = [[0]*5002 for _ in range(5002)] # vector < int >
visit = [[0]*5002 for _ in range(5002)];
visitCnt = 0
n = 0
m = 0

def dfs(a : int) -> bool :
    global aMatch
    global bMatch
    global adj
    global visit
    global visitCnt
    if visit[a] == visitCnt:
        return False
    visit[a] = visitCnt
    for next in range(len(adj[a])):
        b = adj[a][next]
        if bMatch[b] == -1 or dfs(bMatch[b]):
            aMatch[a] = b
            bMatch[b] = a
            return True
    return False

def bipartiteMatch() -> int:
    global n
    global m
    global visitCnt
    global aMatch
    global bMatch
    aMatch = [-1]*(n - 1)
    bMatch = [-1]*(m + 1)

    ans = 0
    for a in range(n):
        visitCnt += 1
        ans += dfs(a)
    return ans


# 5
# X....
# X....
# ..X..
# .X...
# ....X
n = 5
inputData = [
            ['X','.','.','.','.'],
            ['X','.','.','.','.'],
            ['.','.','X','.','.'],
            ['.','X','.','.','.'],
            ['.','.','.','.','X']
           ]
map = []
for inputRow in inputData:
    inputRowInit = []
    for inputCol in inputRow:
        if inputCol == 'X':
            inputRowInit.append(1)
        else:
            inputRowInit.append(0)
    map.append(inputRowInit)

# 행 기준으로 넘버링
cnt = 1
check = False
for i in range(n):
    check = False
    for j in range(n):
        if map[i][j] == 0:
            col[i][j] = cnt
            check = True
        else:
            if check:
                cnt += 1
                check = False
    if check:
        cnt += 1

# 열 기준으로 넘버링
cnt = 1
for j in range(n):
    check = False
    for i in range(n):
        if map[i][j] == 0:
            row[i][j] = cnt
            check = True
        else:
            if check:
                cnt += 1
                check = False
    if check:
        cnt += 1

maxR = 0
maxC = 0

# 1 인 곳은 이분 그래프에 포함되지 않도록 한다.
for i in range(n):
    for j in range(n):
        if map[i][j] == 0:
            adj[row[i][j]].append((col[i][j]))
            maxR = max(maxR, row[i][j])
            maxC = max(maxC, col[i][j])

# 이제는 n, m으로 보는 것이 아닌 넘버링 단위로 봐야한다.
n = maxR
m = maxC
get = bipartiteMatch()
print(get)
