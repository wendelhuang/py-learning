class test(object):
	def __init__(self):
		print('init')
	def __call__(self, *args, **kwargs):
		print('call')
	def __new__(cls, *args, **kwargs):
		print('new')
		return super(test, cls).__new__(cls, *args, **kwargs)
		
t = test()
#t()