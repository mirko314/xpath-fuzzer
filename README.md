# xpath-fuzzer

## Setup
```
docker build . -t xpath-fuzzer:latest
docker run -it xpath-fuzzer /bin/bash
# For Dev instead run
docker run -v ${PWD}:/app -it myimage /bin/bash
```

## Run
There are 3 Tasks:
  - Generate xPaths or craft them manually (xpath_builder.py)
  - Test those xPaths against Libraries (supervisor.py)
  - Analyse Testresults (analyzer.py)
```
# Generate xPaths based on xPath functions with replaced parameters
python3 xpath_builder.py
# Test all input.txt lines on testfile/inventory.xml
python3 supervisor.py
# Or e.g. test xpath //book on testfile/inventory.xml
python3 supervisor.py //book
# Analyse the Output of the tests in output/
python3 analyzer.py
```
## Architecture
  - libraries/ contains subfolders for each supported xpath library with an exec_file.sh making it work
  - output/ contains the outputs of the current tests
  - testfiles/ contains the XML testfiles
  - xpath/ contains tools to build the xpath fuzzing inputs
    - input.txt gets read line by line and each line gets tested


## TODO
  - Setup Fixed Version numbers of libraries
  - Analyize Script
    - Strip Whitespace
    - Normalize Error Messages
    - Formatted Ouput in Console
    - Saving in file for analysing / visualization
  - xPath Generation Script
    - Legit xPaths
      - Functions
      - Distinguish by xPath version
    - Malicous Inputs
      - Malformed

## Open Questions
  - How to craft mailcious inputs effectivly

## Testing XPath version:
  ```sh
  // XPath version> 2.0 :
  python3 supervisor.py "compare('abc', 'abc')"
  ```

## 🚧 Command Line collection notes (WIP) 🚧
```sh
diff -yw output/1/xqilla.txt output/1/rexml.txt
grun xpath main -tree
```

## XPath Parse Trees
```
//book/test/ads
(main (expr (orExpr (andExpr (equalityExpr (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot // (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book))))) / (step axisSpecifier (nodeTest (nameTest (qName (nCName test))))) / (step axisSpecifier (nodeTest (nameTest (qName (nCName ads)))))))))))))))))))
//book
(main (expr (orExpr (andExpr (equalityExpr (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot // (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book)))))))))))))))))))
//book[price>3]
(main (expr (orExpr (andExpr (equalityExpr (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot // (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book)))) (predicate [ (expr (orExpr (andExpr (equalityExpr (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName price)))))))))))) > (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (filterExpr (primaryExpr 3)))))))))))) ]))))))))))))))))

```
## Collected Errors
```
python3 supervisor.py "-name:bookstore[.]" :
Testing library: rexml , xpath: -name:bookstore[.]
/usr/lib/ruby/2.3.0/rexml/xpath_parser.rb:431:in `expr': undefined method `to_f' for []:Array (NoMethodError)
Did you mean?  to_s
               to_a
               to_h
	from /usr/lib/ruby/2.3.0/rexml/xpath_parser.rb:127:in `match'
	from /usr/lib/ruby/2.3.0/rexml/xpath_parser.rb:68:in `parse'
	from /usr/lib/ruby/2.3.0/rexml/xpath.rb:78:in `match'
	from /app/libraries/rexml/rexml.rb:9:in `<main>'
```