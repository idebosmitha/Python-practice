x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

a, b = x, y
while b != 0:
	a, b = b, a%b

print(f'GCD: {a}')
print(f'LCM: {x * y // a}')

# print('GCD:', a, sep='@')
# print('GCD: ' + str(a))
