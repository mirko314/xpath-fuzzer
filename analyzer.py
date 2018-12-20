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

def readFile(filename):
  f = open(filename, "r")
  return f.readlines()

print("Starting to analyze the outputs of /output.")
# For every Folder in Output:
folders_to_analyse = os.listdir("output")
for folder in folders_to_analyse:
  files = os.listdir("output/" + folder)
  xpath_results = []
  xpath_query = readFile("output/" + folder + "/xpath.txt")[0]
  files.remove("xpath.txt")
  for i in range(len(files)):
    second_file_name = "output/" + folder + "/" + files[i]
    second_file_content = readFile(second_file_name)
    found_existing_result = False
    for result in xpath_results:
      if second_file_content == result[1]:
        result[0].append(files[i])
        found_existing_result = True
        break
    if not found_existing_result:
      xpath_results.append([[files[i]], second_file_content])
    # xpath_results should now have an array with:
    # [[ [libname1, libnam2], "xpathresult"], [libname3, libnam4], "xpathresult2"]]
    # output = ": " + file_name + " mit: " + second_file_name
    # if files_equal:
    #   output = color.BLUE + "EQUAL Result:     " + output + color.END
    # else:
    #   output = color.RED + "DIFFERENT Result: " +  output + color.END
  print(xpath_query.strip() + " (Folder: " + folder + "): " + str(xpath_results))
print("Finished to analyze the outputs of /output.")