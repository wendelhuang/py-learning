import re

def m(s):
	return re.compile(s)

def test():
	arr = ['A', 'B', 'C']
	brr = [m(str) for str in arr]
	for r in brr:
		print(type(r))
		print(r)
	crr = [(re.compile(str)) for str in arr]
	[(print(r)) for r in crr]
	
	drr = map(m, arr)
	[(print(r)) for r in drr]

if __name__ == '__main__':
	test()