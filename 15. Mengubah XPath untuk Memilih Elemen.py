from xml.dom import minidom

xml_data = '''<root>
    <child id="1">Content 1</child>
    <child id="2">Content 2</child>
</root>'''

dom = minidom.parseString(xml_data)
child = dom.getElementsByTagName('child')[0]
print(child.getAttribute('id'))  # Mengambil atribut id
# Fungsi: Mengambil nilai atribut dari elemen menggunakan DOM.
# Kondisi: Ketika Anda ingin mendapatkan informasi lebih detail dari elemen.