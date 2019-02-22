from collections import Counter


# a = list(map(int, input('Enter an array: ').split()))

a = [1, 3, 1, 4, 1, 2, 2, 3, 1, 4, 2, 3, 3, 3, 3]

freq = dict()
for i in a:
	freq[i] = freq.get(i, 0) + 1
	# if i in freq:
	# 	freq[i] += 1
	# else:
	# 	freq[i] = 1

print(freq)

freq = {}
for i in set(a):
	freq[i] = a.count(i)
print(freq)


freq = {i:a.count(i) for i in set(a)}
print(freq)


freq = Counter(a)
print(freq)

items = list(freq.items())

max_number = max(items, key=lambda x: x[1])
print(max_number[0])
