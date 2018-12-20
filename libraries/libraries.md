# Supported xPath libraries

## General list of Libaries
### libxml2 and libxslt:
XMLStarlet easy to use tool to test/execute XPath commands on the fly.
https://en.m.wikipedia.org/wiki/XMLStarlet

xmllint (libxml2)

libxml2
https://en.m.wikipedia.org/wiki/Libxml2

RaptorXML Server from Altova supports XPath 1.0, 2.0, and 3.0
BASIC	Edit
Pavuk XML Processor for QM/BASIC[8]

Pathan ( Discontiued?? )
pugixml ( No easy CLI, No easy example for xPath found)
Sedna XML Database, XML Database, no easy xpath CLI, https://en.m.wikipedia.org/wiki/Sedna_(database)
VTD-XML, Java?, Article on how to xpath https://dzone.com/articles/vtd-xml-parser, probably writing a java file necessary, https://vtd-xml.sourceforge.io/userGuide/0.html
Xalan
XQilla
Free Pascal	Edit
The unit XPath is included in the default libraries
Implementations for database engines	Edit
OpenLink Virtuoso
Java	Edit
Saxon XSLT supports XPath 1.0, XPath 2.0 and XPath 3.0 (as well as XSLT 2.0, XQuery 3.0, and XPath 3.0)
BaseX (also supports XPath 2.0 and XQuery)
VTD-XML
Sedna XML Database Both XML:DB and proprietary.
QuiXPath a streaming open source implementation by Innovimax
Xalan
Dom4j
The Java package javax.xml.xpath has been part of Java standard edition since Java 5 [9] via the Java API for XML Processing. Technically this is an XPath API rather than an XPath implementation, and it allows the programmer the ability to select a specific implementation that conforms to the interface.

JavaScript	Edit
jQuery XPath plugin based on Open-source XPath 2.0 implementation in JavaScript
FontoXPath Open source XPath 3.1 implementation in JavaScript. Currently under development.
.NET Framework	Edit
In the System.Xml and System.Xml.XPath namespaces[10]
Sedna XML Database
Perl	Edit
XML::LibXML (libxml2)
PHP	Edit
Sedna XML Database
Python	Edit
The ElementTree XML API in the Python Standard Library includes limited support for XPath expressions
libxml2
Amara
Sedna XML Database
lxml
Scrapy[11]
Ruby	Edit
libxml2[12]
Nokogiri
Scheme
Sedna XML Database
SQL	Edit
MySQL supports a subset of XPath from version 5.1.5 onwards[13]
PostgreSQL supports XPath and XSLT from version 8.4 on[14]
Tcl	Edit
The tdom package provides "a very complete, compliant and fast XPath implementation in C"


## xqilla
Options:
```
Usage: xqilla [options] <XQuery file>...
-h                : Show this display
-p                : Parse in XPath 3.0 mode (default is XQuery mode)
-P                : Parse in XPath 1.0 compatibility mode (default is XQuery mode)
-s                : Parse XSLT 2.0
-f                : Parse using W3C Full-Text extensions
-u                : Parse using W3C Update extensions
-e                : Parse using XQilla specific extensions
-d                : Run the query in interactive debugging mode
-x                : Use the Xerces-C data model (default is the FastXDM)
-i <file>         : Load XML document and bind it as the context item
-b <baseURI>      : Set the base URI for the context
-v <name> <value> : Bind the name value pair as an external variable
-o <file>         : Write the result to the specified file
-n <number>       : Run the queries a number of times
-q                : Quiet mode - no output
-t                : Output an XML representation of the AST
```