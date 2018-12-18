# xpath-fuzzer

## Setup
```
docker build docker -t myimage:latest
docker run -v ${PWD}:/app -it myimage
(cd /libraries/xmllib2 && make)
docker run -it myimage
```

## Run
```
# Test all input.txt lines on testfile/inventory.xml
python supervisor.py
# Or e.g. test xpath //book on testfile/inventory.xml
python supervisor.py //book
```
## Architecture
  - libraries/ contains subfolders for each supported xpath library with an exec_file.sh making it work
  - output/ contains the outputs of the current tests
  - testfiles/ contains the XML testfiles
  - xpath/ contains tools to build the xpath fuzzing inputs
    - input.txt gets read line by line and each line gets tested


## TODO
  - Setup Fixed Version numbers of libraries