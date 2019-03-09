from string import whitespace

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

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element.decode('utf-8'))
    return result

def cleanup_errors(string):
  return string.replace("Syntaxerrorafteroraroundtheendof==>", "") # VTD

def strip_whitespace(string_to_strip):
  return string_to_strip.translate({whitespace: None}).replace("\n", "").replace(" ", "")