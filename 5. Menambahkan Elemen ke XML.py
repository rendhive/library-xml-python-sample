import xml.etree.ElementTree as ET

root = ET.Element("root")
child1 = ET.SubElement(root, "child")
child1.text = "Content 1"

child2 = ET.SubElement(root, "child")
child2.text = "Content 2"

print(ET.tostring(root, encoding='unicode'))
# Fungsi: Menambahkan elemen baru ke XML.
# Kondisi: Ketika Anda ingin membangun struktur XML secara programatik.