n, m = map(int, input().split())
matrix = [['W' for i in range(m+2)] for j in range(n+2)]

# def printMatrix():
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             print(matrix[i][j],end='')
#         print()

# printMatrix()

def fill(a,b):
	if matrix[a][b] == 'W': return
	matrix[a][b] = 'W'
	fill(a+1,b)
	fill(a-1,b)
	fill(a,b-1)
	fill(a,b+1)


count = 0
for i in range(n):
    line = input()
    for j in range(m):
        matrix[i+1][j+1] = line[j]

for i in range(n):
	for j in range(m):
		if matrix[i+1][j+1] == 'L':
			count = count + 1
			fill(i+1,j+1)

print(count)
