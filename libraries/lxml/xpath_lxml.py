from lxml import etree
import sys

def readFile(filename):
  f = open(filename, "r")
  return f.read()

file_name = sys.argv[1]
xpath = sys.argv[2]
f = readFile(file_name)
tree = etree.parse(file_name)
results = tree.xpath(xpath)
if isinstance(results, list):
  for element in results:
    print(etree.tostring(element).decode("utf-8"))
else:
  print(results)