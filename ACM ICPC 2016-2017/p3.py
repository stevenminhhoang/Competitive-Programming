a = list(map(int, input().split()))
b = list(map(int, input().split()))
win = 0
lose = 0
# print(a)
# print(b)

for x in a:
    for y in b:
        if x > y:
            win = win + 1
        if x < y:
            lose = lose + 1

print("%.5f" % (win/(win + lose)))
