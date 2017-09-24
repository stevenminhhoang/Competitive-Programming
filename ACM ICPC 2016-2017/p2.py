n,m = map(int, input().split())

def fix(row):
	for i in range(len(row)-1, -1, -1):
		for j in range(i+1, len(row)):
			if row[j-1] + row[j] == 'o.':
				row[j-1], row[j] = '.o'
	return row

print("\n".join("".join(x) for x in zip(*[fix(list(x)) for x in zip(*[input().strip() for _ in range(n)])])))
