s = [1, 5, 2, 4, 3]
s1 = []
for x in range(len(s) - 1):
	if s[x] < s[x+1]:
		s1.append(s[x+1])
print(s1)
