import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child id="1">Content 1</child>
    <child id="2">Content 2</child>
</root>'''

root = ET.fromstring(xml_data)
child2 = root.find('child[@id="2"]')
print(child2.text)  # Menggunakan XPath-like query
# Fungsi: Mencari elemen berdasarkan atribut.
# Kondisi: Ketika Anda ingin mendapatkan elemen spesifik berdasarkan nilai atribut.