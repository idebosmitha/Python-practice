n = int(input('Enter the number of terms: '))

a, b = 0, 1
print(a, end='')
for i in range(n - 2):
	print(", ", b, end='')
	a, b = b, a + b



# Geneator version of fibonacci
# Skip this if you're a beginner
def fib():
	a, b = 0, 1
	yield a
	while True:
		yield b
		a, b = b, a + b


for i, val in enumerate(fib()):
	if i == 10:
		break
	print(val)
