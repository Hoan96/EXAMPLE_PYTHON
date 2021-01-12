import xml.etree.ElementTree as ET
tree = ET.parse('XXX.xml')
root = tree.getroot()
print(root[1].attrib)
