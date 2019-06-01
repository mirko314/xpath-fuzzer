require "rexml/document"
include REXML
string = <<EOF
  <?xml version="1.0"?>
  <bookstore>
      <price>123</price>
      <price>456</price>
      <price>789</price>
      <price>234</price>
  </bookstore>
EOF
doc = Document.new string
puts XPath.match( doc, "//price>400")