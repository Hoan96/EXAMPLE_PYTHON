#define class
class Persion():
	"""docstring for Persion"""
	def __init__(self, ids,name,age):
		self.ids = ids
		self.name = name
		self.age = age
a = Persion(1,"HOAN",25)
xyz = []
for x in range(10):
	new = Persion(x,"NOW",25)
	xyz.append(new )

for x in xyz:
	print(str(x.ids))