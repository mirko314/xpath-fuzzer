#!/bin/bash
# DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
# ps h -p $$ -o args='' | cut -f1 -d' '
# OUTPUT="xqilla -i /home/testfiles/inventory.xml <<< "//book"
xqilla -i $1 <( echo $2 )
