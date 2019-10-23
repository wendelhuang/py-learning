from multiprocessing import Process
import multiprocessing
import time

def job1(dict):
	while True:
		print('job1 is doing, dict = %s' % (str(dict)))
		dict['job1'] = 'doing'
		time.sleep(3)
	
def job2(dict):
	while True:
		print('job2 is doing, dict = %s' % (str(dict)))
		dict['job2'] = 'doing'
		time.sleep(5)

def main(dict):
	p1 = Process(target=job1, args=(dict,))
	p2 = Process(target=job2, args=(dict,))
	p1.start()
	p2.start()
	
	time.sleep(10)
	while True:
		time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
		print(dict)
		print('%s: job1: %s, job2: %s' % (time_str, dict['job1'], dict['job2']))
		if (dict['job1'] != None and dict['job2'] != None):
			print('remove job state')
			del dict['job1']
			del dict['job2']
		time.sleep(10)


if __name__ == '__main__':
	dict = multiprocessing.Manager().dict()
	main(dict)