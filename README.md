# xpath-fuzzer

## Setup
```
docker build docker -t xpath-fuzzer:latest
docker run -it xpath-fuzzer
# For Dev instead run docker run -v ${PWD}:/app -it myimage
```

## Run
There are 3 Tasks:
  - Generate xPaths or craft them manually (xpath_builder.py)
  - Test those xPaths against Libraries (supervisor.py)
  - Analyse Testresults (analyzer.py)
```
# Generate xPaths based on xPath functions with replaced parameters
python xpath_builder.py
# Test all input.txt lines on testfile/inventory.xml
python supervisor.py
# Or e.g. test xpath //book on testfile/inventory.xml
python supervisor.py //book
# Analyse the Output of the tests in output/
python analyzer.py
```
## Architecture
  - libraries/ contains subfolders for each supported xpath library with an exec_file.sh making it work
  - output/ contains the outputs of the current tests
  - testfiles/ contains the XML testfiles
  - xpath/ contains tools to build the xpath fuzzing inputs
    - input.txt gets read line by line and each line gets tested


## TODO
  - Setup Fixed Version numbers of libraries
  - Analyize Script
    - Strip Whitespace
    - Normalize Error Messages
    - Formatted Ouput in Console
    - Saving in file for analysing / visualization
  - xPath Generation Script
    - Legit xPaths
      - Functions
      - Distinguish by xPath version
    - Malicous Inputs
      - Malformed

## Open Questions
  - How to craft mailcious inputs effectivly

