n = int(input('Enter the number of terms: '))
s = 0

for i in range(1, n + 1):
	s += 1 / i

print(s)
print('%.3f' %s)
print('{:.3f}'.format(s))
print(f'{s:.3f}')

print(sum(1/i for i in range(1, int(input('Enter the number of terms: '))+1)))
