s = list(input())
arr = []
l = []

# longest = 1
for char in s:
    arr.append(ord(char))

print(arr)

length = 1

for i in range(len(s)-1):

    if arr[i+1]-arr[i] == 1:
        length = length + 1
    if arr[i+1]-arr[i] != 1:
        print(arr[i+1]-arr[i])
        l.append(length)
        length = 1

l.append(length)

# print(l)
