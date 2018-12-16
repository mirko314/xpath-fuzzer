bashCommand = "sh ./docker/libaries/basex/exec_file.sh"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
print process.stdout.readlines()
print "test"
output, error = process.communicate()