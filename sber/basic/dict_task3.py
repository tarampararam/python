s = ['abc', 'abc', 'abc']
d = dict()

for x in s:
#	if x not in d:
	d.setdefault(x, 0)
	if x in d:
		d[x] += 1
print(d)
