import threading
from threading import Timer
import time

def print_hello():
	print('hello')

def welcome(args):
	print(args)

def clock():
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
	t = Timer(1, clock)
	t.start()
	
def test_timer_start():
	Timer(5, print_hello).start()

def test_timer_cancel():
	t1 = Timer(3, print_hello)
	t2 = Timer(5, print_hello)
	
	t1.start()
	t2.start()
	
	time.sleep(4)
	
	t2.cancel()

def test_timer_param():
	t1 = Timer(3, welcome, ['Lily'])
	t1.start()
	
	'''
	error
	'''
	t2 = Timer(4, welcome, ['Lily', 'Bob'])
	t2.start()

def test_timer_clock():
	t = Timer(1, clock)
	t.start()


if __name__ == '__main__':
	test_timer_start()
	test_timer_cancel()
	test_timer_param()
	test_timer_clock()