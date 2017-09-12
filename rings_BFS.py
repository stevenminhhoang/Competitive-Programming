row, col = map(int, input().split())

def printTree():
    for i in range(1,row+1):
        for j in range(1,col+1):
            if maxValue >= 10:
                print('.',end='')
            if nums[i][j] == 0:
                print('..',end='')
            elif nums[i][j] >= 10:
                print(nums[i][j],end='')
            else:
                print('.',nums[i][j],end='',sep='')
        print()

# def printMatrix(arr):
#     for i in range(0,row+2):
#         for j in range(0,col+2):
#             print(arr[i][j], end='')
#         print()

matrix = [['.' for i in range(col+2)] for j in range(row+2)]
nums = [[0 for i in range(col+2)] for j in range(row+2)]

queue = []

for i in range(row):
    line = input()
    for j in range(col):
        if line[j] == 'T':
            matrix[i+1][j+1] = 'T'
            nums[i+1][j+1] = -1

for i in range(row+2):
    for j in range(col+2):

        if matrix[i][j] == '.':
            queue.append(i)
            queue.append(j)

while len(queue) > 0:
    r = queue.pop(0)
    c = queue.pop(0)


    if  r-1 > 0 and nums[r-1][c] == -1:
        nums[r-1][c] = nums[r][c] + 1
        queue.append(r-1)
        queue.append(c)

    if r+1 < row+1 and nums[r+1][c] == -1:
        nums[r+1][c] = nums[r][c] + 1
        queue.append(r+1)
        queue.append(c)

    if c-1 > 0 and nums[r][c-1] == -1:
        nums[r][c-1] = nums[r][c] + 1
        queue.append(r)
        queue.append(c-1)

    if c+1 < col+1 and nums[r][c+1] == -1:
        nums[r][c+1] = nums[r][c] + 1
        queue.append(r)
        queue.append(c+1)

maxValue = 0
for i in range(row + 2):
    for j in range(col + 2):
        if nums[i][j] > maxValue:
            maxValue = nums[i][j]

printTree()
