
f = open("xpath/functions.txt", "r")
xpath_functions = f.readlines()

mapping = {
  'object': '//book',
  'number': '123',
  'node-set': '//book',
  'string': 'testabc'
}
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
  print(xpath_function)

