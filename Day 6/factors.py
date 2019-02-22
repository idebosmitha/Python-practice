n = int(input('Enter a number: '))

f = 2
while n != 1:
	if n % f == 0:
		print(f)
		n /= f
	else:
		f += 1
