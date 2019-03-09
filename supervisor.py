import subprocess
from multiprocessing import Pool
import sys
import os
import time
from util import color
from util import concatenate_list_data
from util import strip_whitespace
from util import cleanup_errors

PARALLEL_PROCESSES = 1

def saveOutput(libraryName, inputId, inputString, output):
  if not os.path.isdir("output/" + inputId + "/"):
    os.makedirs("output/" + inputId + "/")
    f = open("output/" + inputId + "/xpath.txt", "w")
    f.write(inputString)

  f = open("output/" + inputId + "/" + libraryName + ".txt", "w")
  output = strip_whitespace(output)
  output = cleanup_errors(output)
  f.write(output)

def readInputs():
  f = open("xpath/input.txt", "r")
  return f.readlines()

def generateBashCmd(libraryName, testFileName, xpath):
  return ['bash', 'exec_file.sh', '/app/testfiles/' + testFileName, xpath]

def testlibrary(libraryName, testFileName, xpath):
  bashCommand = generateBashCmd(libraryName, testFileName, xpath)
  process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, cwd='/app/libraries/' + libraryName )
  return concatenate_list_data(process.stdout.readlines())
  # output, error = process.communicate()

def testAndSaveOutput(libraryName, testFileName, xpath, counter):
  output = testlibrary(libraryName, "inventory.xml", xpath)
  saveOutput(libraryName, str(counter), xpath, output)

def testAndPrintOutput(libraryName, testFileName, xpath, _counter):
  print(" ".join(["Testing library:", libraryName, ", xpath:", xpath]))
  output = testlibrary(libraryName, "inventory.xml", xpath)
  print("".join(output))

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

# LIBRARIES = ["xmllib2", "basex", "xqilla"]
LIBRARIES = ["nokogiri", "basex", "xqilla", "rexml", "xalan-j", "saxon", "jaxen", "lxml", "VTD-Gen"]
printInstructions()

MODE = checkMode()
if MODE == "all":
  xpaths = readInputs()
else:
  xpaths = [sys.argv[1]]

now = time.time()
args = []
counter = 0
for xpath in xpaths:
  counter += 1
  args = args + list(map(lambda lib: [lib, "inventory.xml", xpath, str(counter)], LIBRARIES))
print(args)
if MODE == "all":
  with Pool(PARALLEL_PROCESSES) as p:
    p.starmap(testAndSaveOutput, args)
else:
  for arg in args:
    testAndPrintOutput(*arg)
time_used = time.time() - now
print("Testing took: " + str(time_used) + " seconds to test " + str(len(LIBRARIES)) + " libraries with " + str(counter) + " xPath expressions." )
