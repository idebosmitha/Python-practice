a = list(map(int, input('Enter an array of numbers: ').split()))
k = int(input('Enter the value of K: '))

values = set(a)

for i in a:
	if i not in values:
		continue
	if k-i in values:
		print(i, k-i)
		values.remove(k-i)
