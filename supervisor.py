import subprocess


def saveOutput(libaryName, inputId, output):
  f = open("output/" + inputId + "/" + libaryName + ".txt", "w")
  f.write(output)

def readInputs():
  f = open("xpath/input.txt", "r")
  return f.readlines()

def generateBashCmd(libaryName, testFileName, xpath):
  return 'sh ./docker/libaries/' + libaryName +'/exec_file.sh testfiles/' + testFileName + ' ' + xpath



process = subprocess.Popen(generateBashCmd("basex", "inventory.xml", "//book").split(), stdout=subprocess.PIPE)
output = process.stdout.readlines()
saveOutput("basex", "1", "".join(output))
print output
output, error = process.communicate()