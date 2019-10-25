class test(object):
	def a(self):
		self.name = 'lily'
		
	def b(self):
		print('I am %s' % (self.name))
t = test()
#t.b()
t.a()
print(t.name)
t.b()