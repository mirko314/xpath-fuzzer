#!/bin/bash
cd antlr4/gramminator
rm tests/*
grammarinator-generate -l ./xpathCustomUnlexer.py -p ./xpathCustomUnparser.py -n 500 -d 25
rm /app/xpath/input.txt
for f in tests/test*; do (cat "${f}"; echo) >> /app/xpath/input.txt; done