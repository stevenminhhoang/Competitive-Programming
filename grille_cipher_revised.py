import itertools
n = int(input())

grid = [['X']*n for i in range(n)]
ans =[['.']*n for i in range(n)]

def printGrid(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = '')
        # print()

for i in range(n):
    line = input()
    for j in range(n):
        grid[i][j] = line[j]

mes = input()
valid = True
pos = 0

for rep in range(4):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                if ans[i][j] != '.':
                    valid = False
                    break
                ans[i][j] = mes[pos]
                pos = pos + 1


    # printGrid(grid)
    grid = list(zip(*grid[::-1]))



for i in range(n):
    for j in range(n):
        if ans[i][j] == '.':
            valid = False


if valid == True:
    printGrid(ans)
else:
    print('invalid grille')
