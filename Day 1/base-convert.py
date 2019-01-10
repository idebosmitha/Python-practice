def convert_from_10(x, base):
	s = ''
	while x > 0:
		rem = x % base
		rem = str(rem) if rem < 10 else chr(65 + rem - 10)
		s = rem + s
		x //= base
	return s


n = input('Enter a number: ')
base = int(input('Enter its base: '))
to_base = int(input('Enter the base you want to convert it to: '))

x = int(n, base)
y = convert_from_10(x, to_base)

print(y)
