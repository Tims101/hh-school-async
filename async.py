def final_callback():
    # executes after all functions from async group were called
    print("final")    

def error_callback(e):
	print(e)
    # executed on error

def func1(*args):
	print("func1")

def func2(*args):
	print("func2")

def func3(*args):
	print("func3")

class AsyncGroup:

	observableFuncs = []

	def __init__(self, final_callback, error_callback):
		self.final_callback = final_callback
		self.error_callback = error_callback

	def add(self, func):
		def inner(*args, **kwargs):
			try:
				func(*args, **kwargs)	
				self.observableFuncs.remove(func);		
			except Exception as e:
				self.error_callback(e)
			finally: 
				if len(self.observableFuncs) == 0:
					self.final_callback();						
		self.observableFuncs.append(func);
		return inner;

group = AsyncGroup(final_callback, error_callback)

func1 = group.add(func1)
func2 = group.add(func2)
func3 = group.add(func3)

# ...

x = y = z = 0;
func1(x, y)
func2()
func3(z)

# now final_callback should be executed