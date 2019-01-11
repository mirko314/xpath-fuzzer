#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
# OUTPUT="$(${DIR}/xmllib2.out $1 $2)"
python3 ${DIR}/xpath_lxml.py $1 "$2"