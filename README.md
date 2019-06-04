# xpath-fuzzer

## Setup
```
docker build . -t xpath-fuzzer:latest
docker run -it xpath-fuzzer /bin/bash
# For Dev instead run
docker run -v ${PWD}:/app -it myimage /bin/bash
```

## Run
There are 3 Tasks:
  - Generate xPaths or craft them manually (input_generation.sh)
  - Test those xPaths against Libraries (supervisor.py)
  - Analyse Testresults (analyzer.py)
```
# Generate xPaths using Grammarinator + ANTLR4
bash input_generation.sh

# Test all input.txt lines as XPath Expressions on testfile/testdocument.xml
python3 supervisor.py

# Analyse the Output of the tests in output/
python3 analyzer.py

# Quick Test Single XPath: e.g. //book on testfile/testdocument.xml
python3 supervisor.py //book
```
## Architecture
  - libraries/ contains subfolders for each supported xpath library with an exec_file.sh making it work
  - output/ contains the outputs of the current tests
  - testfiles/ contains the XML testfiles
  - xpath/input.txt gets read line by line and each line gets tested

## Namespace Prefixes
All Libraries except rexml only allow xpath expressions with namespace prefixes when those namespaces are bound to the uri explicitly.
We set up the libraries with 6 example namespace prefixes:
```
prefix 'a' is bound to https://a.com/
prefix 'b' is bound to https://b.com/
prefix 'c' is bound to https://c.com/
prefix 'd' is bound to https://d.com/
prefix 'e' is bound to https://e.com/
```
