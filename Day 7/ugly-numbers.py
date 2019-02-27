def is_ugly(n):
	i = 2
	while n != 1:
		while n % i == 0:
			if i > 5:
				return False
			n //= i
		else:
			i += 1
	return True


n = int(input('Enter n: '))
i, j = 0, 1

while i != n:
	if is_ugly(j):
		# print(j)
		i += 1
	j += 1

print(j - 1)
