'''
test daemon process can not create process
'''

from multiprocessing import Process
import os
import time


def daemon_process():
	print('deamon_process pid: %d start' % (os.getpid()))
	time.sleep(6)
	print('deamon_process pid: %d end' % (os.getpid()))

def main():
	print('main pid %d start' % (os.getpid()))
	p = Process(target=daemon_process)
	# daemon process will end as main process
	p.daemon = True
	p.start()
	time.sleep(3)
	print('main pid %d end' % (os.getpid()))
	
if __name__ == '__main__':
	main()