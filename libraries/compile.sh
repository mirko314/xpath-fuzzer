# Compile Java Libs
#!/bin/bash

# Compile Java libs
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
# Xalan-j
cd ${DIR}/xalan-j && javac XPathQueryExample.java