require "nokogiri"

file_name = ARGV[0]
xpath =  ARGV[1]
@doc = Nokogiri::XML(File.open(file_name))
puts @doc.xpath(xpath)


# doc = Nokogiri::XML::Document.parse(open('../../xml_files_windows/standard.xml'),
#                                       url=nil,
#                                       encoding=nil,
# 									  options=Nokogiri::XML::ParseOptions::DTDLOAD
#                                       )

# puts doc.at_css("data").content


#doc  = Nokogiri::XSLT(File.read('../../xml_files_windows/optional/xslt.xsl'))

#puts doc.root
