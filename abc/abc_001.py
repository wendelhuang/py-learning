'''
'''
from abc import ABCMeta

'''
class MyABC:
	__metaclass__ = ABCMeta
'''
class MyABC(metaclass=ABCMeta):
	pass

MyABC.register(tuple)
assert issubclass(tuple, MyABC)
assert isinstance((), MyABC)

