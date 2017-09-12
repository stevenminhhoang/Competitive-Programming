degree = 0
pos = 0

def cw():
    global degree
    global pos
    degree += 9
    pos = (pos - 1 + 40) % 40

def ccw():
    global degree
    global pos
    degree += 9
    pos = (pos + 1) % 40

flag = True
while flag:
    s = list(map(int, input().split()))
    if all([s[i] == 0 for i in range(4)]):
        flag = False
        break
    degree = 0
    pos = s[0]
    for i in range(80):
        cw()
    while pos != s[1]:
        cw()
    for i in range(40):
        ccw()
    while pos != s[2]:
        ccw()
    while pos != s[3]:
        cw()
    print(degree)
