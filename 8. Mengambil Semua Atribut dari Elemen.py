import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child id="1" name="child1">Content 1</child>
    <child id="2" name="child2">Content 2</child>
</root>'''

root = ET.fromstring(xml_data)
for child in root:
    print(child.attrib)  # Mengambil semua atribut dari elemen
# Fungsi: Mengakses semua atribut dari elemen XML.
# Kondisi: Ketika Anda ingin mendapatkan semua informasi yang terasosiasi dengan elemen.