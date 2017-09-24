n = int(input())
seq = list(map(int, input().split()))
# print(seq)
arr = []

longest = 1

x = 0
previous = seq[0]
for i in range(n):
   if seq[i] != previous:
      diff = seq[i] - previous
      if x == 0 or diff * x < 0:
         longest = longest + 1
      previous = seq[i]
      x = diff

# print(arr)
print(longest)
