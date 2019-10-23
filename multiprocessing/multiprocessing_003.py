from multiprocessing import Pool

'''
use Pool to get return value
'''
def f(x):
	print(x*x)
	return x*2
	
def main():
	pool = Pool(4)
	result = []
	result.append(pool.apply_async(f, [1,]))
	result.append(pool.apply_async(f, [2,]))
	result.append(pool.apply_async(f, [3,]))
	pool.close()
	pool.join()
	out = map(lambda x: x.get(), result)
	[(print(o)) for o in out]

if __name__ == '__main__':
	main()