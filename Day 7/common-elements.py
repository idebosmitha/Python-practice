a1 = set(map(int, input('Enter the first array: ').split()))
a2 = set(map(int, input('Enter the second array: ').split()))

commons = a1 & a2  # intersection
print(commons)

not_commons = a1 ^ a2  # symetric difference
print(not_commons)
