DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
OUTPUT="$(basex -i ../inventory.xml "//book")"
echo "${OUTPUT}"