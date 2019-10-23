'''
usage of BackgroundScheduler param
'''
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time

def tick(dict):
	print(dict)
	print('Tick! The time is: %s, dict["key"] = %s' % (datetime.now(), dict['key']))

if __name__ == '__main__':
	scheduler = BackgroundScheduler()
	dict = {}
	dict['key'] = 'value'
	scheduler.add_job(tick, 'cron', second = '*/1', args=(dict,))
	scheduler.start()
	
	try:
		while True:
			time.sleep(2)
			print('sleep')
	except(KeyboardInterrupt, SystemExit):
		scheduler.shutdown()
		print('Exit main')