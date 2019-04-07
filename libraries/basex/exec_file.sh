#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
basex "declare namespace a=\"https://a.com/\";declare namespace b=\"https://b.com/\";declare namespace c=\"https://c.com/\";declare namespace d=\"https://d.com/\";declare namespace e=\"https://e.com/\";doc(\"$1\")$2"