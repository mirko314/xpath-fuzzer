#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
# OUTPUT="$(${DIR}/xmllib2.out $1 $2)"
java -cp ${DIR}:${DIR}/*.jar:.:*:${DIR}/jaxen-1.1.16.jar jaxen $1 "$2"
