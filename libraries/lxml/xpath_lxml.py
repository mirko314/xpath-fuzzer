from lxml import etree
import sys

def readFile(filename):
  f = open(filename, "r")
  return f.read()

file_name = sys.argv[1]
xpath = sys.argv[2]
f = readFile(file_name)
tree = etree.parse(file_name)
results = tree.xpath(xpath, namespaces={
  'a': "https://a.com/",
  'b': "https://b.com/",
  'c': "https://c.com/",
  'd': "https://d.com/",
  'e': "https://e.com/"
})
if isinstance(results, list):
  for element in [s for s in results]:
    # if is attribute
    if isinstance(element, etree._ElementUnicodeResult):
      print(element)
    else:
      print(etree.tostring(element, pretty_print=True))
else:
  print(results)