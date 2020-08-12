board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
answer = 0;

lengthY = len(board)
lengthX = len(board[0])
max = 0

# 행이나 열의 길이가 2 미만이라면 직접 돌리면서 1이 하나라도 있는지 체크 합니다.
# 하나라도 있으면 통과.
if lengthY < 2 or lengthY < 2:
    for i in range(lengthY):
        for j in range(lengthX):
            if board[i][j] == 1:
                max = 1
else:
    # 첫 번째 행열을 제외시키기 위해서 i와 j에 1을 할당합니다.
    for i in range(1, lengthY):
        for j in range(1, lengthX):
            # 1이 아닐 경우 패스! 1인 값만 동적으로 변경해 줍니다.
            if board[i][j] == 1 :
                #현재 값의 좌측값, 상단값, 좌측상단값 중 최소값에 +1을 해줍니다.
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1
                # 다시 배열을 돌리는 수고를 하지않기 위해서 max값을 찾아 저장해 줍니다.
                if (board[i][j] > max):
                    max = board[i][j]
print(board)
print(pow(max, 2))
