import xml.etree.ElementTree as ET

# Pastikan Anda memiliki file 'data.xml' di direktori yang sama
tree = ET.parse('data.xml')
root = tree.getroot()
print(root.tag)  # Menampilkan tag root
# Fungsi: Membaca dan mem-parsing file XML dari file eksternal.
# Kondisi: Ketika Anda ingin memproses data XML yang disimpan dalam file.