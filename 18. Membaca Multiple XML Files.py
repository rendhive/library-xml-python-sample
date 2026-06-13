import xml.etree.ElementTree as ET
import glob

xml_files = glob.glob('*.xml')  # Membaca semua file XML di direktori
for file in xml_files:
    tree = ET.parse(file)
    root = tree.getroot()
    print(f"Root tag of {file}: {root.tag}")
# Fungsi: Membaca banyak file XML dalam satu proses.
# Kondisi: Ketika Anda ingin mengelola banyak file XML secara bersamaan.