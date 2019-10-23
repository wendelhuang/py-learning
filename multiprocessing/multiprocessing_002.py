from multiprocessing import Pool
import multiprocessing
import time

def work(num):
	return num*num

def main():
	pool = Pool(3)
	r = pool.map(work, (1,2,3,))
	pool.close()
	pool.join()
	print(r)


if __name__ == '__main__':
	main()