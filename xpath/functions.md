# XPath functions
copied from https://docs.oracle.com/cd/E35413_01/doc.722/e35419/dev_xpath_functions.htm#autoId62

## Operators
### Booleans
```
<=
<
>=
>=
!=
and
or
```
## Numbers
```
-expr
*
div
mod
+
-
```
### Node Sets
```
|
[expr]
/
//
```


## Node Set Functions [XPath §4.1]
```
number last()
number position()
number count(node-set)
node-set id(object)
string local-name(node-set?)
string namespace-uri(node-set?)
string name(node-set?)
String Functions [XPath §4.2]
string string(object?)
string concat(string, string, string*)
string starts-with(string, string)
string contains(string, string)
string substring-before(string, string)
string substring-after(string, string)
string substring(string, number, number?)
number string-length(string?)
string normalize-space(string?)
string translate(string, string, string)
```

## Boolean Functions [XPath §4.3]
```
boolean boolean(object)
boolean not(boolean)
boolean true()
boolean false()
```
## Number Functions [XPath §4.4]
```
number number(object?)
number sum(node-set)
number floor(number)
number ceiling(number)
number round(number)
```


# OSM Behavior XPath Functions:


## Node Set Functions
```
string matrix-concat(node-set,node-set,node-set?)
node-set evaluate(string)
node-set instance(string?) [Declarative Rules Only]
node-set match(node-set?, string)
```
## String Functions
```
string lower-case(string?)
string upper-case(string?)
string ends-with(string, string)
```
## Boolean Functions
```
boolean boolean-from-string(string)
object if(boolean, object, object)
```
## Number Functions
```
number avg(node-set)
number min(node-set)
number max(node-set)
number count-not-empty(node-set)
```