require "rexml/document"
include REXML
string = <<EOF
  <?xml version="1.0"?>
  <bookstore>
  </bookstore>
EOF
doc = Document.new string
puts XPath.match( doc, "number(false())")
puts XPath.match( doc, "false()>=false()")