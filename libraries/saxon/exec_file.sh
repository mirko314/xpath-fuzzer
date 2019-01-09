#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
# OUTPUT="$(${DIR}/xmllib2.out $1 $2)"
java -cp ${DIR}:.:*:${DIR}/saxon9he.jar Saxon $1 "$2"