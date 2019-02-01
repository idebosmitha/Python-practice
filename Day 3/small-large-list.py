l = list(map(int, input('Enter a list of numbers: ').split()))

l.sort()
new_list = list()
n = len(l)

for i in range(n//2 + 1):
	new_list.append(l[i])
	if i == n//2 and n%2 != 0:
		break
	new_list.append(l[-(i + 1)])

print(new_list)