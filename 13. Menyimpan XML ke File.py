import xml.etree.ElementTree as ET

root = ET.Element('root')
child1 = ET.SubElement(root, 'child')
child1.text = 'Content 1'

tree = ET.ElementTree(root)
tree.write('output.xml')  # Menyimpan data XML ke file
# Fungsi: Menyimpan objek XML ke file.
# Kondisi: Ketika Anda perlu menyimpan hasil pemrosesan XML ke dalam file.