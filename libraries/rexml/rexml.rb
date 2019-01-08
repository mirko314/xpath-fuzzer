require "rexml/document"
include REXML

file_name = ARGV[0]
xpath =  ARGV[1]
file = File.new( file_name )
@doc = REXML::Document.new file

puts XPath.match( @doc, xpath )