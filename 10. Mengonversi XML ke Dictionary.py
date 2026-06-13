import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child id="1">Content 1</child>
    <child id="2">Content 2</child>
</root>'''

def xml_to_dict(elem):
    return {child.tag: child.text for child in elem}

root = ET.fromstring(xml_data)
result = xml_to_dict(root)
print(result)
# Fungsi: Mengonversi elemen XML menjadi struktur dictionary.
# Kondisi: Ketika Anda perlu menggunakan informasi XML dalam bentuk terstruktur.