import xml.etree.ElementTree as ET

xml_data = '''<root xmlns:ns="http://example.com/ns">
    <ns:child>Content 1</ns:child>
</root>'''

root = ET.fromstring(xml_data)
child = root.find('{http://example.com/ns}child')  # Menggunakan namespace
print(child.text)
# Fungsi: Mengelola XML dengan namespace.
# Kondisi: Ketika Anda bekerja dengan XML yang menggunakan namespace XML.