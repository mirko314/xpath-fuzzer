# xpath-fuzzer

## Setup
```
docker build docker -t myimage:latest
docker run -v ${PWD}:/app -it myimage
(cd /libraries/xmllib2 && make)
docker run -it myimage
```
## Architecture
  - libraries/ contains subfolders for each supported xpath library

## TODO
  - Setup Fixed Version numbers of libraries