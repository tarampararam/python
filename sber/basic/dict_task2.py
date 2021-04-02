d = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
value = str(input('enter a value: '))

for k, v in d.items():
	if (v == value):
		print(k)
