#import mymodule as persion
from mymodule import persion
def my_funtion(*kids):
	print("Hello  from a funtion"+kids[2])

my_funtion("NAME","HHI","ÁDSD")

# Class
class Persion():
	"""docstring for Persion"""
	def __init__(self, name,age):
		self.name = name
		self.age = age
p1=Persion("Jione",36)
print(p1.age)
print(p1.name)
a = persion["age"]
print(a)
#######################