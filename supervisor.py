import subprocess


def saveOutput(libaryName, inputId, output):
  f = open("output/" + inputId + "/" + libaryName + ".txt", "w")
  f.write(output)

def readInputs():
  f = open("xpath/input.txt", "r")
  return f.readlines()

def generateBashCmd(libaryName, testFileName, xpath):
  return 'sh ./docker/libaries/' + libaryName +'/exec_file.sh testfiles/' + testFileName + ' ' + xpath

def testLibary(libaryName, testFileName, xpath):
  bashCommand = generateBashCmd(libaryName, testFileName, xpath)
  process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
  output = process.stdout.readlines()
  saveOutput(libaryName, "1", "".join(output))
  print output
  output, error = process.communicate()

LIBARIES = ["xmllib2", "basex"]

for
testLibary("xmllib2", "inventory.xml", "//book")