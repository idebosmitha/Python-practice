l = list(map(int, input('Enter a list of numbers: ').split()))

l1 = [-1] * len(l)

for i in l:
	if l[i] >= 0:
		l1[l[i]] = l[i]

print(l1)
