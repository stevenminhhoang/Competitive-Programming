s = input()
# print(s[0:2])

bestLength = len(s)
for i in range(len(s)-1):
    for j in range(1,len(s)):
        substring = s[i:j+1]
        length = len(s.replace(substring, 'M')) + len(substring)
        if length < bestLength:
            bestLength = length

print(bestLength)
