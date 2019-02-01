'''   
    1 0
   1 1 0
  1 2 1 0
 1 3 3 1 0
1 4 6 4 1 0
'''
n = int(input('Enter the number of lines: '))

p = [1]

for i in range(n):
	print(' ' * (n-i-1) + ' '.join(map(str, p)))
	p.append(0)
	for j in range(len(p) - 1, 0, -1):
		p[j] = p[j] + p[j - 1]
