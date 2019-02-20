l1 = list(map(int, input('enter the elements of the first list: ').split()))
l2 = list(map(int, input('enter the elements of the second list: ').split()))
l3 = list(map(int, input('enter the elements of the third list: ').split()))

i1, i2, i3 = 0, 0, 0

while i1 < len(l1) and i2 < len(l2) and i3 < len(l3):
	if l1[i1] == l2[i2] == l3[i3]:
		print(l1[i1])
		i1 += 1
		i2 += 1
		i3 += 1
	elif l1[i1] <= l2[i2] and l1[i1] <= l3[i3]:
		i1 += 1
	elif l2[i2] <= l1[i1] and l2[i2] <= l3[i3]:
		i2 += 1
	elif l3[i3] <= l2[i2] and l3[i3] <= l1[i1]:
		i3 += 1
