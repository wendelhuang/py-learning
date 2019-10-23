'''
usage of BackgroundScheduler
'''
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

def tick():
	print('Tick! The time is: %s' % (datetime.now()))

if __name__ == '__main__':
	scheduler = BackgroundScheduler()
	scheduler.add_job(tick, 'interval', seconds = 5)
	scheduler.start()
	
	try:
		while True:
			time.sleep(2)
			print('sleep')
	except(KeyboardInterrupt, SystemExit):
		scheduler.shutdown()
		print('Exit main')