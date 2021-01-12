import xml.etree.ElementTree as ET

class Tag():
	"""docstring for Persion"""
	def __init__(self, ids,name,addr,fun,tagvalue):
		self.ids = ids
		self.name = name
		self.addr = addr
		self.fun = fun
		self.tagvalue = tagvalue

tree = ET.parse('XXX.xml')
root = tree.getroot()
TagMangement = []
#print(root[1].attrib)
for elem  in root:
	#print(elem.attrib['TagID'])
	tag = Tag(elem.attrib['TagID'],elem.attrib['TagName'],elem.attrib['TagAddress'],elem.attrib['TagFunc'],elem.attrib['TagValue'])
	TagMangement.append(tag)
for tagss in TagMangement:
	print(tagss.name)
data = ET.Element('')
items =ET.SubElement(data,'Root')
items.set('TagID','1')
items.set('TagName','NAME')
mydata = ET.tostring(data)
print(mydata)
myfile = open("new.xml","w")
myfile.write(mydata)