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
rootx = ET.Element("Root")
for x in TagMangement:
	xxx = str(x.ids)
	new = ET.Element("Tag",dict(TagID = xxx,TagName=x.name,TagAddress=x.addr,TagFunc=x.fun,TagValue=x.tagvalue))
	rootx.append(new)
treex = ET.ElementTree(rootx)
treex.write("newx.xml")