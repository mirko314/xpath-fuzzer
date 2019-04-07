require "rexml/document"
include REXML

file_name = ARGV[0]
xpath =  ARGV[1]
with_example_namespaces = true
file = File.new( file_name )
@doc = REXML::Document.new file
namespaces = with_example_namespaces ? {
  'a'=> "https://a.com/",
  'b'=> "https://b.com/",
  'c'=> "https://c.com/",
  'd'=> "https://d.com/",
  'e'=> "https://e.com/"
}: nil
puts XPath.match( @doc, xpath, namespaces)