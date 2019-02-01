import math


def ncr(n, r):
	return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


n = int(input('Enter the number of lines: '))

for i in range(n):
	print(' ' * (n - i - 1), end='')
	for j in range(i + 1):
		print(ncr(i, j), end=' ')
	print()
