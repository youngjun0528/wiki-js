# https://www.crocus.co.kr/773
# https://www.programmersought.com/article/91912312744/
# https://justicehui.github.io/ps/2019/03/27/BOJ9525/
def dfs(x):
    visited[x]=1
    for nx in path[x]:
        if col[nx]==-1 or (not visited[col[nx]] and dfs(col[nx])):
            row[x]=nx
            col[nx]=x
            return 1
    return 0


n = 5
D = [
    ['X','.','.','.','.'],
    ['X','.','.','.','.'],
    ['.','.','X','.','.'],
    ['.','X','.','.','.'],
    ['.','.','.','.','X']
   ]

R=[[-1]*n for _ in range(n)]
C=[[-1]*n for _ in range(n)]

r,c=0,0

# 행 기준으로 넘버링
now1,now2=0,0
for i in range(n):
    if now1!=0:
        r += 1
        now1 = 0
    for j in range(n):
        if D[i][j]=='.':
            R[i][j] = r
            now1 += 1
        if D[i][j]=='X' and now1!=0:
            r += 1
            now1 = 0
print(R)

# 열 기준으로 넘버링
for j in range(n):
    if now2!=0:
        c+=1
        now2=0
    for i in range(n):
        if D[i][j]=='.':
            C[i][j]=c
            now2+=1
        if D[i][j]=='X' and now2!=0:
            c+=1
            now2=0
print(C)

r += 1
c += 1
path=[[] for _ in range(r)]
for i in range(n):
    for j in range(n):
        if R[i][j]>=0 and C[i][j]>=0:
            path[R[i][j]].append(C[i][j])
print(path)
row=[-1]*r
col=[-1]*c
res=0
print(r)
for i in range(r):
    if row[i]==-1:
        visited=[0]*r
        if dfs(i):
            res+=1
print(res)
print(row)
print(col)


