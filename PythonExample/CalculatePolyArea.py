import math


def CalculatePolyArea(): # 다각형의 넓이 구하기
	polyPoint = [[0, 0], [10, 10], [0, 10], [10, 0]]
	vertex = 4
	mPoint = [0, 0] # 다각형 내의 임의의 점
	width = 0
	height = 0
	areaPoly = 0 # 다각형을 작은 삼각형으로 쪼갰을 때 - 밑변 : width, 높치 : height
	print(int(vertex/2))
	print(polyPoint[2][0])

	mPoint[0] = math.fabs((polyPoint[0][0] + polyPoint[int(vertex/2)][0]) / 2) # 다각형 내의 임의의 x좌표
	mPoint[1] = math.fabs((polyPoint[0][1] + polyPoint[int(vertex/2)][1]) / 2) # 다각형 내의 임의의 y좌표
	print(mPoint)
	for i in range(vertex): # 다각형 내의 쪼개진 모든 삼각형의 넓이를 구한다.
		width = math.sqrt(pow((polyPoint[i][0] - polyPoint[(i+1)%vertex][0]), 2) + pow((polyPoint[i][1] - polyPoint[(i+1)%vertex][1]), 2)) # 쪼개진 삼각형의 밑변의 길이
		print(polyPoint[i])
		print(polyPoint[(i+1)%vertex])
		height = GetDistanceLineToPoint(mPoint, polyPoint[i], polyPoint[(i+1)%vertex]) # 쪼개진 삼각형의 높이 (점과 직선 사이의 거리 공식 사용)
		areaPoly += (width * height) / 2 # 각각의 삼각형 넓이를 합한다.


	return areaPoly # 다각형의 넓이 return

def GetDistanceLineToPoint(mPoint, pPoint1, pPoint2): # 직선과 직선 밖의 한 점 사이의 길이 구하기
	m = 0
	d = 0 # m : 직선의 기울기, d : 점과 직선 사이의 거리
	# 직선의 상태를 확인하여 직선과 점의 정확한 길이를 구해낸다.
	if (pPoint1[0] == pPoint2[0]): # 직선이 y축과 평행하다면
		d = math.fabs(mPoint[0] - pPoint1[0])
	elif(pPoint1[1] == pPoint2[1]): # 직선이 x축과 평행하다면
		m = (pPoint2[1] - pPoint1[1]) / (pPoint2[0] - pPoint1[0])  # 직선의 기울기 구하기
		d = math.fabs(mPoint[1] - pPoint1[1])
	else: # 그 외는직선과 직선 밖의 한 점의 거리 공식 사용
		m = (pPoint2[1] - pPoint1[1]) / (pPoint2[0] - pPoint1[0])  # 직선의 기울기 구하기
		d = math.fabs(m*mPoint[0] - mPoint[1] - m*pPoint1[0] + pPoint1[1]) / math.sqrt((m * m) + ((-1) * (-1)))
	return d # 구해진 점과 직선 사이의 거리 값 return

print(CalculatePolyArea())
