INPUTFILE = "xpath/input.txt"
FUNCTIONSFILE = "xpath/functions.txt"

# In future: use array of things to input
mapping = {
  'object': '//book',
  'number': '123',
  'node-set': '//book',
  'string': 'testabc'
}

def save_inputs(inputs):
  f = open(INPUTFILE, "w")
  f.writelines("\n".join(xpath_return))

def get_functions():
  f = open(FUNCTIONSFILE, "r")
  return f.readlines()

xpath_functions = get_functions()
# Save all xPaths in xpath_return
xpath_return = []
for xpath_function in xpath_functions:
  #remove return type
  xpath_function = xpath_function.split(' ', 1)[1]
  # replace params types by values
  for k, v in mapping.iteritems():
    xpath_parameters = xpath_function[xpath_function.find('(')::]
    rest = xpath_function[:xpath_function.find('('):]
    xpath_function = rest + xpath_parameters.replace(k, v)
  # remove conditional ? *
  xpath_function = xpath_function.replace('?', '')
  xpath_function = xpath_function.replace('*', '')
  xpath_function = xpath_function.strip()
  xpath_return.append(xpath_function)

print(xpath_return)
save_inputs(xpath_return)

