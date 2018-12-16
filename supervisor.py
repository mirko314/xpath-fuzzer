import subprocess
import sys
import os

class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'
def saveOutput(libaryName, inputId, output):
  if not os.path.isdir("output/" + inputId + "/"):
    os.makedirs("output/" + inputId + "/")
  f = open("output/" + inputId + "/" + libaryName + ".txt", "w")
  f.write(output)

def readInputs():
  f = open("xpath/input.txt", "r")
  return f.readlines()

def generateBashCmd(libaryName, testFileName, xpath):
  return 'sh ./libaries/' + libaryName +'/exec_file.sh testfiles/' + testFileName + ' ' + xpath

def testLibary(libaryName, testFileName, xpath):
  bashCommand = generateBashCmd(libaryName, testFileName, xpath)
  process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
  return process.stdout.readlines()
  # output, error = process.communicate()

def printInstructions():
  print(color.BOLD + "Welcome to the xPath Fuzzing Framework" + color.END )
  print("To quickly check a custom xpath enter " + color.BOLD +"python supervisor.py \"yourxpath\"."+ color.END)
  print("Leave Blank to run every line as input in xpath/input.txt \n")

def checkMode():
  print(sys.argv)
  if len(sys.argv) == 1:
    return "all"
  else:
    return "quick"

LIBARIES = ["xmllib2", "basex"]
printInstructions()

MODE = checkMode()
if MODE == "all":
  xpaths = readInputs()
else:
  xpaths = [sys.argv[1]]

counter = 0
for xpath in xpaths:
  counter += 1
  for libaryName in LIBARIES:
    print(" ".join(["Testing Libary:", libaryName, ", xpath:", xpath]))
    output = testLibary(libaryName, "inventory.xml", xpath)
    if MODE == "all":
      saveOutput(libaryName, str(counter), "".join(output))
    else:
      print("".join(output))
