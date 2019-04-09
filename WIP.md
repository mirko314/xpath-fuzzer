

This prevents some XML signature wrapping attacks as an expression like
a:element
only will resolve to elements with the namespace a set to a.com.
Namespace Wrapping attacks are prevented.
Consider the following XML Document.
An Attacker might try to redefine Namespace Prefixes.
But since the Namespaces only resolved to the previously defined Prefix-NamespaceUri List, it is not possible to get the a:elem3 node using the xpath: "//a:elem3".
Instead nothing is returned by each library.
The outer a:elem1 is returned however when selected using "//a:elem1"
```
<a:elem1 xmlns:a="https://a.com">
 <b:elem2 xmlns:b="https://b.com">
   <a:elem3 xmlns:a="https://c.com"/>
 </b:elem2>
</a:elem1>
```

## Testing XPath version:
  ```sh
  // XPath version> 2.0 :
  python3 supervisor.py "compare('abc', 'abc')"
  ```

  basex, xqilla, saxon benutzen xpath v2

## 🚧 Command Line collection notes (WIP) 🚧
```sh
diff -yw output/1/xqilla.txt output/1/rexml.txt
grun xpath main -tree
(End with ctrl-d)

cd antlr4/gramminator
rm tests/*
grammarinator-generate -l ./xpathCustomUnlexer.py -p ./xpathCustomUnparser.py -n 100 -d 20
for f in test*; do (cat "${f}"; echo) >> /app/xpath/input.txt; done
```

## XPath Parse Trees

### Comparing = and >=
```
/book=/book
(main (expr (orExpr (andExpr (
  equalityExpr (
    relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot / (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book))))))))))))))
  =
    (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot / (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book))))))))))))))
)))))
```
```
/book>=/book
(main (expr (orExpr (andExpr (
  equalityExpr (
  relationalExpr (
    additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot / (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book))))))))))))
  )
  >=
    (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot / (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book)))))))))))))
))
))))
```

```
//book/test/ads
(main (expr (orExpr (andExpr (equalityExpr (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot // (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book))))) / (step axisSpecifier (nodeTest (nameTest (qName (nCName test))))) / (step axisSpecifier (nodeTest (nameTest (qName (nCName ads)))))))))))))))))))
//book
(main (expr (orExpr (andExpr (equalityExpr (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot // (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book)))))))))))))))))))
//book[price>3]
(main (expr (orExpr (andExpr (equalityExpr (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot // (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book)))) (predicate [ (expr (orExpr (andExpr (equalityExpr (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName price)))))))))))) > (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (filterExpr (primaryExpr 3)))))))))))) ]))))))))))))))))


/book>=/book
(main (expr (orExpr (andExpr (
  equalityExpr (
  relationalExpr (
    additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot / (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book))))))))))))
  )
  >=
    (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot / (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book)))))))))))))
))
))))

vs

/book=/book
(main (expr (orExpr (andExpr (
  equalityExpr (
    relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot / (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book))))))))))))))
  =
    (relationalExpr (additiveExpr (multiplicativeExpr (unaryExprNoRoot (unionExprNoRoot (pathExprNoRoot (locationPath (absoluteLocationPathNoroot / (relativeLocationPath (step axisSpecifier (nodeTest (nameTest (qName (nCName book))))))))))))))
)))))
```
## Collected Errors
```
'/bookstore=/bookstore'  in Folder: 009:
  xqilla(2.0), basex(2.0), saxon(2.0), lxml, xalan-j, rexml, jaxen, nokogiri: true
  VTD-Gen: false
------------------------------------------------------------
'/bookstore>=/bookstore'  in Folder: 010:
  xqilla(2.0), basex(2.0), saxon(2.0), rexml: true
  lxml, xalan-j, VTD-Gen, jaxen, nokogiri: false


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

```
Switchen zwischen xpath v1 und xpath v2 libs:
'//data[@type=number(..<=..)]'  in Folder: 004:
  xqilla(2.0), basex(2.0), saxon(2.0): <datatype="1">EvaluiertvonAuthentication</data>
  lxml, xalan-j, VTD-Gen, jaxen, nokogiri: <datatype="0">EvaluiertvonBI</data>
  rexml:
```

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

## Namespaces and prefixes
For the use of Namespace Prefixes we supply the libraries with the following mappings:

  'a': "https://a.com/",
  'b': "https://b.com/",
  'c': "https://c.com/",
  'd': "https://d.com/",
  'e': "https://e.com/"

###LXML:
Done
If your XPath expression uses namespace prefixes, you must define them in a prefix mapping. To this end, pass a dictionary to the namespaces keyword argument that maps the namespace prefixes used in the XPath expression to namespace URIs:
namespaces={'x': 'http://codespeak.net/ns/test1',
...                           'b': 'http://codespeak.net/ns/test2'})

https://lxml.de/xpathxslt.html

### Nokogiri
Done

###REXML
Done
https://ruby-doc.org/stdlib-1.9.3/libdoc/rexml/rdoc/REXML/XPath.html
Can have namespace mapping, yet not required.
Infers automatically then.
example to add:
XPath.first( node, "a/x:b", { "x"=>"http://doofus" } )

###VTD-Gen
Done

### jaxen
Done:

import org.jaxen.SimpleNamespaceContext;

import java.util.HashMap;
HashMap namespaceMap = new HashMap();
namespaceMap.put( "a", "https://a.com/");
namespaceMap.put( "b", "https://b.com/");
namespaceMap.put( "c", "https://c.com/");
namespaceMap.put( "d", "https://d.com/");
namespaceMap.put( "e", "https://e.com/");

org.jaxen.UnresolvableException: Cannot resolve namespace prefix 'a'
### saxon
javax.xml.xpath.XPathExpressionException: net.sf.saxon.trans.XPathException: Namespace prefix 'a' has not been declared
### basex
Use XQuery to declare namespace as variable
[XPST0081] No namespace declared for 'a:elem1'
Schwierig
Irgendwie so:
-b{URL}ln=value
"declare namespace ns='URL'; declare variable $ns:ln external; $ns:ln"
http://docs.basex.org/wiki/Command-Line_Options
### xqilla
Use XQuery to declare namespace as variable
https://stackoverflow.com/questions/19357644/how-to-define-namespaces-for-xpath-using-the-xqilla-commandline-tool
/dev/fd/63:1:3: error: No namespace for prefix 'a' [err:XPST0081]

declare namespace dc="http://purl.org/dc/elements/1.1/";
doc("my.file.xml")//dc:title

xalan-j
Done
Help found https://stackoverflow.com/questions/6390339/how-to-query-xml-using-namespaces-in-java-with-xpath