arr = [1, 2, 3, 4, 5, 6, 7]
new_arr = []
'''
for x in range(len(arr)):
	if x == min(arr):
		min_el = x
		x = max(arr)
'''
min_el = min(arr)
max_el = max(arr)
for x in range(len(arr)):
	if (arr[x] == min_el):
		arr[x] = max_el
	elif (arr[x] == max_el):
		arr[x] = min_el
	new_arr.append(arr[x])
print(new_arr)
		
