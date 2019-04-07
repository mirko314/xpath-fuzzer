require "nokogiri"

file_name = ARGV[0]
xpath =  ARGV[1]
@doc = Nokogiri::XML(File.open(file_name))
puts @doc.xpath(xpath, {
  'a': "https://a.com/",
  'b': "https://b.com/",
  'c': "https://c.com/",
  'd': "https://d.com/",
  'e': "https://e.com/"
}) #, 'my' => 'uri:mynamespace'


# doc = Nokogiri::XML::Document.parse(open('../../xml_files_windows/standard.xml'),
#                                       url=nil,
#                                       encoding=nil,
# 									  options=Nokogiri::XML::ParseOptions::DTDLOAD
#                                       )

# puts doc.at_css("data").content


#doc  = Nokogiri::XSLT(File.read('../../xml_files_windows/optional/xslt.xsl'))

#puts doc.root
