#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
# OUTPUT="$(${DIR}/xmllib2.out $1 $2)"
java -cp ${DIR}:${DIR}/*.jar:.:*:${DIR}/vtd-xml_2.13_4.jar vtdgen $1 "$2"
