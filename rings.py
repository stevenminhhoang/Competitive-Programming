row,col = map(int, input().split())

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

matrix = [['.' for i in range(col+2)] for j in range(row+2)]
nums = [[0 for i in range(col+2)] for j in range(row+2)]

for i in range(row):
    line = input()
    for j in range(col):
        if line[j] == 'T':
            matrix[i+1][j+1] = 'T'
            nums[i+1][j+1] = -1

for level in range(1,(max(row, col) // 2 + 1)):
    for i in range(1,row+1):
        for j in range(1,col+1):
            left = nums[i][j-1]
            right = nums[i][j+1]
            up = nums[i-1][j]
            down = nums[i+1][j]
            if nums[i][j] == -1 and (left == level - 1 or right == level - 1 or up == level - 1 or down == level - 1):
                nums[i][j] = level

maxValue = 0
for i in range(row + 2):
    for j in range(col + 2):
        if nums[i][j] > maxValue:
            maxValue = nums[i][j]

printTree()
