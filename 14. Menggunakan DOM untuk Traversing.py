from xml.dom import minidom

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

dom = minidom.parseString(xml_data)
for child in dom.getElementsByTagName('child'):
    print(child.firstChild.data)  # Mengakses data tekstual di dalam child
# Fungsi: Menggunakan DOM untuk menelusuri file XML.
# Kondisi: Ketika Anda perlu fleksibilitas dalam melacak elemen di XML.