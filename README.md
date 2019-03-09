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
bash input_generation.sh
<!-- python3 xpath_builder.py -->
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

cd antlr4/gramminator
rm tests/*
grammarinator-generate -l ./xpathCustomUnlexer.py -p ./xpathCustomUnparser.py -n 100 -d 20
for f in test*; do (cat "${f}"; echo) >> /app/xpath/input.txt; done
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
## Collected XPATHs
number(boolean(..))
count(..)
count(parent::*)


Libs sind sich nicht ganz sicher was denn jetzt der Root ist:
```
/.//./..
->
saxon.txt, xalan-j.txt, jaxen.txt: <?xml-stylesheettype
basex.txt: same  as saxon.txt, xalan-j.txt, jaxen.txt just with attribute reordering
lxml: <bookstorespecialty="novel">
VTD-Gen.txt, nokogiri.txt: <?xmlversion="1.0"?>
rexml.txt: same as but with simple quotes and attribute reordering
xqilla: <?xmlversion="1.1" BUMPS XML VERSION??

Same:
/|//child::*/.//..//parent::*

```

### TRUE OR FALSE 🤔
```
../@bookstore:bookstore<@first-name/..=.=preceding-sibling::book//bookstore/bookstore:book/.//@first-name>=//.>=..
  xqilla.txt, basex.txt, saxon.txt, lxml.txt, rexml.txt, nokogiri.txt:
  xalan-j.txt: false
  VTD-Gen.txt: Syntaxerrorafteroraroundtheendof==>
  jaxen.txt: true


'./..<../../@first-name<=..'
  xqilla.txt, basex.txt, saxon.txt, rexml.txt:
  lxml.txt: True
  xalan-j.txt, nokogiri.txt: true
  VTD-Gen.txt, jaxen.txt: false

'first-name:bookstore[.]'
  xqilla.txt, basex.txt, saxon.txt: true
  lxml.txt: False
  xalan-j.txt, VTD-Gen.txt, jaxen.txt, nokogiri.txt: false
  rexml.txt: truefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsetruefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalse

🙃 REXML kann sich nicht entscheiden und rastet richtig aus


./@bookstore:bookstore/parent::first-name:book>following::bookstore<=..!=/.
        xqilla.txt, basex.txt, saxon.txt, lxml.txt, nokogiri.txt:
        xalan-j.txt: false
        VTD-Gen.txt: Syntaxerrorafteroraroundtheendof==>
        rexml.txt, jaxen.txt: true
```

```
@first-name:bookstore//..=book:first-name
  xqilla.txt, basex.txt, saxon.txt, lxml.txt, rexml.txt, jaxen.txt, nokogiri.txt:
  xalan-j.txt: false
  VTD-Gen.txt: Syntaxerrorafteroraroundtheendof==>
```

### Was ist denn mit REXML los?
```
//@node:ancestor/..=ancestor-or-self::first-name:bookstore=.//.<=.
  xqilla.txt, basex.txt, saxon.txt, lxml.txt, jaxen.txt, nokogiri.txt:
  xalan-j.txt: true
  VTD-Gen.txt: Syntaxerrorafteroraroundtheendof==>
  rexml.txt: falsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalsefalse

//../../node//..!=//..
  xqilla.txt, basex.txt, saxon.txt, xalan-j.txt, VTD-Gen.txt, jaxen.txt, nokogiri.txt: false
  lxml.txt: False
  rexml.txt: truetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetruetrue

@book:book//.=//./.
  xqilla.txt, basex.txt, saxon.txt, lxml.txt, nokogiri.txt:
  xalan-j.txt, jaxen.txt: false
  VTD-Gen.txt: Syntaxerrorafteroraroundtheendof==>
  rexml.txt: [...]
```

### Xalan-J gibt gerne immer false zurück
```
//@ancestor:namespace//node>@book//./@first-name:bookstore
  xqilla.txt, basex.txt, saxon.txt, lxml.txt, rexml.txt, jaxen.txt, nokogiri.txt:
  xalan-j.txt: false
  VTD-Gen.txt: Syntaxerrorafteroraroundtheendof==>

//child::namespace:preceding-sibling/.!=..
  xqilla.txt, basex.txt, saxon.txt, lxml.txt, rexml.txt, jaxen.txt, nokogiri.txt:
  xalan-j.txt: false
  VTD-Gen.txt: Syntaxerrorafteroraroundtheendof==>

Manchmal aber auch Gerne true:
/..//.//node>/..<=//ancestor::node:comment//..//@descendant-or-self>=//./child::namespace/./parent::descendant-or-self
        xqilla.txt, basex.txt, saxon.txt, lxml.txt, rexml.txt, jaxen.txt, nokogiri.txt:
        xalan-j.txt: true
        VTD-Gen.txt: Syntaxerrorafteroraroundtheendof==>
```

```
.<//.//@descendant-or-self//.
  xqilla.txt, basex.txt, saxon.txt, xalan-j.txt, VTD-Gen.txt, jaxen.txt, nokogiri.txt: false
  lxml.txt: False
  rexml.txt:
```

Using True / False as switch for different elements:
```
<?xml version="1.0"?>
<doc>
  <data type="0">Evaluiert von BI</data>
  <data type='1'>Evaluiert von Authentication</data>
</doc>


root@8107130e187d:/app# python3 supervisor.py "//data[@type=number((./..<../..)<=..)]"
Welcome to the xPath Fuzzing Framework
Testing library: nokogiri , xpath: //data[@type=number((./..<../..)<=..)]
<data type="1">Evaluiert von Authentication</data>

Testing library: basex , xpath: //data[@type=number((./..<../..)<=..)]
[FORG0001] Cannot cast to xs:boolean: Evaluiert von BIEvaluiert von Au....

Testing library: xqilla , xpath: //data[@type=number((./..<../..)<=..)]
/dev/fd/63:1:1: error: Invalid lexical value [err:FORG0001]

Testing library: rexml , xpath: //data[@type=number((./..<../..)<=..)]
xpath_parser.rb:690:in `compare': undefined method `<=' for true:TrueClass

Testing library: xalan-j , xpath: //data[@type=number((./..<../..)<=..)]
<data type="1">Evaluiert von Authentication</data>

Testing library: saxon , xpath: //data[@type=number((./..<../..)<=..)]
; SystemID: ; Line#: 1; Column#: 37
ValidationException: The string "Evaluiert von BI\n  Evaluiert ..."
cannot be cast to a boolean

Testing library: jaxen , xpath: //data[@type=number((./..<../..)<=..)]
<data type="0">Evaluiert von BI</data>


Testing library: lxml , xpath: //data[@type=number((./..<../..)<=..)]
<data type="1">Evaluiert von Authentication</data>


Testing library: VTD-Gen , xpath: //data[@type=number((./..<../..)<=..)]
<data type="0">Evaluiert von BI</data>
Testing took: 4.069594621658325 seconds to test 9 libraries with 1 xPath expressions.
```

