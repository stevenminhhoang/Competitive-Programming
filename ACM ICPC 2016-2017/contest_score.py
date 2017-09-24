n,k = map(int, input().split())
time = []
for i in range(n):
    time.append(int(input()))

sorted_time = sorted(time[:k])

current = 0
ans = 0
selection = k

while len(sorted_time) > 0 :
    current = current + sorted_time.pop(0)
    ans = ans + current
    if selection < n :
        sorted_time.append(time[selection])
        selection = selection + 1


print(ans)
