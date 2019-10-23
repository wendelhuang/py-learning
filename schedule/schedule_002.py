import psutil
import time
import os
import sched
'''
sched usage
'''

schedule = sched.scheduler(time.time, time.sleep)


def print_process(param):
	print('param: %s' % (param))
	pids = psutil.pids()
	print('----------------------------------')
	for i, pid in enumerate(pids):
		p = psutil.Process(pid)
		print('index: %d, pid: %d, pname: %s' % (i, pid, p.name()))
	schedule.enter(15, 0, print_process, ('Lily',))

def test_sched_process():
	schedule.enter(0, 0, print_process, ('Lily',))
	schedule.run()


if __name__ == '__main__':
	test_sched_process()