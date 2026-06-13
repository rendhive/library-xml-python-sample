import xml.etree.ElementTree as ET

xml_data = '''<root>
    <child>Old Content</child>
</root>'''

root = ET.fromstring(xml_data)
root.find('child').text = 'New Content'  # Mengubah isi elemen
print(ET.tostring(root, encoding='unicode'))  # Mengonversi kembali ke string
# Fungsi: Mengubah isi dari satu elemen dalam XML.
# Kondisi: Ketika Anda perlu memperbarui nilai yang sudah ada dalam struktur XML.