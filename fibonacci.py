def fib(max):
	a,b = 0,1
	while a < max:
		yield a
		a, b = b, a + b

class Fib:
	'''裴波那契序列生成'''
	def __init__(self,max):
		self.max = max

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def __next__(self):
		num = self.a
		if num > self.max:
			raise StopIteration
		self.a,self.b = self.b,self.a+self.b
		return "哈哈哈"
