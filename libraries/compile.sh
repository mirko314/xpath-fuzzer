# Compile Java Libs
#!/bin/bash

# Compile Java libs
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
# Xalan-j
cd ${DIR}/saxon && javac -cp .:*:saxon9he.jar Saxon.java
cd ${DIR}/xalan-j && javac -cp ${DIR}/xalan-j:saxon9he.jar XPathQueryExample.java
cd ${DIR}/jaxen && javac -cp .:*:jaxen-1.1.16.jar jaxen.java


# Xalan-j
# cd ${DIR}/xalan-j && javac -cp ${DIR}/xalan-j XPathQueryExample.java
# cd ${DIR}/xalan-j && javac -cp ${DIR}/xalan-j Saxon.java