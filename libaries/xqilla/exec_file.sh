#!/bin/bash
# DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
ps h -p $$ -o args='' | cut -f1 -d' '
OUTPUT="xqilla -i /home/testfiles/inventory.xml <( echo //book )"
echo "${OUTPUT}"
$(${OUTPUT})

# Does not work:
# echo "$(libaries/xqilla/exec_file.sh testfiles/inventory.xml //book)"
# Caught unknown exception

#Does work:
# xqilla -i testfiles/inventory.xml <( echo //book )