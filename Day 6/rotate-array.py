a = list(map(int, input('Enter an array: ').split()))
r = int(input('Enter the rotation value: '))

r %= len(a)

a = a[r:] + a[:r]

print(a)
