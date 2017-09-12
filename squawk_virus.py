n,m,s,t = map(int, input().split())

adjacent_list = []
squawks_in = [0 for x in range(n)]
squawks_out = [0 for x in range(n)]

for i in range(n):
    adjacent_list.append([])

squawks_out[s] = 1

for i in range(m):
    x,y = map(int, input().split())
    adjacent_list[x].append(y)
    adjacent_list[y].append(x)


for time in range(t):
    for i in range(n):
        for j in adjacent_list[i]:
            squawks_in[j] =  squawks_in[j] + squawks_out[i]
    for i in range(n):
        squawks_out[i] = squawks_in[i]
        squawks_in[i] = 0


number_of_squawks = sum(squawks_out)
print(number_of_squawks)
