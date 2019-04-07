#!/bin/bash
# DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
# ps h -p $$ -o args='' | cut -f1 -d' '
# OUTPUT="xqilla -i /home/testfiles/inventory.xml <<< "//book"
xqilla  <( echo "declare namespace a=\"https://a.com/\";declare namespace b=\"https://b.com/\";declare namespace c=\"https://c.com/\";declare namespace d=\"https://d.com/\";declare namespace e=\"https://e.com/\";doc(\"$1\")$2" )

# commandline=(xqilla -i $1 <( echo "$2" ))