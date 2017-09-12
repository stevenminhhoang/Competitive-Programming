#!/usr/bin/python3

def doTreePrint(nDigits):
  for i in range(1,nR+1):
    for j in range(1,nC+1):
      print('.',end='')
      if nDigits == 3 and nums[i][j] < 10:
        print('.',end='')
      if nums[i][j] == 0:
        print('.',end='')
      else:
        print(nums[i][j],end='')
    print()

line = input()
splitLine = line.split(' ')
nR = int(splitLine[0])
nC = int(splitLine[1])

grid = []
nums = []
for i in range(nR+2):
  grid.append([])
  nums.append([])
  for j in range(nC+2):
    grid[i].append('.')
    nums[i].append(0)

for i in range(nR):
  line = input()
  for j in range(nC):
    grid[i+1][j+1] = line[j]
    if line[j] == 'T':
      nums[i+1][j+1] = -1

queue = []
for i in range(nR+2):
  for j in range(nC+2):
    if grid[i][j] == '.':
      queue.append(i)
      queue.append(j)

while len(queue) > 0:
    r = queue.pop(0)
    c = queue.pop(0)

    if r-1 > 0 and nums[r-1][c] == -1:
        nums[r-1][c] = nums[r][c] + 1
        queue.append(r-1)
        queue.append(c)

    if r+1 < nR+1 and nums[r+1][c] == -1:
        nums[r+1][c] = nums[r][c] + 1
        queue.append(r+1)
        queue.append(c)

    if c-1 > 0 and nums[r][c-1] == -1:
        nums[r][c-1] = nums[r][c] + 1
        queue.append(r)
        queue.append(c-1)

    if c+1 < nC+1 and nums[r][c+1] == -1:
        nums[r][c+1] = nums[r][c] + 1
        queue.append(r)
        queue.append(c+1)

# maxVal = 0
# for i in range(nR+2):
#   for j in range(nC+2):
#     if nums[r][c] > maxVal:
#       maxVal = nums[r][c]
#
# if maxVal < 10:
#   doTreePrint(2)
# else:
#   doTreePrint(3)
def printMatrix(arr):
    for i in range(0,nR+2):
        for j in range(0,nC+2):
            print(arr[i][j], end='')
        print()

printMatrix(grid)
printMatrix(nums)
