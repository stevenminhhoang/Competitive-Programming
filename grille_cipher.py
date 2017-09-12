n = int(input())

grid = [['X' for i in range(n)] for j in range(n)]
ans =[['.' for i in range(n)] for j in range(n)]

for i in range(n):
    line = input()
    for j in range(n):
        grid[i][j] = line[j]

mes = input()

pos = 0
count = 0
valid = True

def fillIn():
    global pos
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                if ans[i][j] != '.':
                    global valid
                    valid = False
                    return
                ans[i][j] = mes[pos]
                pos = pos + 1


while count < 4:
    fillIn()
    count = count + 1
    grid = list(zip(*grid[::-1]))

def printGrid():
    for i in range(n):
        for j in range(n):
            print(ans[i][j], end = '')
        # print()


if count < 4:
    valid = False

for i in range(n):
    for j in range(n):
        if ans[i][j] == '.':
            valid = False

if valid == True:
    printGrid()
else:
    print('invalid grille')
