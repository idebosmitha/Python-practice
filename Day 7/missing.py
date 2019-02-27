l = list(map(int, input().split()))
n = len(l) + 1

xor = n
for i in range(1, n):
	xor ^= i ^ l[i-1]

print(xor)

xor = n
for i, v in enumerate(l, 1):
	xor ^= v ^ i 

print(xor)
