while (True):
	n = int(input("Enter a number: "))
	if (n > 9):
		print("enter a lower number")
	else:
		break
for x in range(1, n + 1):
	for y in range(1, x + 1):
		print(y, end='')
	print()
