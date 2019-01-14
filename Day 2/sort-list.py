arr = list(map(int, input('Enter a list: ').split()))
l = len(arr)

arr_left = arr[:l//2]
arr_right = arr[l//2:]

arr_left.sort()
arr_right.sort(reverse=True)

arr_sorted = arr_left + arr_right
print(arr_sorted)
