import time

def test_time_strftime():
	t = time.gmtime()
	now = time.localtime(time.time())
	print(now)
	print(time.strftime('%Y-%m-%d %H:%M:%S', t))
	print(time.strftime('%Y-%m-%d %H:%M:%S', now))

def test_time_diff():
	time_str1 = '2019-10-18 14:00:00'
	time_str2 = '2019-10-18 14:05:00'
	
	stamp1 = time.strptime(time_str1, '%Y-%m-%d %H:%M:%S')
	stamp2 = time.strptime(time_str2, '%Y-%m-%d %H:%M:%S')
	
	t1 = time.mktime(stamp1)
	t2 = time.mktime(stamp2)
	
	diff = t2 - t1
	print(diff)

if __name__ == '__main__':
	test_time_strftime()
	test_time_diff()