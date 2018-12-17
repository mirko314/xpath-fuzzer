# xpath-fuzzer

## Setup
```
docker build docker -t myimage:latest
docker run -v ${PWD}:/home -it myimage
(cd /libaries/xmllib2 && make)
docker run -it myimage
```

## TODO
  - Setup Fixed Version numbers of Libaries