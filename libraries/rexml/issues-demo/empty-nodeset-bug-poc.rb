require "rexml/document"
include REXML
puts XPath::VERSION
string = <<EOF
  <?xml version="1.0"?>
  <bookstore>
  </bookstore>
EOF
doc = Document.new string
puts XPath.match(doc, "boolean(/nonexistent)")
puts XPath.match(doc, "boolean(/nonexistent)=false()")
puts XPath.match( doc, "boolean(/nonexistent)>=false()")
puts XPath.match(doc, "number(true())")

# puts XPath.match( doc, "false()>=false()")