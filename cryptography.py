s = input()
key = list(input())
ans = []


for i in range(len(s)):
    ch = chr(ord('A') + (ord(s[i])-ord(key[i]) + 26) % 26)
    ans.append(ch)
    key.append(ch)

print(''.join(ans))
