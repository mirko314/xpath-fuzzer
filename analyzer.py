import os
import filecmp

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

# For every Folder in Output:
for folder in os.listdir("output"):
  files = os.listdir("output/" + folder)
  files.remove("xpath.txt")
  for i in range(len(files)):
    for i2 in range(i + 1, len(files)):
      files_equal = filecmp.cmp("output/" + folder + "/" + files[i], "output/" + folder + "/" + files[i2])
      output = ": output/" + folder + "/" + files[i] + " mit: " + "output/" + folder + "/" + files[i2]
      if files_equal:
        output = color.BLUE + "EQUAL Result:     " + output + color.END
      else:
        output = color.RED + "DIFFERENT Result: " +  output + color.END
      print(output)