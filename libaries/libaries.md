# Supported xPath Libaries

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