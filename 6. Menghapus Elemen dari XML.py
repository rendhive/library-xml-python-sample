import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child>Content 1</child>
    <child>Content 2</child>
</root>'''

root = ET.fromstring(xml_data)
root.remove(root[0])  # Menghapus elemen pertama
print(ET.tostring(root, encoding='unicode'))
# Fungsi: Menghapus elemen dari XML.
# Kondisi: Ketika Anda perlu menghapus data yang tidak diperlukan.