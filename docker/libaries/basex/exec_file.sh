DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
OUTPUT="basex -i $1 $2"
# echo "${OUTPUT}"
echo "$(${OUTPUT})"