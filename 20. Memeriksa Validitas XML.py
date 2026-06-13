import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child>Content 1</child>
</root>'''

try:
    ET.fromstring(xml_data)  # Parsing validasi
    print("XML is valid.")
except ET.ParseError:
    print("XML is not valid.")
# Fungsi: Memeriksa validitas dari XML.
# Kondisi: Ketika Anda ingin memastikan bahwa XML yang di-processing adalah valid sebelum beroperasi.