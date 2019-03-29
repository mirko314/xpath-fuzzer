import os
import filecmp
import textwrap
from util import color
from util import concatenate_list_data
from util import strip_whitespace

def multipleReplace(text, wordDict):
  for key in wordDict:
      text = text.replace(key, wordDict[key])
  return text

def addXPathVersion(libraries):
  lib_to_xpath = {
    "xqilla": "xqilla(2.0)",
    "basex": "basex(2.0)",
    "saxon": "saxon(2.0)",
  }
  return map(lambda x: multipleReplace(x, lib_to_xpath), libraries)

def remove_file_type(file_name):
  return file_name[:-4]

def readFile(filename):
  f = open(filename, "r")
  return f.read()

def save_output_array(xpath_query, foldername, results):
  # Results:
  # [Array of different Testresults of type: [Array of Libraries, Testresult of those Libraries]]
  # If all Libs have the same result, dont output anything
  # if len(results) == 1:
  #   return
  print("------------------------------------------------------------")
  print( "'" + xpath_query.strip() + "'  in Folder: " + folder + ": ")
  for result in xpath_results:
    libraries = map(lambda x: x[:-4], result[0])
    libraries = addXPathVersion(libraries)

    test_result = color.BOLD + result[1] + color.END
    print("  " + (", ").join(libraries) + ": " + test_result[:25] +  textwrap.shorten(test_result[25:], 40))


def compare_results(result1, result2):
  return strip_whitespace(result1) == strip_whitespace(result2)

print("Starting to analyze the outputs of /output.")
# For every Folder in Output:
folders_to_analyse = os.listdir("output")
for _count, folder in enumerate(sorted(folders_to_analyse)):
  files = os.listdir("output/" + folder)
  xpath_results = []
  xpath_query = readFile("output/" + folder + "/xpath.txt")
  files.remove("xpath.txt")
  for i in range(len(files)):
    second_file_name = "output/" + folder + "/" + files[i]
    second_file_content = readFile(second_file_name)
    found_existing_result = False
    for result in xpath_results:
      if compare_results(second_file_content, result[1]):
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
  save_output_array(xpath_query, folder, xpath_results)


print("Finished to analyze the outputs of /output.")

