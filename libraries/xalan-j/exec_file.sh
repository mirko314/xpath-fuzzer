#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
# OUTPUT="$(${DIR}/xmllib2.out $1 $2)"
java -cp ${DIR} XPathQueryExample $1 "$2"